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

# # # # Ancientness sensitivity values (adjusted weights)
# # # ancientness_sensitivity_values = {
    # # # 'Adj all': 100, 'Adj pert': 150, 'Adj ppl': 200, 'Adv all': 100,
    # # # 'Noun act': 500, 'Noun animal': 1000, 'Noun artifact': 800,
    # # # # Add remaining POS categories and weights...
# # # }
# Define ancientness sensitivity values (adjusted for hunter-gatherer society)
ancientness_sensitivity_values = {
    'Adj all': 100, 'Adj pert': 150, 'Adj ppl': 200, 'Adv all': 100,
    'Noun act': 500, 'Noun animal': 1000, 'Noun artifact': 800, 'Noun attribute': 200,
    'Noun body': 300, 'Noun cognition': 100, 'Noun communication': 150, 'Noun event': 90,
    'Noun feeling': 60, 'Noun food': 1200, 'Noun group': 350, 'Noun location': 400,
    'Noun motive': 200, 'Noun object': 150, 'Noun person': 100, 'Noun phenomenon': 100,
    'Noun plant': 900, 'Noun possession': 75, 'Noun process': 150, 'Noun quantity': 80,
    'Noun relation': 120, 'Noun shape': 70, 'Noun state': 60, 'Noun substance': 90,
    'Noun time': 400, 'Noun tops': 110,
    'Verb body': 700, 'Verb change': 650, 'Verb cognition': 300, 'Verb communication': 500,
    'Verb competition': 400, 'Verb consumption': 500, 'Verb contact': 350, 'Verb creation': 300,
    'Verb emotion': 250, 'Verb motion': 200, 'Verb perception': 150, 'Verb possession': 120,
    'Verb social': 150, 'Verb stative': 100, 'Verb weather': 450
}

# Calculate sentiment
def calculate_sentiment(text):
    try:
        blob = TextBlob(text)
        return blob.sentiment.polarity
    except Exception as e:
        logging.error(f"Error calculating sentiment for text: {text}. Error: {e}")
        return 0

# Preprocess text and calculate word frequencies
def preprocess_and_calculate_frequencies():
    whole_text = []
    for synset in wn.all_synsets():
        try:
            whole_text.append(synset.definition())
            whole_text.extend(synset.examples())
            whole_text.extend([lemma.name() for lemma in synset.lemmas()])
        except Exception as e:
            logging.error(f"Error processing synset {synset.name()}: {e}")
    full_text = " ".join(whole_text)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(full_text) if word.isalpha()]
    return Counter(words)

# Count POS and calculate sensitivity
def count_pos_and_sensitivity(tokens):
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    tagged_tokens = nltk.pos_tag(tokens)

    sensitivity_sum = defaultdict(int)
    # # # pos_map = {
        # # # "Adj all": ["JJ", "JJR", "JJS"],
        # # # "Noun act": ["NN", "NNS"],
        # # # # Add mappings for other POS categories...
    # # # }
	
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
                freq_sensitivity = row_frequency * sum(sensitivity_sum.values())
                row = {
                    'Synset ID': synset.name(),
                    'Word': lemma.name(),
                    'Part of Speech': synset.pos(),
                    'Definition': synset.definition(),
                    'Examples': ", ".join(synset.examples()),
                    'Frequency': row_frequency,
                    'SensitivitySum': sum(sensitivity_sum.values()),
                    'Freq * Sensitivity': freq_sensitivity,
                    'Text': f"   {freq_sensitivity}"  # Text column to avoid Excel scientific notation
                }
                data.append(row)
            except Exception as e:
                logging.error(f"Error processing synset {synset.name()} and lemma {lemma.name()}: {e}")
    df = pd.DataFrame(data)
    return df.sort_values(by=['Freq * Sensitivity'], ascending=False)

# Main execution
def main():
    try:
        word_frequencies = preprocess_and_calculate_frequencies()
        wordnet_data = collect_wordnet_data(word_frequencies)
        wordnet_data.to_excel(
            "withadditionaltextcolshuntergatherers_sorted_wordnet_data.xlsx", index=False, engine='openpyxl'
        )
        print("Data exported successfully.")
    except Exception as e:
        logging.error(f"Execution error: {e}")
        print("Error occurred. Check log for details.")

if __name__ == "__main__":
    main()