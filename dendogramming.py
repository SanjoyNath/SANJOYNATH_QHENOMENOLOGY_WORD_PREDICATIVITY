import logging
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from collections import Counter, defaultdict
from nltk import pos_tag, word_tokenize, ngrams
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

# Calculate n-gram frequencies
def calculate_ngrams(words, n=2):
    return Counter(ngrams(words, n))

# Calculate word relatedness (co-occurrence) with a sliding window
def calculate_word_relatedness(words, window_size=10):
    relatedness = defaultdict(Counter)
    for i, word1 in enumerate(words):
        for word2 in words[i+1:i+window_size]:
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

# Split text into manageable chunks for analysis
def chunk_text(text, chunk_size=10000):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i + chunk_size])

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

# Main function to analyze text and create word graphs
def analyze_text(text, pdf_path=None):
    try:
        svg_files = []
        pdf_files = []

        # Process chunks of text
        for chunk in chunk_text(text):
            words = preprocess_text(chunk)

            word_freqs = calculate_word_frequencies(words)
            relatedness = calculate_word_relatedness(words)

            # Export data to CSV
            export_word_frequencies_to_csv(word_freqs)
            export_graph_data_to_csv(relatedness)

            # Generate word cloud and save as SVG
            wordcloud_file = 'wordcloud.svg'
            visualize_wordcloud(word_freqs, output_file=wordcloud_file)
            svg_files.append(wordcloud_file)

            # Generate and save word graphs
            pdf_files.extend(split_and_generate_pdf_pages(relatedness, word_freqs))

        # Combine all generated PDF files into one
        combined_pdf = 'combined_word_graphs.pdf'
        combine_pdfs(pdf_files, combined_pdf)

        # If provided, generate text dump from PDF
        if pdf_path:
            generate_text_dump_from_pdf(pdf_path)

        print("Analysis complete.")
        return combined_pdf, svg_files

    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")
        print(f"An error occurred during analysis: {e}")

# GUI for file selection
def select_pdf_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path

if __name__ == '__main__':
    pdf_file_path = select_pdf_file()
    if pdf_file_path:
        try:
            # Extract text from PDF and analyze it
            with open(pdf_file_path, 'rb') as file:
                text = ""
                pdf_reader = PdfReader(file)
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text

            if text:
                analyze_text(text, pdf_path=pdf_file_path)
            else:
                print("No text found in the PDF.")
        except Exception as e:
            logging.error(f"Failed to process the selected PDF file: {e}")
            print(f"Failed to process the selected PDF file: {e}")
    else:
        print("No PDF file selected.")
