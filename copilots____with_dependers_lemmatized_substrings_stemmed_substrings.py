import nltk
from nltk.corpus import wordnet as wn
from collections import Counter
import pandas as pd
import re

def clean_token(token):
    """
    Cleans a token to ensure it contains only alphabets, numbers, and dots.
    Removes special characters, non-printable characters, and invalid symbols.
    """
    return re.sub(r"[^a-zA-Z0-9.]", "", token)

def count_pos_in_tokens(tokens, pos_tag):
    """
    Counts the number of tokens belonging to a specific part of speech.
    """
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

def lemmatize_and_stem(token):
    """
    Lemmatizes and stems a token.
    """
    lemmatizer = nltk.WordNetLemmatizer()
    stemmer = nltk.PorterStemmer()
    return stemmer.stem(lemmatizer.lemmatize(token))

def count_substring_occurrences(substring, text):
    """
    Counts the occurrences of a substring within a text.
    """
    return len(re.findall(re.escape(substring), text))

def generate_wordnet_report(output_file, excel_file):
    """
    Generate a WordNet report with unique tokens, cleaned and categorized by POS counts.
    Save it to a text file and export it to Excel.
    """
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
    
    data = [] # List to hold data for Excel export
    
    # Open the output file for writing
    with open(output_file, "w", encoding="utf-8") as f:
        # Write column headers
        f.write("###Word###Row Number###Unique Word Counter###Same Word Different Meaning Counter###Meaning"
                "###Category###Category Description###Part of Speech###Word Count###Word Count Percentile###Token Sum"
                "###Token Sum Percentile###Unique Token Count_in_all_meanings_on_same_word###Unique Tokens (Underscore-Separated)_in_all_meanings_on_same_word"
                "###Unique Token for current row of unique meaning for current word Count###Unique Tokens (Underscore-Separated) for current row of unique meaning for current word Count"
                "###Noun Count_in_only_current row_meanings_on_same_word###Verb Count_inonly_current row_meanings_on_same_word"
                "###Adverb Count_inonly_current row_meanings_on_same_word###Adjective Count_inonly_current row_meanings_on_same_word"
                "###Preposition Count_inonly_current row_meanings_on_same_word"
                "###Noun Count_in_all_meanings_on_same_word###Verb Count_in_all_meanings_on_same_word"
                "###Adverb Count_in_all_meanings_on_same_word###Adjective Count_in_all_meanings_on_same_word"
                "###Preposition Count_in_all_meanings_on_same_word###Depender Count###Lemmatized Stemmed Substrings Presences in Whole Dictionary Additional Depender Count\\n")
        
        unique_word_counter = 0
        row_number = 0
        
        # Get all words in WordNet (lemmas)
        lemmas = [lemma.name() for synset in wn.all_synsets() for lemma in synset.lemmas()]
        words = sorted(set(lemmas))
        
        # Count occurrences of each word in the dictionary
        word_count = Counter(lemmas)
        max_word_count = max(word_count.values()) # Max frequency for percentile calculation
        total_token_count = sum(word_count.values()) # Sum of all token frequencies
        
        # Combine all descriptions to calculate unique tokens
        combined_descriptions = " ".join([synset.definition() for synset in wn.all_synsets()])
        
        for word in words:
            unique_word_counter += 1
            synsets = wn.synsets(word)
            
            raw_tokens = set(combined_descriptions.lower().split())
            clean_tokens_all_meanings = {clean_token(token) for token in raw_tokens if clean_token(token)}
            unique_tokens_str_all_meanings = "_".join(sorted(clean_tokens_all_meanings))
            
            # POS counts for all meanings
            noun_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "noun")
            verb_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "verb")
            adverb_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "adverb")
            adjective_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "adjective")
            preposition_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "preposition")
            
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
                
                # Tokens and POS counts for the current row only
                raw_tokens_current_row = set(synset.definition().lower().split())
                clean_tokens_current_row = {clean_token(token) for token in raw_tokens_current_row if clean_token(token)}
                unique_tokens_str_current_row = "_".join(sorted(clean_tokens_current_row))
                
                noun_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "noun")
                verb_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "verb")
                adverb_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "adverb")
                adjective_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "adjective")
                preposition_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "preposition")
                
                # Calculate Depender Count
                depender_count = count + sum(word_count[token] for token in clean_tokens_current_row)
                
                # Calculate lemmatized and stemmed substring presence count
                lemmatized_stemmed_substrings_presences_in_whole_dictionary_additional_depender_count = 0
                for token in clean_tokens_current_row:
                    lemmatized_stemmed_token = lemmatize_and_stem(token)
                    lemmatized_stemmed_substrings_presences_in_whole_dictionary_additional_depender_count += count_substring_occurrences(lemmatized_stemmed_token, combined_descriptions)
                
                # Write row to the text file
                row_number += 1
                f.write(f"###{word}###{row_number}###{unique_word_counter}###{meaning_counter}###"
                        f"{synset.definition()}###{category}###{category_description}###{human_readable_pos}###{count}###"
                        f"{word_count_percentile:.2f}###{token_sum}###{token_sum_percentile:.2f}###{len(clean_tokens_all_meanings)}###{unique_tokens_str_all_meanings}###"
                        f"{len(clean_tokens_current_row)}###{unique_tokens_str_current_row}###{noun_count_current_row}###{verb_count_current_row}###{adverb_count_current_row}###{adjective_count_current_row}###{preposition_count_current_row}###"
                        f"{noun_count_all_meanings}###{verb_count_all_meanings}###{adverb_count_all_meanings}###{adjective_count_all_meanings}###{preposition_count_all_meanings}###"
                        f"{depender_count}###{lemmatized_stemmed_substrings_presences_in_whole_dictionary_additional_depender_count}\\n")
                
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
                    "Unique Token Count_in_all_meanings_on_same_word": len(clean_tokens_all_meanings),
                    "Unique Tokens (Underscore-Separated)_in_all_meanings_on_same_word": unique_tokens_str_all_meanings,
                    "Unique Token for current row of unique meaning for current word Count": len(clean_tokens_current_row),
