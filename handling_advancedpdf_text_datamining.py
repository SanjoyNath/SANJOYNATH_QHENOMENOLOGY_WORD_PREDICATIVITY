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
import logging  # Import for logging errors
from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer for stemming
stemmer = PorterStemmer()
# Initialize NLP tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
# Set up logging to log errors to a file named 'error.log'
logging.basicConfig(filename='error.log', level=logging.ERROR)


from PyPDF2 import PdfReader

def generate_text_dump_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        logging.error(f"Error reading PDF file: {e}")
        return ""
		
		
		

# Generate pivot report for noun-to-noun relatedness
def generate_noun_to_noun_pivot_report(pos_tagged_words, relatedness, filename='noun_to_noun_pivot_report.csv'):
    noun_to_noun_data = defaultdict(Counter)
    for (word1, pos1), (word2, pos2) in zip(pos_tagged_words, pos_tagged_words[1:]):
        if pos1.startswith('NN') and pos2.startswith('NN'):  # Check for noun-to-noun relatedness
            noun_to_noun_data[word1][word2] += relatedness[word1].get(word2, 0)
    # Prepare data for the CSV file
    rows = []
    for noun1, connections in noun_to_noun_data.items():
        for noun2, weight in connections.items():
            rows.append([noun1, noun2, weight])
    # Save noun-to-noun pivot report as CSV
    pd.DataFrame(rows, columns=['Noun1', 'Noun2', 'Weight']).to_csv(filename, index=False)

# Generate pivot report for noun-to-verb relatedness
def generate_noun_to_verb_pivot_report(pos_tagged_words, relatedness, filename='noun_to_verb_pivot_report.csv'):
    noun_to_verb_data = defaultdict(Counter)
    for (word1, pos1), (word2, pos2) in zip(pos_tagged_words, pos_tagged_words[1:]):
        if pos1.startswith('NN') and pos2.startswith('VB'):  # Check for noun-to-verb relatedness
            noun_to_verb_data[word1][word2] += relatedness[word1].get(word2, 0)
    # Prepare data for the CSV file
    rows = []
    for noun, verbs in noun_to_verb_data.items():
        for verb, weight in verbs.items():
            rows.append([noun, verb, weight])
    # Save noun-to-verb pivot report as CSV
    pd.DataFrame(rows, columns=['Noun', 'Verb', 'Weight']).to_csv(filename, index=False)

# Preprocess the text: tokenize, stem, lemmatize, and remove stopwords/punctuation
def preprocess_text_with_stemming(text):
    if text is None:
        return [], []
    words = word_tokenize(text.lower())
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words and word not in string.punctuation]
    stemmed_words = [stemmer.stem(word) for word in words if word not in stop_words and word not in string.punctuation]
    return lemmatized_words, stemmed_words

# Calculate stemming frequencies
def calculate_stem_frequencies(words):
    return Counter(words)

# Helper function to convert POS tag to WordNet format
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN  # Default to noun

# Preprocess the text: tokenize, lemmatize, and remove stopwords/punctuation
def preprocess_text(text):
    if text is None:
        return []
    words = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(word) for word in words if word not in stop_words and word not in string.punctuation]

# Calculate word frequencies
def calculate_word_frequencies(words):
    return Counter(words)

# Calculate n-grams frequencies
def calculate_ngrams(words, n=3):
    return Counter(ngrams(words, n))

# Calculate word relatedness (co-occurrence) within a sliding window
def calculate_word_relatedness(words, window_size=30):
    relatedness = defaultdict(Counter)
    for i, word1 in enumerate(words):
        for word2 in words[i+1:i+window_size]:
            if word1 != word2:
                relatedness[word1][word2] += 1
    return relatedness

# Generate and save a word cloud as an SVG
def visualize_wordcloud(word_freqs, output_file='wordcloud.svg', title='Word Cloud'):
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_freqs)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(title, fontsize=16)
    plt.savefig(output_file, format="svg")
    plt.close()

# Export word relatedness data to a CSV file
def export_graph_data_to_csv(relatedness, filename='word_relatedness.csv'):
    rows = [[word1, word2, weight] for word1, connections in relatedness.items() for word2, weight in connections.items()]
    pd.DataFrame(rows, columns=['Word1', 'Word2', 'Weight']).to_csv(filename, index=False)

# Export POS tagged frequencies to a CSV file
def export_pos_frequencies_to_csv(pos_tags, filename='pos_frequencies.csv'):
    pos_freqs = Counter(pos_tags)
    pd.DataFrame.from_dict(pos_freqs, orient='index', columns=['Frequency']).sort_values(by='Frequency', ascending=False).to_csv(filename)

