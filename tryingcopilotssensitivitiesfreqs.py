import nltk
from nltk.corpus import wordnet as wn
import pandas as pd
from textblob import TextBlob
from collections import defaultdict, Counter
import re
import logging

# Download necessary NLTK data
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')

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

# Function to dump total concatenated text and return frequency of unique words
def dump_whole_dictionary_text(output_file, freq_output_file):
    whole_text = []
    columns_to_dump = ['Definition', 'Examples', 'Synonyms', 'Antonyms', 
                       'Hypernyms', 'Hyponyms', 'Meronyms', 
                       'Holonyms', 'Troponyms', 
                       'Derivationally Related Forms', 
                       'Lexical Relations']
    
    try:
        for synset in list(wn.all_synsets()):
            for lemma in synset.lemmas():
                try:
                    row_data = {
                        'Definition': synset.definition() if hasattr(synset, 'definition') else '',
                        'Examples': ' '.join(synset.examples()) if hasattr(synset, 'examples') else '',
                        'Synonyms': ' '.join([l.name() for l in synset.lemmas()]) if hasattr(synset, 'lemmas') else '',
                        'Antonyms': ' '.join([ant.name() for ant in lemma.antonyms()]) if hasattr(lemma, 'antonyms') else '',
                        'Hypernyms': ' '.join([h.name() for h in synset.hypernyms()]) if hasattr(synset, 'hypernyms') else '',
                        'Hyponyms': ' '.join([h.name() for h in synset.hyponyms()]) if hasattr(synset, 'hyponyms') else '',
                        'Meronyms': ' '.join([m.name() for m in synset.part_meronyms()]) if hasattr(synset, 'part_meronyms') else '',
                        'Holonyms': ' '.join([h.name() for h in synset.part_holonyms()]) if hasattr(synset, 'part_holonyms') else '',
                        'Troponyms': ' '.join([t.name() for t in synset.troponyms()]) if hasattr(synset, 'troponyms') else '',
                        'Derivationally Related Forms': ' '.join([d.name() for d in lemma.derivationally_related_forms()]) if hasattr(lemma, 'derivationally_related_forms') else '',
                        'Lexical Relations': ' '.join([l.name() for l in synset.lemmas()]) if hasattr(synset, 'lemmas') else ''
                    }

                    # Append all text to whole_text
                    for column in columns_to_dump:
                        whole_text.append(row_data[column])

                except Exception as e:
                    logging.error(f"Error processing synset {synset.name()} and lemma {lemma.name()}: {e}")
                    continue

        # Preprocess and tokenize
        whole_text_str = " ".join(whole_text)
        lemmatizer = nltk.WordNetLemmatizer()
        words = nltk.word_tokenize(whole_text_str)
        words = [lemmatizer.lemmatize(word.lower()) for word in words if word.isalpha()]
        words.sort(key=len)
        word_freq = Counter(words)
    except Exception as e:
        logging.error(f"Unexpected error in preprocessing: {e}")
        raise

    # Sort the word frequencies in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Write the cleaned text to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(whole_text_str)

    # Prepare data for the frequency output file and Excel file
    data = []
    for word, freq in sorted_word_freq:
        pos_counts, sensitivity_sum, max_sensitivity, min_sensitivity, average_sensitivity = count_pos_in_tokens_deeper_on_categories([word], ancientness_sensitivity_values)
        pos_tags = ", ".join(pos_counts.keys())
        category_descriptions = ", ".join(f"{cat}: {count}" for cat, count in pos_counts.items())
###        sensitivity_sum_value = sum(sensitivity
		
		
        sensitivity_sum_value = sum(sensitivity_sum.values())
        freq_sensitivity_sum = freq * sensitivity_sum_value
        freq_sensitivity_max = freq * max(max_sensitivity.values(), default=0)
        freq_sensitivity_min = freq * min(min_sensitivity.values(), default=0)
        if average_sensitivity:
            avg_sens_value = sum(average_sensitivity.values()) / len(average_sensitivity)
            freq_sensitivity_avgs = freq * avg_sens_value
        else:
            freq_sensitivity_avgs = 0
        # Calculate sentiment values
        sentiment = TextBlob(word).sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
        data.append([word, freq, pos_tags, category_descriptions, sensitivity_sum_value,
                     max(max_sensitivity.values(), default=0), min(min_sensitivity.values(), default=0),
                     sum(average_sensitivity.values()) / len(average_sensitivity) if average_sensitivity else 0,
                     freq_sensitivity_max, freq_sensitivity_min, freq_sensitivity_avgs, freq_sensitivity_sum,
                     polarity, subjectivity])

    # Write the word frequencies to the frequency output file with additional columns
    with open(freq_output_file, "w", encoding="utf-8") as f:
        f.write("WordToken###Frequency###POS###CategoryDescription###SensitivitySum###MaxSensitivity###MinSensitivity###AverageSensitivity###Frequency*SensitivitySum###Frequency*MaxSensitivity###Frequency*MinSensitivity###Frequency*AverageSensitivity###Polarity###Subjectivity\n")
        for row in data:
            f.write("###".join(map(str, row)) + "\n")

    # Create a DataFrame and save it to an Excel file
    df = pd.DataFrame(data, columns=["WordToken", "Frequency", "POS", "CategoryDescription", "SensitivitySum",
                                     "MaxSensitivity", "MinSensitivity", "AverageSensitivity", "Frequency*SensitivitySum",
                                     "Frequency*MaxSensitivity", "Frequency*MinSensitivity", "Frequency*AverageSensitivity",
                                     "Polarity", "Subjectivity"])
    excel_output_file = f"copilots_sentimentsalsominsmaxesavgssumssensitivitiesdumpsfreqs{len(word_freq)}_words.xlsx"
    df.to_excel(excel_output_file, index=False)
    return word_freq

# Main function to run independently
def main():
    output_file = "copilots_sentimentsalsominsmaxesavgssumssensitivities.txt"
    freq_output_file = "copilots_sentimentsalsominsmaxesavgssumssensitivitiesdumpsfreqs.txt"

    try:
        word_frequency = dump_whole_dictionary_text(output_file, freq_output_file)
        print(f"Processed data has been saved to {output_file} and {freq_output_file}.")
    except Exception as e:
        logging.error(f"Error during processing: {e}")
        print("An error occurred during the process. Check the log file for details.")

if __name__ == "__main__":
    main()		