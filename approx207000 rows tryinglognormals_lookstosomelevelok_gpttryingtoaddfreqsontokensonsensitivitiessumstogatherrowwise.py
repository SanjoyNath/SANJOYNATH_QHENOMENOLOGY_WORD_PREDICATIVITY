import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
from textblob import TextBlob
from collections import defaultdict, Counter
import logging

# Download necessary NLTK data
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')
nltk.download('punkt')

# Configure logging
logging.basicConfig(filename="wordnet_export.log", level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Define ancientness sensitivity values
ancientness_sensitivity_values = {
    'Adj all': 600, 'Adj pert': 550, 'Adj ppl': 500, 'Adv all': 450,
    'Noun act': 400, 'Noun animal': 350, 'Noun artifact': 300, 'Noun attribute': 250,
    'Noun body': 200, 'Noun cognition': 150, 'Noun communication': 100, 'Noun event': 90,
    'Noun feeling': 80, 'Noun food': 250, 'Noun group': 150, 'Noun location': 120,
    'Noun motive': 130, 'Noun object': 120, 'Noun person': 100, 'Noun phenomenon': 90,
    'Noun plant': 80, 'Noun possession': 75, 'Noun process': 70, 'Noun quantity': 60,
    'Noun relation': 100, 'Noun shape': 60, 'Noun state': 50, 'Noun substance': 80,
    'Noun time': 150, 'Noun tops': 100,
    'Verb body': 600, 'Verb change': 550, 'Verb cognition': 500, 'Verb communication': 450,
    'Verb competition': 400, 'Verb consumption': 350, 'Verb contact': 300, 'Verb creation': 250,
    'Verb emotion': 200, 'Verb motion': 150, 'Verb perception': 100, 'Verb possession': 90,
    'Verb social': 80, 'Verb stative': 70, 'Verb weather': 60
}

# Function to calculate sentiment
def calculate_sentiment(text):
    try:
        blob = TextBlob(text)
        return blob.sentiment.polarity
    except Exception as e:
        logging.error(f"Error calculating sentiment for text: {text}. Error: {e}")
        return 0

# Preprocess text and calculate frequencies
def preprocess_and_calculate_frequencies():
    whole_text = []
    for synset in wn.all_synsets():
        for lemma in synset.lemmas():
            try:
                whole_text.append(lemma.name())
                whole_text.append(synset.definition())
                whole_text.extend(synset.examples())
                whole_text.extend([l.name() for l in synset.lemmas()])
            except Exception as e:
                logging.error(f"Error processing synset {synset.name()} and lemma {lemma.name()}: {e}")
    full_text = " ".join(whole_text)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(full_text) if word.isalpha()]
    return Counter(words)

# Calculate POS and sensitivity
def count_pos_and_sensitivity(tokens):
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    tagged_tokens = nltk.pos_tag(tokens)
    pos_map = {
        "Adj all": ["JJ", "JJR", "JJS"],
        "Adv all": ["RB", "RBR", "RBS"],
        "Noun act": ["NN", "NNS", "NNP", "NNPS"],
        "Verb change": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
    }
    sensitivity_sum = defaultdict(int)
    for token, tag in tagged_tokens:
        for pos_category, tags in pos_map.items():
            if tag in tags:
                sensitivity_sum[pos_category] += ancientness_sensitivity_values.get(pos_category, 0)
    return sensitivity_sum

# Collect WordNet data
def collect_wordnet_data(word_freq):
    data = []
    for synset in wn.all_synsets():
        for lemma in synset.lemmas():
            try:
                row_text = f"{synset.definition()} {' '.join(synset.examples())} {' '.join([l.name() for l in synset.lemmas()])}"
                tokens = word_tokenize(row_text)
                sensitivity_sum = count_pos_and_sensitivity(tokens)
                row_frequency = sum(word_freq.get(token.lower(), 0) for token in tokens)
                row = {
                    'Synset ID': synset.name(),
                    'Word': lemma.name(),
                    'Part of Speech': synset.pos(),
                    'Definition': synset.definition(),
                    'Examples': ", ".join(synset.examples()),
                    'Frequency': row_frequency,
                    'SensitivitySum': sum(sensitivity_sum.values()),
                }
                data.append(row)
            except Exception as e:
                logging.error(f"Error processing synset {synset.name()} and lemma {lemma.name()}: {e}")
    return pd.DataFrame(data)

# Main execution
def main():
    try:
        word_frequencies = preprocess_and_calculate_frequencies()
        wordnet_data = collect_wordnet_data(word_frequencies)
        wordnet_data.to_excel("gptfreshtryingenhanced_wordnet_data.xlsx", index=False, engine='openpyxl')
        print("Data exported successfully.")
    except Exception as e:
        logging.error(f"Execution error: {e}")
        print("Error occurred. Check log for details.")

if __name__ == "__main__":
    main()