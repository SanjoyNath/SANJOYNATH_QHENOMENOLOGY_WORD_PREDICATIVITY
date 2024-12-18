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
from PyPDF2 import PdfReader
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
    return wordnet.NOUN

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

# Calculate word relatedness (co-occurrence) within sentences
def calculate_word_relatedness(sentences):
    relatedness = defaultdict(Counter)
    for sentence in sentences:
        words = preprocess_text(sentence)
        for i, word1 in enumerate(words):
            for word2 in words[i+1:]:
                if word1 != word2:
                    relatedness[word1][word2] += 1
                    relatedness[word2][word1] += 1
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
    rows = [[word1, word2, weight] for word1, connections in relatedness.items() for word2, weight in connections.items() if weight > 0]
    pd.DataFrame(rows, columns=['Word1', 'Word2', 'Weight']).sort_values(by='Weight', ascending=False).to_csv(filename, index=False)

# Visualize word relatedness graph
def visualize_word_graph(relatedness, word_freqs, output_file='word_graph.svg'):
    G = nx.Graph()
    for word1, connections in relatedness.items():
        for word2, weight in connections.items():
            if weight > 0:
                G.add_edge(word1, word2, weight=weight)

    pos = nx.spring_layout(G)  # Spring layout for clear visualization
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
    sentences = sent_tokenize(text)
    for i in range(0, len(sentences), chunk_size):
        yield ' '.join(sentences[i:i + chunk_size])

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

        # Process chunks of text
        for chunk in chunk_text(text):
            sentences = sent_tokenize(chunk)
            relatedness = calculate_word_relatedness(sentences)
            word_freqs = calculate_word_frequencies(preprocess_text(chunk))

            # Export data to CSV
            export_word_frequencies_to_csv(word_freqs)
            export_graph_data_to_csv(relatedness)

            # Generate word cloud and save as SVG
            wordcloud_file = 'wordcloud.svg'
            visualize_wordcloud(word_freqs, output_file=wordcloud_file)
            svg_files.append(wordcloud_file)

            # Generate and save word graphs
            word_graph_file = 'word_graph.svg'
            visualize_word_graph(relatedness, word_freqs, output_file=word_graph_file)
            svg_files.append(word_graph_file)

        print("Analysis complete.")
        return svg_files

    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")
        print(f"An error occurred during analysis: {e}")

# GUI for file selection
def select_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
    return file_path

if __name__ == '__main__':
    file_path = select_file()
    if file_path:
        try:
            if file_path.lower().endswith('.pdf'):
                generate_text_dump_from_pdf(file_path)
                text = read_text_from_file(file_path.replace('.pdf', '_dump.txt'))
            else:
                text = read_text_from_file(file_path)

            if text:
                analyze_text(text, file_path if file_path.lower().endswith('.pdf') else None)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")
