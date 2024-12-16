import tkinter as tk
from tkinter import filedialog
import pandas as pd
from collections import Counter

# Function to open file dialog and read the selected text file
def open_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path

# Function to process the text file
def process_text_file(file_path):
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Remove blank rows and strip whitespace
    lines = [line.strip() for line in lines if line.strip()]
    
    # Sort rows by trimmed text lengths
    sorted_lines = sorted(lines, key=len)
    
    # Save the sorted rows to a new text file
    with open('sorted_words.txt', 'w', encoding='utf-8') as file:
        for line in sorted_lines:
            file.write(line + '\n')
    
    # Count the frequency of each unique word
    word_counts = Counter(sorted_lines)
    
    # Prepare data for the unique words text file and Excel file
    unique_words_data = []
    for i, (word, count) in enumerate(word_counts.items(), start=1):
        unique_words_data.append([i, word, count])
    
    # Save the unique words and their frequencies to a new text file
    with open('unique_words.txt', 'w', encoding='utf-8') as file:
        for row in unique_words_data:
            file.write(f"{row[0]}\t{row[1]}\t{row[2]}\n")
    
    # Save the unique words and their frequencies to an Excel file
    df = pd.DataFrame(unique_words_data, columns=['Serial Number', 'Unique Word', 'Frequency'])
    df.to_excel('unique_words.xlsx', index=False)
    
    print("Processing complete. Files saved: sorted_words.txt, unique_words.txt, unique_words.xlsx")

# Main method
if __name__ == "__main__":
    file_path = open_file()  # Open file dialog to select the text file
    if file_path:
        process_text_file(file_path)
    else:
        print("No file selected.")