###                    "Unique Tokens (Underscore-Separated) for
                    "Unique Tokens (Underscore-Separated) for current row of unique meaning for current word Count": unique_tokens_str_current_row,
                    "Noun Count_in_only_current row_meanings_on_same_word": noun_count_current_row,
                    "Verb Count_inonly_current row_meanings_on_same_word": verb_count_current_row,
                    "Adverb Count_inonly_current row_meanings_on_same_word": adverb_count_current_row,
                    "Adjective Count_inonly_current row_meanings_on_same_word": adjective_count_current_row,
                    "Preposition Count_inonly_current row_meanings_on_same_word": preposition_count_current_row,
                    "Noun Count_in_all_meanings_on_same_word": noun_count_all_meanings,
                    "Verb Count_in_all_meanings_on_same_word": verb_count_all_meanings,
                    "Adverb Count_in_all_meanings_on_same_word": adverb_count_all_meanings,
                    "Adjective Count_in_all_meanings_on_same_word": adjective_count_all_meanings,
                    "Preposition Count_in_all_meanings_on_same_word": preposition_count_all_meanings,
                    "Depender Count": depender_count,
                    "Lemmatized Stemmed Substrings Presences in Whole Dictionary Additional Depender Count": lemmatized_stemmed_substrings_presences_in_whole_dictionary_additional_depender_count
            })
    
    # Export data to Excel
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False, engine='openpyxl')
    print(f"Excel report generated successfully and saved to {excel_file}")

if __name__ == "__main__":
    # File paths
    output_file = "wth_depender_count_wordnet_dictionary_with_depender_counter_cleaned_with_pos_counts_forsamerow_and_also_for_unique_tokens_for_all_meanings_clubbed_for_same_word.txt"
    excel_file = "wth_depender_count_wordnet_dictionary_with_depender_counter_cleaned_with_pos_counts_forsamerow_and_also_for_unique_tokens_for_all_meanings_clubbed_for_same_word.xlsx"
    
    # Generate the WordNet report and save it
    generate_wordnet_report(output_file, excel_file)
    print(f"Report generated successfully and saved to {output_file}")