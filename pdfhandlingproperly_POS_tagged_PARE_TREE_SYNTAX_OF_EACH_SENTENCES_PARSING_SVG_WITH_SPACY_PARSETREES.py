import tkinter as tk
from tkinter import filedialog, messagebox
import spacy
import os
import fitz  # PyMuPDF
from collections import Counter, defaultdict
import csv
import re

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
    sentences = re.split(r'(?<=[.!?]) +', text)  # Split text into sentences while keeping sentence-ending punctuation
    sentences = [sentence.strip() + "\r\n" for sentence in sentences if sentence.strip()]
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

# Function to create keyword relatedness report for entities found with spaCy
def create_entity_relatedness_report(sentences, nlp):
    report = []
    entity_pairs = Counter()
    
    for sentence in sentences:
        doc = nlp(sentence)
        entities = [re.sub(r'[^a-zA-Z\s]', '', ent.text) for ent in doc.ents]  # Remove non-alphabet characters
        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):
                entity_pairs[(entities[i], entities[j])] += 1
    
    for pair, count in entity_pairs.items():
        report.append(f"{pair}: {count}")
    
    return report

# Function to create keyword relatedness report for tokens found with spaCy pretrained search matcher
def create_token_relatedness_report(sentences, nlp):
    report = []
    token_pairs = Counter()
    
    for sentence in sentences:
        doc = nlp(sentence)
        tokens = [re.sub(r'[^a-zA-Z\s]', '', token.text) for token in doc]  # Remove non-alphabet characters
        for i in range(len(tokens)):
            for j in range(i + 1, len(tokens)):
                token_pairs[(tokens[i], tokens[j])] += 1
    
    for pair, count in token_pairs.items():
        report.append(f"{pair}: {count}")
    
    return report

# Function to create POS category cross tabs report and generate CSV file
def create_pos_category_report(sentences, nlp):
    pos_counter = defaultdict(lambda: defaultdict(int))
    
    pos_categories = [
        'ADJ', 'ADP', 'ADV', 'AUX', 'CONJ', 'CCONJ', 'DET', 'INTJ', 'NOUN', 
        'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X'
    ]
# # ##increase the relatedness counter +222 for these cases    ADJ (Adjective): Describes or modifies a noun. Examples: happy, blue, large.
# # # #increase the relatedness counter +338 for these cases   ADP (Adposition): A preposition or postposition that shows the relationship between a noun and another word. Examples: in, on, at.
# # ##increase the relatedness counter +11 for these cases   ADV (Adverb): Modifies a verb, an adjective, or another adverb. Examples: quickly, very, well.
# # # #increase the relatedness counter +22 for these cases  AUX (Auxiliary verb): Helps the main verb to form a tense, mood, or voice. Examples: is, have, will.
# # ## # #increase the relatedness counter +60 for these cases   CONJ (Conjunction): Connects words, phrases, or clauses. Examples: and, but, or.
# # # CCONJ (Coordinating conjunction): Connects words, phrases, or clauses of equal rank. Examples: and, but, or.
# # #increase the relatedness counter +6 for these cases DET (Determiner): Introduces a noun and specifies it as known or unknown. Examples: the, a, some.
# # # INTJ (Interjection): Expresses a spontaneous feeling or reaction. Examples: oh, wow, ouch.
# # ## # #increase the relatedness counter +3000 for these cases  NOUN (Noun): Names a person, place, thing, or idea. Examples: cat, city, happiness.
# # # NUM (Numeral): Indicates a number or order. Examples: one, two, first.
# # # PART (Particle): A small function word that does not fit into other categories. Examples: not, to (as in "to go").
# # # PRON (Pronoun): Replaces a noun. Examples: he, she, it.
# # #increase the relatedness counter +30 for these cases PROPN (Proper noun): Names a specific person, place, or organization. Examples: John, London, Microsoft.
# # # i dont need relatedness with these PUNCT (Punctuation): Marks used to clarify meaning in written language. Examples: .,!?.
# # # SCONJ (Subordinating conjunction): Connects a dependent clause to a main clause. Examples: because, although, if.
# # ## # # i dont need relatedness with these SYM (Symbol): A symbol or special character. Examples: $, %, &.
# # # VERB (Verb): Describes an action, state, or occurrence. Examples: run, is, seem.
# # # i dont need relatedness with these cases  X (Other): A catch-all category for words that do not fit into the other categories. Examples: foreign words, typos.	
    
    for sentence in sentences:
        doc = nlp(sentence)
        pos_tags = [token.pos_ for token in doc]
        
        for i in range(len(pos_tags)):
            for j in range(len(pos_tags)):
                pos_counter[pos_tags[i]][pos_tags[j]] += 1 ###### i have written the weightages for each of uch cases...
    
    # Create POS category cross tabs report
    report = []
    
    header_row = ['POS Categories'] + pos_categories
    report.append(header_row)
    
    for pos_row in pos_categories:
        row_data = [pos_row] + [pos_counter[pos_row][pos_col] for pos_col in pos_categories]
        report.append(row_data)
    
    return report

