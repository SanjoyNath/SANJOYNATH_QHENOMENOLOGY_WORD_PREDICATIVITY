import re
from collections import Counter, defaultdict
from tkinter import Tk, filedialog
import pandas as pd

def extract_syllables(word):
    # Regular expression to match syllables
    syllable_pattern = re.compile(r'[aeiouy]+[^aeiouy]*', re.IGNORECASE)
    return syllable_pattern.findall(word)

def open_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path

def process_text_file(file_path):
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    total_lines = len(lines)
    
    # Convert all texts to lower case, remove blank rows, and strip whitespace
    lines = [line.strip().lower() for line in lines if line.strip()]
    
    # Sort rows by trimmed text lengths
    sorted_lines = sorted(lines, key=len)
    
    # Save the sorted rows to a new text file
    with open('WITH_RUNLOGSALSO_WITH_PREFIX_SUBSTRING_SUFFIX_STRINGS_TOKENS_uniquing_first_sorted_words.txt', 'w', encoding='utf-8') as file:
        for line in sorted_lines:
            file.write(line + '\n')
    
    # Count the frequency of each unique word
    word_counts = Counter(sorted_lines)
    
    # Prepare data for the unique words text file and Excel file
    unique_words_data = []
    prefix_counts = defaultdict(int)
    suffix_counts = defaultdict(int)
    middle_counts = defaultdict(int)
    
    # Precompute prefix, suffix, and middle counts
    for idx, line in enumerate(sorted_lines):
        for word in word_counts:
            if line.startswith(word):
                prefix_counts[word] += 1
            if line.endswith(word):
                suffix_counts[word] += 1
            if word in line and not (line.startswith(word) or line.endswith(word)):
                middle_counts[word] += 1
        
        # Print progress
        print(f"Processed {idx + 1} out of {total_lines} lines")
    
    for i, (word, count) in enumerate(word_counts.items(), start=1):
        prefix_count = prefix_counts[word] * count
        suffix_count = suffix_counts[word] * count
        middle_count = middle_counts[word] * count
        
        unique_words_data.append([i, word, count, prefix_count, suffix_count, middle_count])
    
    # Save the unique words and their frequencies to a new text file
    with open('WITHRUNLOGSALSO_unique_words.txt', 'w', encoding='utf-8') as file:
        for row in unique_words_data:
            file.write(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\n")
    
    # Save the unique words and their frequencies to an Excel file
    df = pd.DataFrame(unique_words_data, columns=['Serial Number', 'Unique Word', 'Total Frequency', 'Prefix Frequency', 'Suffix Frequency', 'Middle Frequency'])
    df.to_excel('wthrunslogs_uniquingfirst_unique_words.xlsx', index=False)
    
    print("Processing complete. Files saved: WITH_PREFIX_SUBSTRING_SUFFIX_STRINGS_TOKENS_uniquing_first_sorted_words.txt, unique_words.txt, uniquingfirst_unique_words.xlsx")

# Main method
if __name__ == "__main__":
    file_path = open_file()  # Open file dialog to select the text file
    if file_path:
        process_text_file(file_path)
    else:
        print("No file selected.")
