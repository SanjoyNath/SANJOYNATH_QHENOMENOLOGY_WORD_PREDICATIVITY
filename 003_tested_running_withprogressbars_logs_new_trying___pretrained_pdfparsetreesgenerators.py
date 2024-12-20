import fitz  # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
import pdfplumber
import os
from tkinter import Tk, filedialog, messagebox
import torch
from tqdm import tqdm  # For the progress bar
import logging

# Set up logging for better error tracking
logging.basicConfig(filename="process_log.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize the HuggingFace tokenizer and model for text generation (T5 for sequence-to-sequence tasks)
model_name = "t5-small"  # Change this to any seq2seq model like "t5-base", "t5-large"
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    logging.info("Model and tokenizer loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model and tokenizer: {e}")
    raise

# Ensure model is on the appropriate device (CPU or CUDA for GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Use Hugging Face's parsing pipeline for text generation
parse_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=device.index if device.type == 'cuda' else -1)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        logging.info(f"Text extracted from PDF: {pdf_path}")
        return text
    except Exception as e:
        logging.error(f"Error extracting text from PDF {pdf_path}: {e}")
        raise

# Function to extract text from TXT file
def extract_text_from_txt(txt_path):
    try:
        with open(txt_path, "r", encoding="utf-8") as file:
            text = file.read()
        logging.info(f"Text extracted from TXT: {txt_path}")
        return text
    except Exception as e:
        logging.error(f"Error extracting text from TXT {txt_path}: {e}")
        raise

# Function to generate a parse tree for a sentence using HuggingFace model
def generate_parse_tree(sentence):
    try:
        result = parse_pipeline(sentence, max_new_tokens=100)  # Set a limit for generated tokens
        return result[0]['generated_text']
    except Exception as e:
        logging.error(f"Error generating parse tree for sentence: {sentence} - {e}")
        raise

# Function to create a PDF with sentences and parse trees
def create_pdf_with_parse_trees(sentences, output_pdf_path):
    try:
        doc = fitz.open()  # Create a new PDF document

        for idx, sentence in enumerate(sentences):
            page = doc.new_page()  # Add a new page for each sentence
            page.insert_text((72, 72), sentence, fontsize=12)  # Insert the sentence text

            # Get parse tree for the sentence (use your NLP model for parsing)
            parse_tree = generate_parse_tree(sentence)
            page.insert_text((72, 150), f"Parse Tree:\n{parse_tree}", fontsize=10)  # Insert the parse tree

            # Update progress bar
            progress_bar.update(1)  # Update progress bar here

        doc.save(output_pdf_path)  # Save the PDF
        logging.info(f"PDF created successfully at: {output_pdf_path}")
    except Exception as e:
        logging.error(f"Error creating PDF with parse trees: {e}")
        raise

# Main function to run the application
def main():
    try:
        # Initialize Tkinter dialog
        root = Tk()
        root.withdraw()

        # Prompt user to select a file (either PDF or TXT)
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])

        if not file_path:
            messagebox.showerror("Error", "No file selected. Exiting.")
            logging.warning("No file selected by the user.")
            return

        # Extract text from the file
        if file_path.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        else:
            text = extract_text_from_txt(file_path)

        # Tokenize the text into sentences
        sentences = sent_tokenize(text)
        total_sentences = len(sentences)
        
        # Set up the progress bar (correctly placed before processing begins)
        global progress_bar
        progress_bar = tqdm(total=total_sentences, desc="Processing Sentences", unit="sentence")

        # Create a PDF with parse trees for each sentence
        output_pdf_path = "output_with_parse_trees.pdf"
        create_pdf_with_parse_trees(sentences, output_pdf_path)

        progress_bar.close()  # Close the progress bar once done
        messagebox.showinfo("Success", f"PDF generated: {output_pdf_path}")
        logging.info(f"PDF generated successfully: {output_pdf_path}")

    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()