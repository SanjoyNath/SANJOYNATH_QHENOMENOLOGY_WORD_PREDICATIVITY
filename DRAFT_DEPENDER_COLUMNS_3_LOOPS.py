import nltk
from nltk.corpus import wordnet as wn
from collections import Counter
import pandas as pd
import re

def clean_token(token):
    """Cleans a token to ensure it contains only alphabets, numbers, and dots."""
    return re.sub(r"[^a-zA-Z0-9.]", "", token)

def count_pos_in_tokens(tokens, pos_tag):
    """Counts the number of tokens belonging to a specific part of speech."""
    nltk.download('averaged_perceptron_tagger', quiet=True)
    tagged_tokens = nltk.pos_tag(tokens)
    pos_map = {
        "noun": ["NN", "NNS", "NNP", "NNPS"],
        "verb": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "adverb": ["RB", "RBR", "RBS"],
        "adjective": ["JJ", "JJR", "JJS"],
        "preposition": ["IN"]
    }
    return sum(1 for _, tag in tagged_tokens if tag in pos_map[pos_tag])

def generate_wordnet_report(output_file, excel_file):
    """Generate a WordNet report with unique tokens, cleaned and categorized by POS counts."""
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)

    data = []  # List to hold data for Excel export
    dependency_data = []  # For holding dependencies for each word

    # Open the output file for writing
    with open(output_file, "w", encoding="utf-8") as f:
        # Write column headers
        f.write("###Word###Row Number###Unique Word Counter###Same Word Different Meaning Counter###Meaning"
                "###Category###Category Description###Part of Speech###Word Count###Word Count Percentile###Token Sum"
                "###Token Sum Percentile###Unique Token Count###Unique Tokens (Underscore-Separated)###"
                "Noun Count###Verb Count###Adverb Count###Adjective Count###Preposition Count###Depends_On_Words###Cardinality\n")

        unique_word_counter = 0
        row_number = 0

        # Get all words in WordNet (lemmas)
        lemmas = [lemma.name() for synset in wn.all_synsets() for lemma in synset.lemmas()]
        words = sorted(set(lemmas))

        # Count occurrences of each word in the dictionary
        word_count = Counter(lemmas)
        max_word_count = max(word_count.values())  # Max frequency for percentile calculation
        total_token_count = sum(word_count.values())  # Sum of all token frequencies

        for word in words:
            unique_word_counter += 1
            synsets = wn.synsets(word)

            # Combine all descriptions to calculate unique tokens
            combined_descriptions = " ".join([synset.definition() for synset in synsets])
            raw_tokens = set(combined_descriptions.lower().split())
            clean_tokens = {clean_token(token) for token in raw_tokens if clean_token(token)}
            unique_tokens_str = "_".join(sorted(clean_tokens))

            # POS counts
            noun_count = count_pos_in_tokens(clean_tokens, "noun")
            verb_count = count_pos_in_tokens(clean_tokens, "verb")
            adverb_count = count_pos_in_tokens(clean_tokens, "adverb")
            adjective_count = count_pos_in_tokens(clean_tokens, "adjective")
            preposition_count = count_pos_in_tokens(clean_tokens, "preposition")

            for meaning_counter, synset in enumerate(synsets, start=1):
                category = synset.lexname()
                category_description = synset.lexname().replace('.', ' ').capitalize()
                part_of_speech = synset.pos()

                pos_mapping = {
                    "n": "Noun",
                    "v": "Verb",
                    "a": "Adjective",
                    "s": "Adjective Satellite",
                    "r": "Adverb",
                }
                human_readable_pos = pos_mapping.get(part_of_speech, "Unknown")

                count = word_count[word]
                word_count_percentile = (count / max_word_count) * 100
                token_sum = sum(word_count[lemma.name()] for lemma in synset.lemmas())
                token_sum_percentile = (token_sum / total_token_count) * 100

                # Write row to the text file
                row_number += 1
                f.write(f"###{word}###{row_number}###{unique_word_counter}###{meaning_counter}###"
                        f"{synset.definition()}###{category}###{category_description}###{human_readable_pos}###{count}###"
                        f"{word_count_percentile:.2f}###"
                        f"{token_sum}###"
                        f"{token_sum_percentile:.2f}###"
                        f"{len(clean_tokens)}###{unique_tokens_str}###"
                        f"{noun_count}###{verb_count}###{adverb_count}###{adjective_count}###{preposition_count}###"
                        f"###\n")

                # Collect word-level data for dependencies
                dependency_data.append({
                    "Word": word,
                    "Row Number": row_number,
                    "Unique Tokens (Underscore-Separated)": unique_tokens_str,
                    "Clean Tokens": clean_tokens
                })

                # Append row to the data list for Excel
                data.append({
                    "Word": word,
                    "Row Number": row_number,
                    "Unique Word Counter": unique_word_counter,
                    "Same Word Different Meaning Counter": meaning_counter,
                    "Meaning": synset.definition(),
                    "Category": category,
                    "Category Description": category_description,
                    "Part of Speech": human_readable_pos,
                    "Word Count": count,
                    "Word Count Percentile": word_count_percentile,
                    "Token Sum": token_sum,
                    "Token Sum Percentile": token_sum_percentile,
                    "Unique Token Count": len(clean_tokens),
                    "Unique Tokens (Underscore-Separated)": unique_tokens_str,
                    "Noun Count": noun_count,
                    "Verb Count": verb_count,
                    "Adverb Count": adverb_count,
                    "Adjective Count": adjective_count,
                    "Preposition Count": preposition_count,
                    "Depends On Words": "",  # Placeholder for the new column
                    "Cardinality": 0  # Placeholder for cardinality
                })

    # Now process the dependency data
    df = pd.DataFrame(data)
    for idx, row in df.iterrows():
        word = row['Word']
        # Find words that depend on the current word
        depends_on_words = set()
        for dep_row in dependency_data:
            # Check if current word appears in any other word's unique tokens
            if word in dep_row['Clean Tokens']:
                depends_on_words.add(dep_row['Word'])

        # Update the "Depends On Words" column with the underscore-separated tokens
        df.at[idx, 'Depends On Words'] = "_".join(sorted(depends_on_words))

        # Calculate cardinality (number of unique dependencies)
        df.at[idx, 'Cardinality'] = len(depends_on_words)

    # Export final data to Excel
    df.to_excel(excel_file, index=False, engine='openpyxl')
    print(f"Excel report generated successfully and saved to {excel_file}")

if __name__ == "__main__":
    output_file = "wordnet_dictionary_cleaned_with_pos_counts.txt"
    excel_file = "wordnet_dictionary_cleaned_with_pos_counts_with_dependencies.xlsx"
    
    generate_wordnet_report(output_file, excel_file)
    print(f"Report generated successfully and saved to {output_file}")