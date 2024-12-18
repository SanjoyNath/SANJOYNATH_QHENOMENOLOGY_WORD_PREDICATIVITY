import logging
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from collections import Counter, defaultdict
from nltk import pos_tag, word_tokenize, ngrams, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
from tkinter import Tk, filedialog
from PyPDF2 import PdfWriter, PdfReader
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import io
import string

# Initialize NLP tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

logging.basicConfig(filename='error.log', level=logging.ERROR)

# Convert POS tag to WordNet format
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN  # Default to noun if no match

# Preprocess text: Tokenize, lemmatize, and remove stopwords/punctuation
def preprocess_text(text):
    words = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(word) for word in words if word not in stop_words and word not in string.punctuation]

# Calculate word frequencies
def calculate_word_frequencies(words):
    return Counter(words)

# Split text into sentences and calculate word count for each sentence
def split_sentences_with_word_count(text):
    sentences = sent_tokenize(text)
    return [(sentence, len(word_tokenize(sentence))) for sentence in sentences]

# Calculate window sizes for each sentence in the text
def calculate_window_sizes(sentences):
    sentence_data = split_sentences_with_word_count(sentences)
    window_sizes = []
    
    for i, (sentence, current_count) in enumerate(sentence_data):
        prev_count = sentence_data[i-1][1] if i > 0 else 0
        next_count = sentence_data[i+1][1] if i < len(sentence_data) - 1 else 0
        
        backward_window = prev_count + current_count
        forward_window = current_count + next_count
        window_sizes.append((sentence, backward_window, forward_window))
    
    return window_sizes

# Calculate word relatedness using custom window sizes
def calculate_word_relatedness(text):
    sentences_with_window_sizes = calculate_window_sizes(text)
    relatedness = defaultdict(Counter)
    
    # Process each sentence using its forward and backward window size
    for i, (sentence, back_size, forward_size) in enumerate(sentences_with_window_sizes):
        words = preprocess_text(sentence)
        all_window_words = []

        # Collect words from backward and forward windows
        if i > 0:
            back_words = preprocess_text(sentences_with_window_sizes[i - 1][0])
            all_window_words.extend(back_words[:back_size])
        if i < len(sentences_with_window_sizes) - 1:
            forward_words = preprocess_text(sentences_with_window_sizes[i + 1][0])
            all_window_words.extend(forward_words[:forward_size])

        # Calculate co-occurrences of words within the window
        for word1 in words:
            for word2 in all_window_words:
                if word1 != word2:
                    relatedness[word1][word2] += 1

    return relatedness

# Create and visualize a word cloud
def visualize_wordcloud(word_freqs, output_file='wordcloud.svg', title='Word Cloud'):
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_freqs)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(title, fontsize=16)
    plt.savefig(output_file, format="svg")
    plt.close()

# Export word relatedness data to CSV
def export_graph_data_to_csv(relatedness, filename='word_relatedness.csv'):
    rows = [[word1, word2, weight] for word1, connections in relatedness.items() for word2, weight in connections.items()]
    pd.DataFrame(rows, columns=['Word1', 'Word2', 'Weight']).to_csv(filename, index=False)

# Visualize word relatedness graph
def visualize_word_graph(relatedness, word_freqs, output_file='word_graph.svg'):
    G = nx.Graph()
    for word1, connections in relatedness.items():
        for word2, weight in connections.items():
            if word1 != word2 and weight > 1:
                G.add_edge(word1, word2, weight=weight)

    pos = nx.circular_layout(G)  # Circular layout for clear visualization
    edge_weights = [G[u][v]['weight'] for u, v in G.edges()]

    plt.figure(figsize=(12, 12))
    nx.draw_networkx_nodes(G, pos, node_size=[word_freqs.get(node, 1) * 300 for node in G.nodes()], node_color='skyblue', alpha=0.7)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=[w * 0.2 for w in edge_weights], edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()}, font_size=10, font_color='red')

    plt.title("Word Relatedness Graph", fontsize=16)
    plt.tight_layout()
    plt.savefig(output_file, format="svg")
    plt.close()

