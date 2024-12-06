import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog

def add_annotations_to_pdf(input_pdf_path, output_pdf_path, error_log_path):
    # Open the input PDF
    doc = fitz.open(input_pdf_path)
    
    with open(error_log_path, 'w', encoding='utf-8') as error_log:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # Add green dotted lines around objects and text annotations
            for block in page.get_text("dict")["blocks"]:
                try:
                    bbox = block["bbox"]
                    rect = fitz.Rect(bbox)
                    if rect.is_infinite or rect.is_empty:
                        raise ValueError("Bounding box is infinite or empty")
                    
                    try:
					
					    #i need the red thin circles add_circle_annot(rect)   for every blocks insertion point and wth the blocks BBOX rectangles
                        # Draw green dotted lines around the bounding box
						# i need i want the seperate log for these rect data in a seperate file and also the  Block type: {block['type']}, BBox: {bbox} and the Block content: {block} with the page number wise Block number wise data
						# i need the small font red coloured text at the insertion pont beside the red circle for insertons pont of the  block and with the text (small font to fit n the BBOX ) the text content is lock type: {block['type']}, BBox: {bbox} and the Block content: {block} with the page number wise Block number wse data
                        page.draw_rect(rect, color=(0, 1, 0), width=0.5, dashes=[1, 1])
                    except Exception as e:
                        error_log.write(f"Error drawing rectangle on Page {page_num + 1}: {e}\n")
                        error_log.write(f"Block type: {block['type']}, BBox: {bbox}\n")
                        error_log.write(f"Block content: {block}\n\n")
                    
                    try:
                        # Add text annotation describing the object type
                        if block["type"] == 0:  # Text block
                            annot_text = "Text Object"
                        elif block["type"] == 1:  # Image block
                            annot_text = "Image Object"
                        elif block["type"] == 2:  # Drawing block
                            annot_text = "Drawing Object"
                        else:
                            annot_text = "Unknown Object"
                        #i need the {block} the content text to come on the copied pdf file as green coloured text.
                        annot = page.add_freetext_annot(rect.tl, annot_text, fontsize=8, fontname="helv", color=(0, 1, 0))
                    except Exception as e:
                        error_log.write(f"Error adding annotation on Page {page_num + 1}: {e}\n")
                        error_log.write(f"Block type: {block['type']}, BBox: {bbox}\n")
                        error_log.write(f"Block content: {block}\n\n")
                except Exception as e:
                    error_log.write(f"Error processing block on Page {page_num + 1}: {e}\n")
                    error_log.write(f"Block type: {block['type']}, BBox: {bbox}\n")
                    error_log.write(f"Block content: {block}\n\n")
    
    # Save the output PDF
    try:
        doc.save(output_pdf_path)
    except Exception as e:
        error_log.write(f"Error saving PDF: {e}\n")

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