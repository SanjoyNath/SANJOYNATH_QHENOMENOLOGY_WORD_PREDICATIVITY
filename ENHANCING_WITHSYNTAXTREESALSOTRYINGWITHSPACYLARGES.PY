import tkinter as tk
from tkinter import filedialog, messagebox
import spacy
import os
import fitz  # PyMuPDF
from collections import Counter

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

# Function to create keyword relatedness report
def create_keyword_relatedness_report(sentences, nlp):
    report = []
    keyword_counter = Counter()
    for sentence in sentences:
        doc = nlp(sentence)
        entities = [ent.text for ent in doc.ents]
        keyword_counter.update(entities)
    
    for keyword, count in keyword_counter.items():
        report.append(f"{keyword}: {count}")
    
    return report

# Function to create POS category cross tabs report
def create_pos_category_report(sentences, nlp):
    report = []
    pos_counter = Counter()
    for sentence in sentences:
        doc = nlp(sentence)
        pos_tags = [token.pos_ for token in doc]
        pos_counter.update(pos_tags)
    
    for pos, count in pos_counter.items():
        report.append(f"{pos}: {count}")
    
    return report

# Function to generate SVG files for sentence syntax trees
def generate_svg_files(sentences, nlp):
    svg_files = []
    for i, sentence in enumerate(sentences, start=1):
        doc = nlp(sentence)
        
        # Generate SVG for dependency parse tree
        dep_svg = spacy.displacy.render(doc, style="dep", jupyter=False)
        dep_svg_filename = f"sentence_{i}_dep.svg"
        with open(dep_svg_filename, "w", encoding="utf-8") as file:
            file.write(dep_svg)
        
        # Generate SVG for phrase structure tree (constituent analysis)
        cons_svg = spacy.displacy.render(doc, style="ent", jupyter=False)
        cons_svg_filename = f"sentence_{i}_cons.svg"
        with open(cons_svg_filename, "w", encoding="utf-8") as file:
            file.write(cons_svg)
        
        svg_files.extend([dep_svg_filename, cons_svg_filename])
    
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
        
        # Create keyword relatedness report
        keyword_relatedness_report = create_keyword_relatedness_report(sentences, nlp)
        
        # Write the keyword relatedness report to a new file
        keyword_relatedness_report_file_path = os.path.splitext(file_path)[0] + "_keyword_relatedness_report.txt"
        with open(keyword_relatedness_report_file_path, "w", encoding="utf-8") as report_file:
            report_file.write("\n".join(keyword_relatedness_report))
        
        # Create POS category cross tabs report
        pos_category_report = create_pos_category_report(sentences, nlp)
        
        # Write the POS category cross tabs report to a new file
        pos_category_report_file_path = os.path.splitext(file_path)[0] + "_pos_category_report.txt"
        with open(pos_category_report_file_path, "w", encoding="utf-8") as report_file:
            report_file.write("\n".join(pos_category_report))
        
        # Generate SVG files for sentence syntax trees and constituent analysis
        svg_files = generate_svg_files(sentences, nlp)
        
        # Combine SVG files into a single PDF
        output_pdf_path = os.path.splitext(file_path)[0] + "_syntax_trees.pdf"
        combine_svgs_to_pdf(svg_files, output_pdf_path)
        
        messagebox.showinfo("Success", f"Processing complete!\nComplexity Report: {report_file_path}\nKeyword Relatedness Report: {keyword_relatedness_report_file_path}\nPOS Category Report: {pos_category_report_file_path}\nSyntax Trees PDF: {output_pdf_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()
	
	
	
	
	
	
	
	

# # # D:\SAANS_OFFLINES_GPT_SENTENCES_ANALYSERS>pip install svgwrite
# # # Defaulting to user installation because normal site-packages is not writeable
# # # Collecting svgwrite
  # # # Downloading svgwrite-1.4.3-py3-none-any.whl.metadata (8.8 kB)
# # # Downloading svgwrite-1.4.3-py3-none-any.whl (67 kB)
# # # Installing collected packages: svgwrite
# # # Successfully installed svgwrite-1.4.3	