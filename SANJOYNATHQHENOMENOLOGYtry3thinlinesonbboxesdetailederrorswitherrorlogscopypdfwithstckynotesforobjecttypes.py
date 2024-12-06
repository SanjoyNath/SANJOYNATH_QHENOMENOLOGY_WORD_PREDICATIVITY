import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog

def add_annotations_to_pdf(input_pdf_path, output_pdf_path, error_log_path):
    # Open the input PDF
    doc = fitz.open(input_pdf_path)
    
    with open(error_log_path, 'w', encoding='utf-8') as error_log:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # Add annotations to each block
            for block_num, block in enumerate(page.get_text("dict")["blocks"]):
                try:
                    bbox = block["bbox"]
                    rect = fitz.Rect(bbox)
                    #if rect.is_infinite or rect.is_empty:
                        #raise ValueError("Bounding box is infinite or empty")
                    if rect.is_infinite or rect.is_empty:
                        continue						
                    
                    # Draw green dotted lines around the bounding box
                    page.draw_rect(rect, color=(0, 1, 0), width=0.5, dashes=[1, 1])
                    
                    # Add red thin circles at the insertion point
                    insertion_point = rect.tl  # Top-left corner as insertion point
                    circle_radius = 5
                    page.draw_circle(insertion_point, circle_radius, color=(1, 0, 0), width=0.5)
                    
                    # Add small font red colored text at the insertion point
                    annot_text = f"Block type: {block['type']}, BBox: {bbox}, Block content: {block}"
                    page.insert_text(insertion_point + (circle_radius + 2, -circle_radius - 2), annot_text, fontsize=6, color=(1, 0, 0))
                    
                    # Log the block data in the error log file
                    error_log.write(f"Page {page_num + 1}, Block {block_num + 1}\n")
                    error_log.write(f"Block type: {block['type']}, BBox: {bbox}\n")
                    error_log.write(f"Block content: {block}\n\n")
                    
                except Exception as e:
                    error_log.write(f"Error processing block on Page {page_num + 1}, Block {block_num + 1}: {e}\n")
                    error_log.write(f"Block type: {block['type']}, BBox: {bbox}\n")
                    error_log.write(f"Block content: {block}\n\n")
    
    # Save the output PDF
    try:
        doc.save(output_pdf_path)
    except Exception as e:
        with open(error_log_path, 'a', encoding='utf-8') as error_log:
            error_log.write(f"Error saving PDF: {e}\n")

def main():
    root = tk.Tk()
    root.withdraw()
    
    # Open file dialog to select PDF file
    input_pdf_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    
    if input_pdf_path:
        output_pdf_path = input_pdf_path + "___annotated.pdf"
        error_log_path = input_pdf_path + "___errorlog.txt"
        if output_pdf_path:
            add_annotations_to_pdf(input_pdf_path, output_pdf_path, error_log_path)
            print(f"Annotated PDF saved as {output_pdf_path}")
            print(f"Error log saved as {error_log_path}")

if __name__ == "__main__":
    main()