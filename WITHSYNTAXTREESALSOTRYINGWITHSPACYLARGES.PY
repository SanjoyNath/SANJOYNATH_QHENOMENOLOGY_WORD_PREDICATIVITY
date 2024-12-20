import tkinter as tk
from tkinter import filedialog, messagebox
import spacy
import os
import fitz  # PyMuPDF

# Function to extract text from a TXT file
def extract_text_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as file:
        return file.read()

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to flatten the text and replace sentence endings
def process_text(text):
    text = text.replace("\r\n", "")
    sentences = text.split(".")
    sentences = [sentence.strip() + ".\r\n" for sentence in sentences if sentence.strip()]
    return sentences

# Function to create complexity analysis report
def create_complexity_report(sentences, nlp):
    report = []
    for i, sentence in enumerate(sentences, start=1):
        doc = nlp(sentence)
        tokens = [token.text for token in doc]
        unique_tokens = set(tokens)
        complexity = len(tokens) / len(unique_tokens) if unique_tokens else 0
        report.append(f"{i}. {sentence.strip()} [Complexity: {complexity:.2f}]")
    return report

# Function to generate SVG files for sentence syntax trees
def generate_svg_files(sentences, nlp):
    svg_files = []
    for i, sentence in enumerate(sentences, start=1):
        doc = nlp(sentence)
        svg = spacy.displacy.render(doc, style="dep", jupyter=False)
        svg_filename = f"sentence_{i}.svg"
        with open(svg_filename, "w", encoding="utf-8") as file:
            file.write(svg)
        svg_files.append(svg_filename)
    return svg_files

# Function to combine SVG files into a single PDF
def combine_svgs_to_pdf(svg_files, output_pdf):
    pdf_document = fitz.open()
    for svg_file in svg_files:
        img_doc = fitz.open(svg_file)
        pdf_bytes = img_doc.convert_to_pdf()
        img_pdf = fitz.open("pdf", pdf_bytes)
        pdf_document.insert_pdf(img_pdf)
    pdf_document.save(output_pdf)

# Main function to handle Tkinter interface and processing
def main():
    # Load large spacy model
    nlp = spacy.load("en_core_web_lg")

    # Tkinter GUI
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
    if not file_path:
        messagebox.showerror("Error", "No file selected.")
        return
    
    try:
        # Extract text from the selected file
        if file_path.endswith(".txt"):
            text = extract_text_from_txt(file_path)
        elif file_path.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        else:
            messagebox.showerror("Error", "Unsupported file type.")
            return
        
        # Process the text
        sentences = process_text(text)
        
        # Create complexity analysis report
        complexity_report = create_complexity_report(sentences, nlp)
        
        # Write the complexity report to a new file
        report_file_path = os.path.splitext(file_path)[0] + "_complexity_report.txt"
        with open(report_file_path, "w", encoding="utf-8") as report_file:
            report_file.write("\n".join(complexity_report))
        
        # Generate SVG files for sentence syntax trees
        svg_files = generate_svg_files(sentences, nlp)
        
        # Combine SVG files into a single PDF
        output_pdf_path = os.path.splitext(file_path)[0] + "_syntax_trees.pdf"
        combine_svgs_to_pdf(svg_files, output_pdf_path)
        
        messagebox.showinfo("Success", f"Processing complete!\nComplexity Report: {report_file_path}\nSyntax Trees PDF: {output_pdf_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()