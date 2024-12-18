import logging
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from collections import Counter, defaultdict
from nltk import pos_tag, word_tokenize, sent_tokenize
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

# Configure logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

def get_wordnet_pos(treebank_tag):
    """ Convert POS tag to WordNet format """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN

def preprocess_text(text):
    """ Tokenize, lemmatize, and remove stopwords and punctuation from text """
    words = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(word) for word in words if word not in stop_words and word not in string.punctuation]

def calculate_word_frequencies(words):
    """ Calculate word frequencies from a list of words """
    return Counter(words)

def split_sentences_with_word_count(text):
    """ Split text into sentences and count words in each sentence """
    sentences = sent_tokenize(text)
    return [(sentence, len(word_tokenize(sentence))) for sentence in sentences]

def calculate_window_sizes(sentences):
    """ Calculate window sizes for each sentence """
    sentence_data = split_sentences_with_word_count(sentences)
    window_sizes = []
    
    for i, (sentence, current_count) in enumerate(sentence_data):
        prev_count = sentence_data[i - 1][1] if i > 0 else 0
        next_count = sentence_data[i + 1][1] if i < len(sentence_data) - 1 else 0
        
        backward_window = prev_count + current_count
        forward_window = current_count + next_count
        window_sizes.append((sentence, backward_window, forward_window))
    
    return window_sizes

def calculate_word_relatedness(text):
    """ Calculate word relatedness using custom window sizes """
    sentences_with_window_sizes = calculate_window_sizes(text)
    relatedness = defaultdict(Counter)
    
    for i, (sentence, back_size, forward_size) in enumerate(sentences_with_window_sizes):
        words = preprocess_text(sentence)
        all_window_words = []

        if i > 0:
            back_words = preprocess_text(sentences_with_window_sizes[i - 1][0])
            all_window_words.extend(back_words[:back_size])
        if i < len(sentences_with_window_sizes) - 1:
            forward_words = preprocess_text(sentences_with_window_sizes[i + 1][0])
            all_window_words.extend(forward_words[:forward_size])

        for word1 in words:
            for word2 in all_window_words:
                if word1 != word2:
                    relatedness[word1][word2] += 1

    return relatedness

def visualize_wordcloud(word_freqs, output_file='wordcloud.svg', title='Word Cloud'):
    """ Generate and save a word cloud visualization """
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_freqs)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(title, fontsize=16)
    plt.savefig(output_file, format="svg")
    plt.close()

def export_graph_data_to_csv(relatedness, filename='word_relatedness.csv'):
    """ Export word relatedness data to CSV """
    rows = [[word1, word2, weight] for word1, connections in relatedness.items() for word2, weight in connections.items()]
    pd.DataFrame(rows, columns=['Word1', 'Word2', 'Weight']).to_csv(filename, index=False)

def visualize_word_graph(relatedness, word_freqs, output_file='word_graph.svg'):
    """ Visualize word relatedness as a graph """
    G = nx.Graph()
    for word1, connections in relatedness.items():
        for word2, weight in connections.items():
            if word1 != word2 and weight > 1:
                G.add_edge(word1, word2, weight=weight)

    pos = nx.spring_layout(G)
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

def export_word_frequencies_to_csv(word_freqs, filename='word_frequencies.csv'):
    """ Export word frequencies to CSV """
    pd.DataFrame.from_dict(word_freqs, orient='index', columns=['Frequency']).sort_values(by='Frequency', ascending=False).to_csv(filename)

def generate_text_from_pdf(pdf_path):
    """ Extract text from a PDF file """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except Exception as e:
        logging.error(f"Error extracting text from PDF: {e}")
    return text

def read_text_from_file(file_path):
    """ Read text from a text file """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def analyze_text(text):
    """ Analyze text and generate visualizations """
    try:
        words = preprocess_text(text)
        word_freqs = calculate_word_frequencies(words)
        relatedness = calculate_word_relatedness(text)

        export_word_frequencies_to_csv(word_freqs)
        export_graph_data_to_csv(relatedness)

        visualize_wordcloud(word_freqs)
        visualize_word_graph(relatedness)

        print("Analysis completed and files generated.")
    except Exception as e:
        logging.error(f"An error occurred during text analysis: {e}")

def main():
    """ Main function to handle file dialog and processing """
    Tk().withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf"), ("Text files", "*.txt")],
        title="Select a file"
    )

    if file_path:
        if file_path.lower().endswith('.pdf'):
            text = generate_text_from_pdf(file_path)
        elif file_path.lower().endswith('.txt'):
            text = read_text_from_file(file_path)
        else:
            print("Unsupported file type selected.")
            return

        if text:
            analyze_text(text)

if __name__ == '__main__':
    main()