# Visualize a word relatedness graph as an SVG
def visualize_word_graph(relatedness, word_freqs, output_file='word_graph.svg'):
    G = nx.Graph()
    for word1, connections in relatedness.items():
        for word2, weight in connections.items():
            if word1 != word2 and weight > 1:
                G.add_edge(word1, word2, weight=weight)
    pos = nx.circular_layout(G)
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

# Export phrase and POS tag relationships to CSV
def export_phrase_pos_relationships_to_csv(phrases, pos_tags, filename='phrase_pos_relationships.csv'):
    data = []
    phrase_pos_pairs = list(zip(phrases, pos_tags))
    phrase_pos_counter = Counter(phrase_pos_pairs)
    for (phrase, pos_tag), frequency in phrase_pos_counter.items():
        data.append([phrase, pos_tag, frequency])
    pd.DataFrame(data, columns=['Phrase', 'POS Tag', 'Frequency']).to_csv(filename, index=False)

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

# # # # Generate pivot report with word and phrase breakups by POS tags
# # # def generate_pivot_report(pos_tagged_words, pos_tagged_phrases)
# Generate pivot report with word and phrase breakups by POS tags
def generate_pivot_report(pos_tagged_words, pos_tagged_phrases, filename='pivot_report.csv'):
    pivot_data = defaultdict(lambda: {'Words': [], 'Phrases': [], 'Word Count': 0, 'Phrase Count': 0})
    
    # Separate words and phrases by their POS tags
    for word, pos in pos_tagged_words:
        pivot_data[pos]['Words'].append(word)
        pivot_data[pos]['Word Count'] += 1
    for phrase, pos in pos_tagged_phrases:
        pivot_data[pos]['Phrases'].append(phrase)
        pivot_data[pos]['Phrase Count'] += 1
    
    # Prepare data for the CSV file
    pivot_rows = []
    for pos, data in pivot_data.items():
        pivot_rows.append({
            'POS Tag': pos,
            'Words': ', '.join(data['Words'][:10]),  # Limit to 10 words for readability
            'Phrases': ', '.join(data['Phrases'][:10]),  # Limit to 10 phrases for readability
            'Word Count': data['Word Count'],
            'Phrase Count': data['Phrase Count']
        })
    
    # Save pivot report as CSV
    pd.DataFrame(pivot_rows).to_csv(filename, index=False)

# Analyze text and create visual outputs
def analyze_text(text, pdf_path=None):
    if not text:
        logging.warning("No text to analyze.")
        print("No text to analyze.")
        return
    
    try:
        all_words = []
        all_pos_tags = []
        pos_tagged_words = []
        
        for chunk in chunk_text(text):
            words, _ = preprocess_text_with_stemming(chunk)
            pos_tags = pos_tag(words)
            all_words.extend(words)
            all_pos_tags.extend([tag for _, tag in pos_tags])
            pos_tagged_words.extend(pos_tags)
        
        relatedness = calculate_word_relatedness(all_words, window_size=60)
        export_graph_data_to_csv(relatedness)
        export_pos_frequencies_to_csv(all_pos_tags)
        
        # Generate separate noun-to-noun and noun-to-verb reports
        generate_noun_to_noun_pivot_report(pos_tagged_words, relatedness)
        generate_noun_to_verb_pivot_report(pos_tagged_words, relatedness)
        
        # Create visualizations and generate general pivot report
        visualize_word_graph(relatedness, calculate_word_frequencies(all_words))
        generate_pivot_report(pos_tagged_words, [])
        
        if pdf_path:
            convert_svg_to_pdf('wordcloud.svg', pdf_path)
    
    except Exception as e:
        logging.error(f"Error during text analysis: {e}")
        print("An error occurred during text analysis.")

# Main program function to load and analyze a text file
def main():
    root = Tk()
    root.withdraw()
    
    try:
        # Prompt user to select a text file
        file_path = filedialog.askopenfilename(title="Select Text File",
                                               filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
        if not file_path:
            print("No file selected. Exiting.")
            return
        
        if file_path.endswith('.pdf'):
            text = generate_text_dump_from_pdf(file_path)  # Now this will work
        else:
            text = read_text_from_file(file_path)
        
        analyze_text(text)
    
    except Exception as e:
        logging.error(f"Error in main program: {e}")
        print("An error occurred.")

if __name__ == "__main__":
    main()