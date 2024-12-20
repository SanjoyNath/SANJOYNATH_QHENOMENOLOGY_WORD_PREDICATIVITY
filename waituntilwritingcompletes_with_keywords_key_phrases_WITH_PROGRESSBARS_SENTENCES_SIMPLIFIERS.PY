import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pdfplumber
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from collections import Counter
import os

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Function to extract text from a TXT file
def extract_text_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as file:
        return file.read()

# Function to tokenize text into sentences
def tokenize_sentences(text):
    return sent_tokenize(text)

# Function to simplify a single sentence using the pretrained model
def simplify_sentence(sentence, tokenizer, model):
    inputs = tokenizer("simplify: " + sentence, return_tensors="pt", truncation=True)
    outputs = model.generate(inputs["input_ids"], max_length=512, num_beams=4, early_stopping=True)
    simplified = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return simplified.split(". ")  # Split into parts

# Function to calculate a proxy comprehensibility score
def calculate_comprehensibility(sentence):
    words = sentence.split()
    unique_words = set(words)
    return len(words) / len(unique_words) if unique_words else 0

# Function to extract keywords and key phrases
def extract_keywords_and_phrases(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    keywords = [word for word in words if word.isalnum() and word.lower() not in stop_words]
    key_phrases = [" ".join(phrase) for phrase in zip(words, words[1:]) if all(w.isalnum() for w in phrase)]
    return Counter(keywords), Counter(key_phrases)

def process_file_with_progress(input_file, file_type, output_file1, output_file2, tokenizer, model, progress_bar, progress_label):
    try:
        # Extract text based on file type
        text = extract_text_from_pdf(input_file) if file_type == "pdf" else extract_text_from_txt(input_file)
        
        # Tokenize text into sentences
        sentences = tokenize_sentences(text)
        total_sentences = len(sentences)

        # Ensure there are sentences to process
        if total_sentences == 0:
            raise ValueError("No sentences found in the document.")

        # Data structure to hold sentence complexities and simplified parts
        sentence_data = []

        # Process each sentence
        with open(output_file1, "w", encoding="utf-8") as f1:
            for i, sentence in enumerate(sentences, start=1):
                # Update progress bar and label
                progress_bar["value"] = (i / total_sentences) * 100
                progress_label["text"] = f"Processing sentence {i}/{total_sentences}"
                progress_bar.update()

                # Calculate complexity
                complexity = calculate_comprehensibility(sentence)

                # Simplify sentence
                simplified_parts = simplify_sentence(sentence, tokenizer, model)

                # Write to first output file
                f1.write(f"{i}.0 {sentence.strip()} [Complexity: {complexity:.2f}]\n")
                for j, part in enumerate(simplified_parts, start=1):
                    complexity_part = calculate_comprehensibility(part)
                    f1.write(f"{i}.{j} {part.strip()} [Complexity: {complexity_part:.2f}]\n")
                
                # Collect data for sorting
                sentence_data.append((sentence.strip(), complexity, simplified_parts))

        # Sort by complexity
        sorted_data = sorted(sentence_data, key=lambda x: x[1])

        # Extract keywords and key phrases
        all_text = " ".join([s[0] for s in sorted_data])  # Combine all sentences
        keywords, key_phrases = extract_keywords_and_phrases(all_text)

        # Write to second output file
        with open(output_file2, "w", encoding="utf-8") as f2:
            for sentence, complexity, simplified_parts in sorted_data:
                f2.write(f"Sentence: {sentence} [Complexity: {complexity:.2f}]\n")
                for part in simplified_parts:
                    f2.write(f"  Simplified: {part.strip()}\n")
            f2.write("\n--- Keywords and Their Complexity ---\n")
            for keyword, count in keywords.most_common():
                f2.write(f"{keyword}: {count}\n")
            f2.write("\n--- Key Phrases and Their Complexity ---\n")
            for phrase, count in key_phrases.most_common():
                f2.write(f"{phrase}: {count}\n")

        # Finalize progress
        progress_label["text"] = "Processing complete!"
        return True  # Indicate success

    except Exception as e:
        progress_label["text"] = f"Error: {e}"
        return False  # Indicate failure

# Update select_file to only show success if the processing is complete
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt")])
    if not file_path:
        return
    file_type = "pdf" if file_path.endswith(".pdf") else "txt"
    output_file1 = file_path + "_SIMPLIFIED_SENTENCES.TXT"
    output_file2 = file_path + "_SORTED_COMPLEXITY.TXT"
    if not output_file1 or not output_file2:
        return
    try:
        progress_label["text"] = "Initializing..."
        progress_bar["value"] = 0
        success = process_file_with_progress(file_path, file_type, output_file1, output_file2, tokenizer, model, progress_bar, progress_label)
        if success:
            messagebox.showinfo("Success", f"Processing complete!\nOutputs:\n1. {output_file1}\n2. {output_file2}")
        else:
            messagebox.showerror("Error", "Processing failed. Check progress and files.")
    except Exception as e:
        progress_label["text"] = "Error occurred."
        messagebox.showerror("Error", f"An error occurred: {e}")	
	
	# # # def process_file_with_progress(input_file, file_type, output_file1, output_file2, tokenizer, model, progress_bar, progress_label):
    # # # try:
        # # # Extract text based on file type
        # # # text = extract_text_from_pdf(input_file) if file_type == "pdf" else extract_text_from_txt(input_file)
        
        # # # Tokenize text into sentences
        # # # sentences = tokenize_sentences(text)
        # # # total_sentences = len(sentences)

        # # # Ensure there are sentences to process
        # # # if total_sentences == 0:
            # # # raise ValueError("No sentences found in the document.")

        # # # Data structure to hold sentence complexities and simplified parts
        # # # sentence_data = []

        # # # Process each sentence
        # # # with open(output_file1, "w", encoding="utf-8") as f1:
            # # # for i, sentence in enumerate(sentences, start=1):
                # # # Update progress bar and label
                # # # progress_bar["value"] = (i / total_sentences) * 100
                # # # progress_label["text"] = f"Processing sentence {i}/{total_sentences}"
                # # # progress_bar.update()

                # # # Calculate complexity
                # # # complexity = calculate_comprehensibility(sentence)

                # # # Simplify sentence
                # # # simplified_parts = simplify_sentence(sentence, tokenizer, model)

                # # # Write to first output file
                # # # f1.write(f"{i}.0 {sentence.strip()} [Complexity: {complexity:.2f}]\n")
                # # # for j, part in enumerate(simplified_parts, start=1):
                    # # # complexity_part = calculate_comprehensibility(part)
                    # # # f1.write(f"{i}.{j} {part.strip()} [Complexity: {complexity_part:.2f}]\n")
                
                # # # Collect data for sorting
                # # # sentence_data.append((sentence.strip(), complexity, simplified_parts))

        # # # Sort by complexity
        # # # sorted_data = sorted(sentence_data, key=lambda x: x[1])

        # # # Extract keywords and key phrases
        # # # all_text = " ".join([s[0] for s in sorted_data])  # Combine all sentences
        # # # keywords, key_phrases = extract_keywords_and_phrases(all_text)

        # # # Write to second output file
        # # # with open(output_file2, "w", encoding="utf-8") as f2:
            # # # for sentence, complexity, simplified_parts in sorted_data:
                # # # f2.write(f"Sentence: {sentence} [Complexity: {complexity:.2f}]\n")
                # # # for part in simplified_parts:
                    # # # f2.write(f"  Simplified: {part.strip()}\n")
            # # # f2.write("\n--- Keywords and Their Complexity ---\n")
            # # # for keyword, count in keywords.most_common():
                # # # f2.write(f"{keyword}: {count}\n")
            # # # f2.write("\n--- Key Phrases and Their Complexity ---\n")
            # # # for phrase, count in key_phrases.most_common():
                # # # f2.write(f"{phrase}: {count}\n")

        # # # Finalize progress
        # # # progress_label["text"] = "Processing complete!"
        # # # return True  # Indicate success

    # # # except Exception as e:
        # # # progress_label["text"] = f"Error: {e}"
        # # # return False  # Indicate failure

# Update select_file to only show success if the processing is complete
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt")])
    if not file_path:
        return
    file_type = "pdf" if file_path.endswith(".pdf") else "txt"
    output_file1 = file_path + "_SIMPLIFIED_SENTENCES.TXT"
    output_file2 = file_path + "_SORTED_COMPLEXITY.TXT"
    if not output_file1 or not output_file2:
        return
    try:
        progress_label["text"] = "Initializing..."
        progress_bar["value"] = 0
        success = process_file_with_progress(file_path, file_type, output_file1, output_file2, tokenizer, model, progress_bar, progress_label)
        if success:
            messagebox.showinfo("Success", f"Processing complete!\nOutputs:\n1. {output_file1}\n2. {output_file2}")
        else:
            messagebox.showerror("Error", "Processing failed. Check progress and files.")
    except Exception as e:
        progress_label["text"] = "Error occurred."
        messagebox.showerror("Error", f"An error occurred: {e}")
		
		
		
# # # # Function to process the file and dump results
# # # def process_file_with_progress(input_file, file_type, output_file1, output_file2, tokenizer, model, progress_bar, progress_label):
    # # # # Extract text based on file type
    # # # text = extract_text_from_pdf(input_file) if file_type == "pdf" else extract_text_from_txt(input_file)
    
    # # # # Tokenize text into sentences
    # # # sentences = tokenize_sentences(text)
    # # # total_sentences = len(sentences)

    # # # # Data structure to hold sentence complexities and simplified parts
    # # # sentence_data = []

    # # # # Process each sentence
    # # # with open(output_file1, "w", encoding="utf-8") as f1:
        # # # for i, sentence in enumerate(sentences, start=1):
            # # # # Update progress bar and label
            # # # progress_bar["value"] = (i / total_sentences) * 100
            # # # progress_label["text"] = f"Processing sentence {i}/{total_sentences}"
            # # # progress_bar.update()

            # # # # Calculate complexity
            # # # complexity = calculate_comprehensibility(sentence)

            # # # # Simplify sentence
            # # # simplified_parts = simplify_sentence(sentence, tokenizer, model)

            # # # # Write to first output file
            # # # f1.write(f"{i}.0 {sentence.strip()} [Complexity: {complexity:.2f}]\n")
            # # # for j, part in enumerate(simplified_parts, start=1):
                # # # complexity_part = calculate_comprehensibility(part)
                # # # f1.write(f"{i}.{j} {part.strip()} [Complexity: {complexity_part:.2f}]\n")
            
            # # # # Collect data for sorting
            # # # sentence_data.append((sentence.strip(), complexity, simplified_parts))

    # # # # Sort by complexity
    # # # sorted_data = sorted(sentence_data, key=lambda x: x[1])

    # # # # Extract keywords and key phrases
    # # # all_text = " ".join([s[0] for s in sorted_data])  # Combine all sentences
    # # # keywords, key_phrases = extract_keywords_and_phrases(all_text)

    # # # # Write to second output file
    # # # with open(output_file2, "w", encoding="utf-8") as f2:
        # # # for sentence, complexity, simplified_parts in sorted_data:
            # # # f2.write(f"Sentence: {sentence} [Complexity: {complexity:.2f}]\n")
            # # # for part in simplified_parts:
                # # # f2.write(f"  Simplified: {part.strip()}\n")
        # # # f2.write("\n--- Keywords and Their Complexity ---\n")
        # # # for keyword, count in keywords.most_common():
            # # # f2.write(f"{keyword}: {count}\n")
        # # # f2.write("\n--- Key Phrases and Their Complexity ---\n")
        # # # for phrase, count in key_phrases.most_common():
            # # # f2.write(f"{phrase}: {count}\n")

# Main function to handle Tkinter interface and processing
def main():
    # Load pretrained models (offline)
    model_name = "t5-small"  # Change to "facebook/bart-large" if needed
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Tkinter GUI
    def select_file():
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt")])
        if not file_path:
            return
        file_type = "pdf" if file_path.endswith(".pdf") else "txt"
        output_file1 = file_path + "_SIMPLIFIED_SENTENCES.TXT"
        output_file2 = file_path + "_SORTED_COMPLEXITY.TXT"
        if not output_file1 or not output_file2:
            return
        try:
            progress_label["text"] = "Initializing..."
            progress_bar["value"] = 0
            process_file_with_progress(file_path, file_type, output_file1, output_file2, tokenizer, model, progress_bar, progress_label)
            progress_label["text"] = "Processing complete!"
            messagebox.showinfo("Success", f"Processing complete!\nOutputs:\n1. {output_file1}\n2. {output_file2}")
        except Exception as e:
            progress_label["text"] = "Error occurred."
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Create Tkinter GUI
    root = tk.Tk()
    root.title("Semantic Analysis and Sentence Simplification")

    tk.Label(root, text="Select a PDF or TXT file to process").pack(pady=10)
    tk.Button(root, text="Select File", command=select_file).pack(pady=20)

    progress_label = tk.Label(root, text="")
    progress_label.pack(pady=5)

    progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=5)

    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()