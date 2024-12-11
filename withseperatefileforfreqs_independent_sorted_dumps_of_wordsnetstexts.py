from nltk.corpus import wordnet as wn
from collections import Counter
import re
import nltk

# Download the WordNet data
nltk.download('wordnet')

# Function to dump total concatenated text, replace special characters, and return frequency of unique words
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
    
    # Write the word frequencies to the frequency output file
    with open(freq_output_file, "w", encoding="utf-8") as f:
        for word, freq in sorted_word_freq:
            f.write(f"{word}###{freq}\n")
    
    return word_freq

# Main function to run independently
def main():
    output_file = "independentlygenerated_dumps_whole_dictionary_text_cleaned.txt"
    freq_output_file = "dumpfile_for_word_frequencies_on_whole_wordnet.txt"
    word_frequency = dump_whole_dictionary_text(output_file, freq_output_file)
    
    # Print the frequency of unique words
    print(word_frequency)

if __name__ == "__main__":
    main()