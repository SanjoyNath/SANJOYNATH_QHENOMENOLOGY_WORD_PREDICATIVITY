import nltk
from nltk.corpus import wordnet as wn
from collections import Counter

def generate_wordnet_report(output_file):
    """
    Generate a human-readable WordNet dictionary and save it to a text file.
    """
    # Open the output file for writing
    with open(output_file, "w", encoding="utf-8") as f:
        # Write column headers
        f.write("###Word###Row Number###Unique Word Counter###Same Word Different Meaning Counter"
                "###Meaning###Category###Category Description###Part of Speech###Word Count###Word Count Percentile###Token Sum###Token Sum Percentile\n")
        
        # Initialize unique word counter
        unique_word_counter = 0
        row_number = 0

        # Get all words in WordNet (lemmas)
        lemmas = [lemma.name() for synset in wn.all_synsets() for lemma in synset.lemmas()]
        words = sorted(set(lemmas))
        
        # Count occurrences of each word in the dictionary
        word_count = Counter(lemmas)
        max_word_count = max(word_count.values())  # Max frequency for percentile calculation
        
        # Sum of all token frequencies
        total_token_count = sum(word_count.values())

        for word in words:
            unique_word_counter += 1
            # Get all synsets (meanings) for the word
            synsets = wn.synsets(word)
            
            for meaning_counter, synset in enumerate(synsets, start=1):
                # Extract WordNet category and description
                category = synset.lexname()
                category_description = synset.lexname().replace('.', ' ').capitalize()
                part_of_speech = synset.pos()

                # Map part of speech to human-readable format
                pos_mapping = {
                    "n": "Noun",
                    "v": "Verb",
                    "a": "Adjective",
                    "s": "Adjective Satellite",
                    "r": "Adverb",
                }
                human_readable_pos = pos_mapping.get(part_of_speech, "Unknown")

                # Get the word count
                count = word_count[word]

                # Calculate word count percentile
                word_count_percentile = (count / max_word_count) * 100

                # Token sum: Total occurrences of all words in the current row (same word across meanings)
                token_sum = sum(word_count[lemma.name()] for lemma in synset.lemmas())
                
                # Token sum percentile
                token_sum_percentile = (token_sum / total_token_count) * 100

                # Write row to the file
                row_number += 1
                f.write(f"###{word}###{row_number}###{unique_word_counter}###{meaning_counter}###"
                        f"{synset.definition()}###{category}###{category_description}###{human_readable_pos}###{count}###"
                        f"{word_count_percentile:.2f}###"
                        f"{token_sum}###"
                        f"{token_sum_percentile:.2f}\n")

if __name__ == "__main__":
    # Generate the WordNet report and save it
    output_file = "wordnet_dictionary_with_counts_and_percentiles_report.txt"
    generate_wordnet_report(output_file)
    print(f"Report generated successfully and saved to {output_file}")
