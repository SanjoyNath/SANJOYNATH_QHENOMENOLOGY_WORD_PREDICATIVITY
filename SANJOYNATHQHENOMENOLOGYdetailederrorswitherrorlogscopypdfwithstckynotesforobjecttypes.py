import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog

def add_annotations_to_pdf(input_pdf_path, output_pdf_path, error_log_path):
    # Open the input PDF
    doc = fitz.open(input_pdf_path)
    
    with open(error_log_path, 'w') as error_log:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # Add circles around objects
            for block in page.get_text("dict")["blocks"]:
                try:
                    if block["type"] == 0:  # Text block
                        for line in block["lines"]:
                            for span in line["spans"]:
                                bbox = span["bbox"]
                                rect = fitz.Rect(bbox)
                                if rect.is_infinite or rect.is_empty:
                                    raise ValueError("Bounding box is infinite or empty")
                                page.draw_circle(rect.tl, rect.width / 2, color=(1, 0, 0), fill=None, width=1)
                                annot = page.add_freetext_annot(rect.tl, "Text Object", fontsize=8, fontname="helv")
                                annot.set_colors(stroke=(0, 0, 1))
                    elif block["type"] == 1:  # Image block
                        bbox = block["bbox"]
                        rect = fitz.Rect(bbox)
                        if rect.is_infinite or rect.is_empty:
                            raise ValueError("Bounding box is infinite or empty")
                        page.draw_circle(rect.tl, rect.width / 2, color=(0, 1, 0), fill=None, width=1)
                        annot = page.add_freetext_annot(rect.tl, "Image Object", fontsize=8, fontname="helv")
                        annot.set_colors(stroke=(0, 0, 1))
                    elif block["type"] == 2:  # Drawing block
                        bbox = block["bbox"]
                        rect = fitz.Rect(bbox)
                        if rect.is_infinite or rect.is_empty:
                            raise ValueError("Bounding box is infinite or empty")
                        page.draw_circle(rect.tl, rect.width / 2, color=(0, 0, 1), fill=None, width=1)
                        annot = page.add_freetext_annot(rect.tl, "Drawing Object", fontsize=8, fontname="helv")
                        annot.set_colors(stroke=(0, 0, 1))
                except Exception as e:
                    error_log.write(f"Error processing block on Page {page_num + 1}: {e}\n")
                    error_log.write(f"Block type: {block['type']}, BBox: {bbox}\n")
                    error_log.write(f"Block content: {block}\n\n")
    
    # Save the output PDF
    doc.save(output_pdf_path)

def main():
    root = tk.Tk()
    root.withdraw()
    
    # Open file dialog to select PDF file
    input_pdf_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    
    if input_pdf_path:
        output_pdf_path = input_pdf_path + "___annotated_saan_done.pdf"
        error_log_path = input_pdf_path + "___errorlog_to_annotates.txt"
        if output_pdf_path:
            add_annotations_to_pdf(input_pdf_path, output_pdf_path, error_log_path)
            print(f"Annotated PDF saved as {output_pdf_path}")
            print(f"Error log saved as {error_log_path}")

if __name__ == "__main__":
    main()