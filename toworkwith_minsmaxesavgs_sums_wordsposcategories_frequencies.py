import nltk
from collections import defaultdict, Counter
import re
import pandas as pd
from nltk.corpus import wordnet as wn

# Download the WordNet data
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Define sensitivity values for different POS categories
sensitivity_values = {
    'Adj all': 1, 'Adj pert': 2, 'Adj ppl': 3, 'Adv all': 4,
    'Noun act': 5, 'Noun animal': 6, 'Noun artifact': 7, 'Noun attribute': 8,
    'Noun body': 9, 'Noun cognition': 10, 'Noun communication': 11, 'Noun event': 12,
    'Noun feeling': 13, 'Noun food': 14, 'Noun group': 15, 'Noun location': 16,
    'Noun motive': 17, 'Noun object': 18, 'Noun person': 19, 'Noun phenomenon': 20,
    'Noun plant': 21, 'Noun possession': 22, 'Noun process': 23, 'Noun quantity': 24,
    'Noun relation': 25, 'Noun shape': 26, 'Noun state': 27, 'Noun substance': 28,
    'Noun time': 29, 'Noun tops': 30,
    'Verb body': 31, 'Verb change': 32, 'Verb cognition': 33, 'Verb communication': 34,
    'Verb competition': 35, 'Verb consumption': 36, 'Verb contact': 37, 'Verb creation': 38,
    'Verb emotion': 39, 'Verb motion': 40, 'Verb perception': 41, 'Verb possession': 42,
    'Verb social': 43, 'Verb stative': 44, 'Verb weather': 45
}

def count_pos_in_tokens_deeper_on_categories(tokens, sensitivity_values):
    """
    Counts the number of tokens belonging to each part of speech and calculates the summation, 
    maximum, minimum, and average of sensitivity values for all tokens.
    """
    lemmatizer = nltk.WordNetLemmatizer()
    
    # Lemmatize, stem, and lowercase tokens
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
        "Noun quantity": ["NN", "NNS"],
        "Noun relation": ["NN", "NNS"],
        "Noun shape": ["NN", "NNS"],
        "Noun state": ["NN", "NNS"],
        "Noun substance": ["NN", "NNS"],
        "Noun time": ["NN", "NNS"],
        "Noun tops": ["NN", "NNS"],
        "Verb body": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb change": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb cognition": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb communication": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb competition": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb consumption": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb contact": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb creation": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb emotion": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb motion": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb perception": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb possession": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb social": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb stative": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "Verb weather": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
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
    words = set(wn.words())
    
    for word in words:
        synsets = wn.synsets(word)
        for synset in synsets:
            whole_text.append(word)
            whole_text.append(synset.definition())
            whole_text.extend(synset.examples())
            whole_text.extend(lemma.name() for lemma in synset.lemmas())
    
    # Join the whole text into a single string
    whole_text_str = " ".join(whole_text)
    
    # Replace all special characters, underscores, and non-alphabet characters with new lines
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '\n', whole_text_str)
    
    # Split the cleaned text into words
    split_words = cleaned_text.split()
    
    # Calculate the frequency of unique words
    word_freq = Counter(split_words)
    
    # Sort the word frequencies in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Write the cleaned text to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cleaned_text)
    
    # Prepare data for the frequency output file and Excel file
    data = []
    
    for word, freq in sorted_word_freq:
        pos_counts, sensitivity_sum, max_sensitivity, min_sensitivity, average_sensitivity = count_pos_in_tokens_deeper_on_categories([word], {})
        
        pos_tags = ", ".join(pos_counts.keys())
        category_descriptions = ", ".join(f"{cat}: {count}" for cat, count in pos_counts.items())
        
        sensitivity_sum_value = sum(sensitivity_sum.values())
        
        freq_sensitivity_sum = freq * sensitivity_sum_value
        
        data.append([word, freq, pos_tags, category_descriptions, sensitivity_sum_value,
                     max(max_sensitivity.values(), default=0), min(min_sensitivity.values(), default=0),
                     sum(average_sensitivity.values()) / len(average_sensitivity) if average_sensitivity else 0,
                     freq_sensitivity_sum])
    
    # Write the word frequencies to the frequency output file with additional columns
    with open(freq_output_file, "w", encoding="utf-8") as f:
        f.write("WordToken###Frequency###POS###CategoryDescription###SensitivitySum###MaxSensitivity###MinSensitivity###AverageSensitivity###Frequency*SensitivitySum\n")
        
        for row in data:
            f.write("###".join(map(str, row)) + "\n")
    
    # Create a DataFrame and save it to an Excel file
    df = pd.DataFrame(data, columns=["WordToken","Frequency","POS","CategoryDescription","SensitivitySum",
                                     'MaxSensitivity','MinSensitivity','AverageSensitivity',"Frequency*SensitivitySum"])
    
    excel_output_file = f"minsmaxesavgssumssensitivities_onlemmatizedstemmedtokens_word_frequencies_{len(split_words)}_words.xlsx"
    
    df.to_excel(excel_output_file, index=False)
    
    return word_freq

# Main function to run independently
def main():
    output_file = "minsmaxesavgssumssensitivities_lemmatizedstemmedlowercaseswithmoredetailedsensitivitysindependentlygenerated_dumps_whole_dictionary_text_cleaned.txt"
    freq_output_file = "minsmaxesavgssumssensitivities_lemmatizedstemmedlowercaseswithmoredetailedsensitivitysdumpfile_for_word_frequencies_on_whole_wordnet.txt"
    
    word_frequency = dump_whole_dictionary_text(output_file, freq_output_file)
    
    # Print the frequency of unique words
    print(word_frequency)

if __name__ == "__main__":
    main()