# Function to generate SVG files for various linguistic analyses
def generate_svg_files(sentences, nlp):
    svg_files = []
    
    for i, sentence in enumerate(sentences, start=1):
        doc = nlp(sentence)
        
        # Generate SVG for dependency parse tree (Dependency grammar)
        dep_svg = spacy.displacy.render(doc, style="dep", jupyter=False)
        dep_svg_filename = f"sentence_{i}_dep.svg"
        with open(dep_svg_filename, "w", encoding="utf-8") as file:
            file.write(dep_svg)
        
        # Generate SVG for phrase structure tree (Constituent analysis)
        cons_svg = spacy.displacy.render(doc, style="ent", jupyter=False)
        cons_svg_filename = f"sentence_{i}_cons.svg"###why are all these svg files corrupt??? not opening in the browsers???
        with open(cons_svg_filename, "w", encoding="utf-8") as file:
            file.write(cons_svg)
        
        # Generate SVG for Parse tree analysis (using dependency parse tree as placeholder)
        parse_tree_svg_filename = f"sentence_{i}_parse_tree.svg"
        with open(parse_tree_svg_filename, "w", encoding="utf-8") as file:
            file.write(dep_svg) 
        
        svg_files.extend([dep_svg_filename, cons_svg_filename, parse_tree_svg_filename])
    
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
        complexity_report_file_path = os.path.splitext(file_path)[0] + "_complexity_report.txt"
        with open(complexity_report_file_path, "w", encoding="utf-8") as report_file:
            report_file.write("\n".join(complexity_report))
        
        # Create entity relatedness report
        entity_relatedness_report = create_entity_relatedness_report(sentences, nlp)
        
        # Write the entity relatedness report to a new file
        entity_relatedness_report_file_path = os.path.splitext(file_path)[0] + "_entity_relatedness_report.txt"
        with open(entity_relatedness_report_file_path, "w", encoding="utf-8") as report_file:
            report_file.write("\n".join(entity_relatedness_report))
        
        # Create token relatedness report
        token_relatedness_report = create_token_relatedness_report(sentences, nlp)
        
        # Write the token relatedness report to a new file
        token_relatedness_report_file_path = os.path.splitext(file_path)[0] + "_token_relatedness_report.txt"
        with open(token_relatedness_report_file_path, "w", encoding="utf-8") as report_file:
            report_file.write("\n".join(token_relatedness_report))
        
        # Create POS category cross tabs report
        pos_category_report = create_pos_category_report(sentences, nlp)
        
        # Write the POS category cross tabs report to a CSV file
        pos_category_report_file_path = os.path.splitext(file_path)[0] + "_pos_category_report.csv"
        with open(pos_category_report_file_path, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(pos_category_report)### i need the tabulated svg for this csv file also such that we can see the table like objects in html pages
        
        # Generate SVG files for sentence syntax trees and constituent analysis
        svg_files = generate_svg_files(sentences, nlp)
        
        # Combine SVG files into a single PDF
        output_pdf_path = os.path.splitext(file_path)[0] + "_syntax_trees.pdf"
        combine_svgs_to_pdf(svg_files, output_pdf_path)
        
        messagebox.showinfo("Success", f"Processing complete!\nComplexity Report: {complexity_report_file_path}\nEntity Relatedness Report: {entity_relatedness_report_file_path}\nToken Relatedness Report: {token_relatedness_report_file_path}\nPOS Category Report: {pos_category_report_file_path}\nSyntax Trees PDF: {output_pdf_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()