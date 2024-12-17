import re
from collections import Counter
from tkinter import Tk, filedialog

def extract_syllables(word):
    # Regular expression to match syllables
    syllable_pattern = re.compile(r'[aeiouy]+[^aeiouy]*', re.IGNORECASE)
    return syllable_pattern.findall(word)

def process_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    words = text.split()
    syllables = []
    
    for word in words:
        syllables.extend(extract_syllables(word))
    
    return syllables

def write_syllable_frequencies(syllables, output_file_path):
    syllable_counts = Counter(syllables)
    unique_syllables = sorted(syllable_counts.keys(), key=len)
    
    with open(output_file_path, 'w') as file:
        for syllable in unique_syllables:
            file.write(f"{syllable}\t{syllable_counts[syllable]}\n")

# Use Tkinter to select the input text file
root = Tk()
root.withdraw()  # Hide the root window
input_file_path = filedialog.askopenfilename(title="Select the large input text file")

# Path to the output text file
output_file_path = 'SANJOYNATHQHENOMENOLOGY_unique_syllables_frequencies.txt'

# Process the input file and get the list of syllables
syllables = process_text_file(input_file_path)

# Write the unique syllables and their frequencies to the output file
write_syllable_frequencies(syllables, output_file_path)

print(f"Unique syllables and their frequencies have been written to {output_file_path}.")