import nltk
from nltk.corpus import wordnet as wn
import pandas as pd
from textblob import TextBlob
from collections import defaultdict, Counter
import logging
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

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
        return blob.sentiment.polarity  # Returns sentiment score
    except Exception as e:
        logging.error(f"Error calculating sentiment for text: {text}. Error: {e}")
        return 0  # Return 0 if sentiment calculation fails

# Preprocess text: Lowercase, Lemmatize, Stem, and calculate frequencies
def preprocess_and_calculate_frequencies():
    whole_text = []
    
    for synset in list(wn.all_synsets()):
        for lemma in synset.lemmas():
            try:
                # Prepare the synset row with the ancientness data
                whole_text.append(lemma.name())
                whole_text.append(synset.definition())
                whole_text.extend(synset.examples())
                whole_text.extend([l.name() for l in synset.lemmas()])
                
            except Exception as e:
                logging.error(f"Error processing synset {synset.name()} and lemma {lemma.name()}. Error: {e}")
                continue  # Continue processing other synsets if one fails

    # Combine all text into a single string
    whole_text_str = " ".join(whole_text)

    # Preprocess the text: lowercasing, lemmatization, and stemming
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(whole_text_str)
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word.isalpha()]

    # Sort words by length
    words.sort(key=len)

    # Count frequencies of substrings
    word_freq = Counter(words)
    return word_freq

def count_pos_in_tokens_deeper_on_categories(tokens, sensitivity_values):
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    tagged_tokens = nltk.pos_tag(tokens)

    pos_map = {
        "Adj all": ["JJ", "JJR", "JJS"],
        "Adj pert": ["JJ"],
        "Adj ppl": ["VBN", "VBG"],
        "Adv all": ["RB", "RBR", "RBS"],
        "Noun act": ["NN", "NNS", "NNP", "NNPS"],
        "Noun animal": ["NN", "NNS"],
        "Noun artifact": ["NN", "NNS"],
        "Noun attribute": ["NN", "NNS"],
        "Noun body": ["NN", "NNS"],
        "Noun cognition": ["NN", "NNS"],
        "Noun communication": ["NN", "NNS"],
        "Noun event": ["NN", "NNS"],
        "Noun feeling": ["NN", "NNS"],
        "Noun food": ["NN", "NNS"],
        "Noun group": ["NN", "NNS"],
        "Noun location": ["NN", "NNS"],
        "Noun motive": ["NN", "NNS"],
        "Noun object": ["NN", "NNS"],
        "Noun person": ["NN", "NNS"],
        "Noun phenomenon": ["NN", "NNS"],
        "Noun plant": ["NN", "NNS"],
        "Noun possession": ["NN", "NNS"],
        "Noun process": ["NN", "NNS"],
        "Noun quantity": ["NN", "NNS"]
    }

    pos_counts = defaultdict(int)
    sensitivity_sum = defaultdict(int)
    max_sensitivity = defaultdict(lambda: float('-inf'))
    min_sensitivity = defaultdict(lambda: float('inf'))
    sensitivity_values_list = defaultdict(list)

    for token, tag in tagged_tokens:
        for pos_category, tags in pos_map.items():
            if tag in tags:
                pos_counts[pos_category] += 1
                sensitivity_value = sensitivity_values.get(pos_category, 0)
                sensitivity_sum[pos_category] += sensitivity_value
                max_sensitivity[pos_category] = max(max_sensitivity[pos_category], sensitivity_value)
                min_sensitivity[pos_category] = min(min_sensitivity[pos_category], sensitivity_value)
                sensitivity_values_list[pos_category].append(sensitivity_value)

    average_sensitivity = {pos_category: (sum(values) / len(values) if values else 0)
                           for pos_category, values in sensitivity_values_list.items()}

    return pos_counts, sensitivity_sum, max_sensitivity, min_sensitivity, average_sensitivity

def collect_wordnet_data():
    columns = [
        'Synset ID', 'Word', 'Part of Speech', 'Definition', 'Examples',
        'Synonyms', 'Antonyms', 'Hypernyms', 'Hyponyms', 'Meronyms',
        'Holonyms', 'Troponyms', 'Derivationally Related Forms', 'Lexical Relations',
        'Word Frequency', 'Senses', 'Sentiment', 'SensitivitySum', 'MaxSensitivity', 'MinSensitivity', 'AverageSensitivity'
    ]
    
    word_freq = preprocess_and_calculate_frequencies()  # Calculate word frequencies

    data = []
    
    for synset in list(wn.all_synsets()):
        for lemma in synset.lemmas():
            try:
                # Check if Troponyms exist and handle missing attribute
                troponyms = ', '.join([t.name() for t in getattr(synset, 'troponyms', lambda: [])()])
                
                # Prepare the synset row with the ancientness data
                pos_counts, sensitivity_sum, max_sensitivity, min_sensitivity, average_sensitivity = count_pos_in_tokens_deeper_on_categories([lemma.name()], ancientness_sensitivity_values)
                
                word_frequency = word_freq.get(lemma.name(), 0)  # Get the word frequency
                
                row = {
                    'Synset ID': synset.name(),
                    'Word': lemma.name(),
                    'Part of Speech': synset.pos(),
                    'Definition': synset.definition(),
                    'Examples': ', '.join(synset.examples()),
                    'Synonyms': ', '.join([l.name() for l in synset.lemmas()]),
                    'Antonyms': ', '.join([ant.name() for ant in lemma.antonyms()]),
                    'Hypernyms': ', '.join([h.name() for h in synset.hypernyms()]),
                    'Hyponyms': ', '.join([h.name() for h in synset.hyponyms()]),
                    'Meronyms': ', '.join([m.name() for m in synset.part_meronyms()]),
                    'Holonyms': ', '.join([h.name() for h in synset.part_holonyms()]),
                    'Troponyms': troponyms,
                    'Derivationally Related Forms': ', '.join([d.name() for d in lemma.derivationally_related_forms()]),
                    'Lexical Relations': ', '.join([l.name() for l in synset.lemmas()]),
                    'Word Frequency': word_frequency,  # Word frequency from the calculated word frequencies
                    'Senses': len(synset.lemmas()),
                    'Sentiment': calculate_sentiment(synset.definition()),
                    'SensitivitySum': sum(sensitivity_sum.values()),
                    'MaxSensitivity': max(max_sensitivity.values(), default=0),
                    'MinSensitivity': min(min_sensitivity.values(), default=0),
                    'AverageSensitivity': sum(average_sensitivity.values()) / len(average_sensitivity) if average_sensitivity else 0
                }
                
                data.append(row)
            except Exception as e:
                logging.error(f"Error processing synset {synset.name()} and lemma {lemma.name()}. Error: {e}")
                continue  # Continue processing other synsets if one fails
    
    return pd.DataFrame(data, columns=columns)

def main():
    # Collect the data
    try:
        wordnet_df = collect_wordnet_data()
        # Export to Excel
        wordnet_df.to_excel('textdumpsfirstwordnet_data_with_sensitivity_and_frequency.xlsx', index=False, engine='openpyxl')
        print("WordNet data with sensitivity and word frequencies has been exported to 'wordnet_data_with_sensitivity_and_frequency.xlsx'.")
    except Exception as e:
        logging.error(f"Error during WordNet data collection or export: {e}")
        print("An error occurred during the process. Check the log file for details.")

if __name__ == "__main__":
    main()