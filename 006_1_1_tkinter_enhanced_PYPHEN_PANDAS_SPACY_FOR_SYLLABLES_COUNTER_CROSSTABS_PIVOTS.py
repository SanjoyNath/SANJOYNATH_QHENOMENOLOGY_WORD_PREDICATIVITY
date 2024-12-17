import spacy
import pyphen
import pandas as pd
from collections import Counter
import os
from tkinter import Tk, filedialog

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Add the syllables component to the pipeline using Pyphen
class SyllablesComponent:
    def __init__(self, nlp, lang='en'):
        self.hyphenator = pyphen.Pyphen(lang=lang)
        if not spacy.tokens.Token.has_extension("syllables"):
            spacy.tokens.Token.set_extension("syllables", getter=self.get_syllables)
            spacy.tokens.Token.set_extension("syllables_count", getter=self.get_syllables_count)

    def __call__(self, doc):
        for token in doc:
            token._.syllables = self.get_syllables(token)
            token._.syllables_count = self.get_syllables_count(token)
        return doc

    def get_syllables(self, token):
        return self.hyphenator.inserted(token.text).split('-')

    def get_syllables_count(self, token):
        return len(self.get_syllables(token))

@spacy.Language.factory("syllables")
def create_syllables_component(nlp, name):
    return SyllablesComponent(nlp)

nlp.add_pipe("syllables", after="tagger")

# Function to process a text file and generate syllable reports
def generate_syllable_reports(file_path):
    # Read the words from the file
    with open(file_path, 'r') as f:
        words = f.read().splitlines()

    # Process each word and extract syllable information
    syllable_counter = Counter()
    word_syllables = {}

    for word in words:
        doc = nlp(word)
        for token in doc:
            syllables = token._.syllables
            if syllables:
                word_syllables[word] = syllables
                syllable_counter.update(syllables)

    # Generate syllable frequency report
    syllable_freq_report = pd.DataFrame(syllable_counter.items(), columns=['Syllable', 'Frequency'])
    syllable_freq_report = syllable_freq_report.sort_values(by='Frequency', ascending=False)

    # Save the syllable frequency report to a file
    syllable_freq_report.to_csv('syllable_frequency_report.csv', index=False)

    # Generate pivot report
    unique_syllables = sorted(syllable_counter.keys())
    pivot_data = pd.DataFrame(0, index=unique_syllables, columns=unique_syllables)

    for word, syllables in word_syllables.items():
        for i in range(len(syllables)):
            for j in range(i, len(syllables)):
                pivot_data.at[syllables[i], syllables[j]] += 1

    # Save the pivot report to an Excel file
    with pd.ExcelWriter('syllable_pivot_report.xlsx') as writer:
        pivot_data.to_excel(writer, sheet_name='Pivot Report')

# Function to select a large text file and generate reports using tkinter
def select_file_and_generate_reports():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a large text file", filetypes=[("Text files", "*.txt")])
    
    if file_path and os.path.isfile(file_path):
        generate_syllable_reports(file_path)
        print("Syllable reports generated successfully.")
    else:
        print("Invalid file path. Please try again.")

# Run the function to select file and generate reports
select_file_and_generate_reports()