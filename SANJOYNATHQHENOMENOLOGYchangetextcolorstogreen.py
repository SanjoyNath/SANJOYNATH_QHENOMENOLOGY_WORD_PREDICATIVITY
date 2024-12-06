import fitz  # PyMuPDF

import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog



def change_text_color_to_green(input_pdf_path, output_pdf_path, error_log_path):
    # Open the input PDF
    doc = fitz.open(input_pdf_path)
    
    with open(error_log_path, 'w', encoding='utf-8') as error_log:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # Change text color to green for each block
            for block_num, block in enumerate(page.get_text("dict")["blocks"]):
                try:
                    if block["type"] == 0:  # Text block
                        for line in block["lines"]:
                            for span in line["spans"]:
                                span["color"] = (0, 1, 0)  # Set color to green (RGB: 0, 255, 0)
                                checkinsert=page.insert_text((span["bbox"][0], span["bbox"][1]), span["text"], fontsize=span["size"], color=(0, 1, 0), fontname=span["font"])
                    
                    # Log the block data in the error log file
                    error_log.write(f"Page {page_num + 1}, Block {block_num + 1}\n")
                    error_log.write(f"Block type: {block['type']}, BBox: {block['bbox']}\n")
                    error_log.write(f"Block content: {block}\n\n")
                    
                except Exception as e:
                    error_log.write(f"Error processing block on Page {page_num + 1}, Block {block_num + 1}: {e}\n")
                    error_log.write(f"Block type: {block['type']}, BBox: {block['bbox']}\n")
                    error_log.write(f"Block content: {block}\n\n")
    
    # Save the output PDF
    try:
        doc.save(output_pdf_path)
    except Exception as e:
        with open(error_log_path, 'a', encoding='utf-8') as error_log:
            error_log.write(f"Error saving PDF: {e}\n")

# # # # Example usage
# # # input_pdf_path = "input.pdf"
# # # output_pdf_path = "output_green_text.pdf"
# # # error_log_path = "error_log.txt"

# # # change_text_color_to_green(input_pdf_path, output_pdf_path, error_log_path)


def main():
    root = tk.Tk()
    root.withdraw()
    
    # Open file dialog to select PDF file
    input_pdf_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    
    if input_pdf_path:
        output_pdf_path = input_pdf_path + "___annotated.pdf"
        error_log_path = input_pdf_path + "___errorlog.txt"
        if output_pdf_path:
            ###add_annotations_to_pdf(input_pdf_path, output_pdf_path, error_log_path)
            change_text_color_to_green(input_pdf_path, output_pdf_path, error_log_path)
            print(f"Annotated PDF saved as {output_pdf_path}")
            print(f"Error log saved as {error_log_path}")
			
			
			
if __name__ == "__main__":
    main()			