# Export word frequencies to CSV
def export_word_frequencies_to_csv(word_freqs, filename='word_frequencies.csv'):
    pd.DataFrame.from_dict(word_freqs, orient='index', columns=['Frequency']).sort_values(by='Frequency', ascending=False).to_csv(filename)

# Convert SVG to PDF
def convert_svg_to_pdf(svg_file, pdf_file):
    try:
        drawing = svg2rlg(svg_file)
        renderPDF.drawToFile(drawing, pdf_file)
    except Exception as e:
        logging.error(f"Failed to convert SVG to PDF: {e}")

# Generate PDFs for specific weight ranges in word relatedness
def split_and_generate_pdf_pages(relatedness, word_freqs):
    weight_ranges = [(i, i + 1000) for i in range(0, 30000, 1000)]  # Extended weight ranges
    pdf_files = []

    for min_weight, max_weight in weight_ranges:
        G = nx.Graph()
        for word1, connections in relatedness.items():
            for word2, weight in connections.items():
                if min_weight <= weight < max_weight:
                    G.add_edge(word1, word2, weight=weight)

        if len(G.nodes()) > 0:
            output_file = f'word_graph_{min_weight}_{max_weight}.svg'
            visualize_word_graph(relatedness, word_freqs, output_file=output_file)
            pdf_file = output_file.replace('.svg', '.pdf')
            convert_svg_to_pdf(output_file, pdf_file)
            pdf_files.append(pdf_file)

    return pdf_files

# Combine PDF files
def combine_pdfs(pdf_files, output_pdf='output.pdf'):
    pdf_writer = PdfWriter()
    for pdf_file in pdf_files:
        try:
            with open(pdf_file, 'rb') as f:
                pdf_reader = PdfReader(f)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
            with open(output_pdf, 'wb') as pdf_output:
                pdf_writer.write(pdf_output)
        except Exception as e:
            logging.error(f"Failed to process PDF file {pdf_file}: {e}")

# Generate text dump from PDF
def generate_text_dump_from_pdf(pdf_path):
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        if text:
            text_file_path = pdf_path.replace('.pdf', '_dump.txt')
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

            logging.info(f"Text dump saved to {text_file_path}")
            print(f"Text dump saved to {text_file_path}")
        else:
            logging.warning("No text found in the PDF.")
            print("No text found in the PDF.")

    except Exception as e:
        logging.error(f"Failed to generate text dump: {e}")
        print(f"Failed to generate text dump: {e}")

# Read text from file
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Analyze text and create word graphs
def analyze_text(text, pdf_path=None):
    try:
        svg_files = []
        pdf_files = []

        words = preprocess_text(text)
        word_freqs = calculate_word_frequencies(words)
        relatedness = calculate_word_relatedness(text)

        # Export data to CSV
        export_word_frequencies_to_csv(word_freqs)
        export_graph_data_to_csv(relatedness)

        # Generate word cloud and save as SVG
        wordcloud_file = 'wordcloud.svg'
        visualize_wordcloud(word_freqs, output_file=wordcloud_file)
        svg_files.append(wordcloud_file)

        # Generate graph and save as SVG
        word_graph_file = 'word_graph.svg'
        visualize_word_graph(relatedness, word_freqs, output_file=word_graph_file)
        svg_files.append(word_graph_file)

        # Split graphs into weight ranges and generate PDFs
        pdf_files = split_and_generate_pdf_pages(relatedness, word_freqs)

        # Combine all PDFs into one
        if pdf_files:
            combine_pdfs(pdf_files, output_pdf=pdf_path if pdf_path else 'combined_output.pdf')

    except Exception as e:
        logging.error(f"Failed to analyze text: {e}")
        print(f"Failed to analyze text: {e}")

# Main function to run the program
def main():
    try:
        # Open a file dialog to select a text file
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])

        if not file_path:
            print("No file selected.")
            return

        text = read_text_from_file(file_path)

        if text:
            analyze_text(text)

    except Exception as e:
        logging.error(f"Failed to run the program: {e}")
        print(f"Failed to run the program: {e}")

if __name__ == "__main__":
    main()
