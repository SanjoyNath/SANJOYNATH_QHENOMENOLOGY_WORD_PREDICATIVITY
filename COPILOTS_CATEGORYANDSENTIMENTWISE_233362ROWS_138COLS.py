import pandas as pd
import nltk
from nltk.corpus import wordnet as wn
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

# Ensure required NLTK data is downloaded
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger', quiet=True)

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define category descriptions
categories = [
    "Adj all", "Adj pert", "Adj ppl", "Adv all", "Noun act", "Noun animal", "Noun artifact", "Noun attribute",
    "Noun body", "Noun cognition", "Noun communication", "Noun event", "Noun feeling", "Noun food", "Noun group",
    "Noun location", "Noun motive", "Noun object", "Noun person", "Noun phenomenon", "Noun plant", "Noun possession",
    "Noun process", "Noun quantity", "Noun relation", "Noun shape", "Noun state", "Noun substance", "Noun time",
    "Noun tops", "Verb body", "Verb change", "Verb cognition", "Verb communication", "Verb competition",
    "Verb consumption", "Verb contact", "Verb creation", "Verb emotion", "Verb motion", "Verb perception", "Verb possession",
    "Verb social", "Verb stative", "Verb weather"
]

# Function to clean tokens
def clean_token(token):
    """Cleans a token by removing special characters and invalid symbols."""
    return re.sub(r"[^a-zA-Z0-9.]", "", token)

# Function to count POS in tokens
def count_pos_in_tokens(tokens, pos_tag):
    """Counts tokens belonging to a specific POS."""
    tagged_tokens = nltk.pos_tag(tokens)
    pos_map = {
        "noun": ["NN", "NNS", "NNP", "NNPS"],
        "verb": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
        "adverb": ["RB", "RBR", "RBS"],
        "adjective": ["JJ", "JJR", "JJS"],
        "preposition": ["IN"]
    }
    return sum(1 for _, tag in tagged_tokens if tag in pos_map[pos_tag])

# Function to compute category frequencies
def compute_category_frequencies(tokens, categories):
    frequencies = {category: 0 for category in categories}
    for token in tokens:
        for synset in wn.synsets(token):
            category = synset.lexname()
            if category in frequencies:
                frequencies[category] += 1
    return frequencies

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']

# Merged functionality to process WordNet and generate report
def generate_combined_report(output_file, excel_file):
    data = []  # List to hold data for Excel export
    lemmas = [lemma.name() for synset in wn.all_synsets() for lemma in synset.lemmas()]
    words = sorted(set(lemmas))

    word_count = Counter(lemmas)
    max_word_count = max(word_count.values())
    total_token_count = sum(word_count.values())

    for word in words:
        synsets = wn.synsets(word)
        combined_descriptions = " ".join([synset.definition() for synset in synsets])
        raw_tokens = set(combined_descriptions.lower().split())
        clean_tokens_all_meanings = {clean_token(token) for token in raw_tokens if clean_token(token)}

        noun_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "noun")
        verb_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "verb")
        adverb_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "adverb")
        adjective_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "adjective")
        preposition_count_all_meanings = count_pos_in_tokens(clean_tokens_all_meanings, "preposition")

        # Compute category frequencies for all meanings
        category_frequencies_all_meanings = compute_category_frequencies(clean_tokens_all_meanings, categories)

        for meaning_counter, synset in enumerate(synsets, start=1):
            category = synset.lexname()
            part_of_speech = synset.pos()
            human_readable_pos = {
                "n": "Noun", "v": "Verb", "a": "Adjective", "s": "Adjective Satellite", "r": "Adverb"
            }.get(part_of_speech, "Unknown")

            count = word_count[word]
            word_count_percentile = (count / max_word_count) * 100
            token_sum = sum(word_count[lemma.name()] for lemma in synset.lemmas())
            token_sum_percentile = (token_sum / total_token_count) * 100

            raw_tokens_current_row = set(synset.definition().lower().split())
            clean_tokens_current_row = {clean_token(token) for token in raw_tokens_current_row if clean_token(token)}

            noun_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "noun")
            verb_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "verb")
            adverb_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "adverb")
            adjective_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "adjective")
            preposition_count_current_row = count_pos_in_tokens(clean_tokens_current_row, "preposition")

            # Compute category frequencies for current row
            category_frequencies_current_row = compute_category_frequencies(clean_tokens_current_row, categories)

            sentiment_current = analyze_sentiment(synset.definition())
            sentiment_all = analyze_sentiment(combined_descriptions)

            row_data = {
                "Word": word,
                "Meaning": synset.definition(),
                "Category": category,
                "POS": human_readable_pos,
                "Unique Token Count (All Meanings)": len(clean_tokens_all_meanings),
                "Unique Token Count (Current Row)": len(clean_tokens_current_row),
                "Noun Count (All)": noun_count_all_meanings,
                "Verb Count (All)": verb_count_all_meanings,
                "Adverb Count (All)": adverb_count_all_meanings,
                "Adjective Count (All)": adjective_count_all_meanings,
                "Preposition Count (All)": preposition_count_all_meanings,
                "Noun Count (Current)": noun_count_current_row,
                "Verb Count (Current)": verb_count_current_row,
                "Adverb Count (Current)": adverb_count_current_row,
                "Adjective Count (Current)": adjective_count_current_row,
                "Preposition Count (Current)": preposition_count_current_row,
                "Sentiment (Current)": sentiment_current,
                "Sentiment (All)": sentiment_all
            }

            # Add category frequency columns for all meanings
            for category in categories:
                row_data[f"{category} Frequency (All)"] = category_frequencies_all_meanings.get(category, 0)

            # Add category frequency columns for current row
            for category in categories:
                row_data[f"{category} Frequency (Current)"] = category_frequencies_current_row.get(category, 0)

            data.append(row_data)

    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False, engine="openpyxl")
    print(f"Report generated and saved to {excel_file}")

# Run the combined report generation
generate_combined_report(
    output_file="copilot_detailed_reports_wordnet_combined_report.txt",
    excel_file="copilot_detailed_reports_wordnet_combined_report.xlsx"
)