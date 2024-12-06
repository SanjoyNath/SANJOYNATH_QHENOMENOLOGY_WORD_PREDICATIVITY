import nltk
from nltk.corpus import wordnet as wn

def generate_wordnet_report(output_file):
    """
    Generate a human-readable WordNet dictionary and save it to a text file.
    """
    # Open the output file for writing
    with open(output_file, "w", encoding="utf-8") as f:
        # Write column headers
        f.write("###Word###Row Number###Unique Word Counter###Same Word Different Meaning Counter"
                "###Meaning###Category###Category Description###Part of Speech\n")
        
        # Initialize unique word counter
        unique_word_counter = 0
        row_number = 0

        # Get all words in WordNet (lemmas)
        words = sorted(set(lemma.name() for synset in wn.all_synsets() for lemma in synset.lemmas()))

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

                # Write row to the file
                row_number += 1
                f.write(f"###{word}###{row_number}###{unique_word_counter}###{meaning_counter}###"
                        f"{synset.definition()}###{category}###{category_description}###{human_readable_pos}\n")

if __name__ == "__main__":
    # Generate the WordNet report and save it
    output_file = "wordnet_dictionary_report.txt"
    generate_wordnet_report(output_file)
    print(f"Report generated successfully and saved to {output_file}")