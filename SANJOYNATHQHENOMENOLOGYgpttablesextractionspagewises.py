import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
import csv
import os


def extract_and_annotate_pdf(input_pdf, output_csv_dir, annotated_pdf_path, error_log_path, block_report_path):
    try:
        # Open the PDF
        doc = fitz.open(input_pdf)
        error_log = open(error_log_path, 'w', encoding='utf-8')
        block_report = open(block_report_path, 'w', encoding='utf-8')

        block_report.write("Page#\tBlock#\tType\tBBox\tContent\n")
        
        # Iterate through pages
        for page_num in range(len(doc)):
            try:
                page = doc.load_page(page_num)
                csv_file_path = os.path.join(output_csv_dir, f"page_{page_num + 1}.csv")
                
                with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    blocks = page.get_text("dict")["blocks"]

                    for block_num, block in enumerate(blocks, start=1):
                        block_type = block["type"]
                        bbox = block["bbox"]
                        rect = fitz.Rect(bbox)

                        if rect.is_empty or rect.is_infinite:
                            continue

                        # Add block details to the report
                        block_content = ""
                        if block_type == 0:  # Text block
                            for line in block["lines"]:
                                row = []
                                for span in line["spans"]:
                                    text = span["text"].replace(",", "_").replace("\n", "_")
                                    row.append(text)
                                    block_content += f"{text} "
                                csv_writer.writerow(row)

                        block_report.write(f"{page_num + 1}\t{block_num}\t{block_type}\t{bbox}\t{block_content.strip()}\n")

                        # Annotate blocks
                        page.draw_rect(rect, color=(0, 1, 0), width=1, dashes=[3, 3])  # Green dotted box
                        if block_type == 0:
                            center_x, center_y = rect.tl  # Use top-left for circle
                            page.draw_circle((center_x + 5, center_y + 5), 3, color=(1, 0, 0), fill=None, width=1)

                        # Modify text color if text block
                        if block_type == 0:
                            for line in block["lines"]:
                                for span in line["spans"]:
                                    try:
                                        rect = fitz.Rect(span["bbox"])
                                        page.insert_textbox(
                                            rect, span["text"],
                                            color=(1, 0.5, 0.5),  # Blush color
                                            fontsize=span["size"],
                                            fontname="helv",  # Default font fallback
                                            align=0
                                        )
                                    except Exception as font_error:
                                        error_log.write(
                                            f"Font issue on Page {page_num + 1}, Block {block_num}: {font_error}\n"
                                        )
            except Exception as page_error:
                error_log.write(f"Error on page {page_num + 1}: {page_error}\n")
        
        # Save the annotated PDF
        doc.save(annotated_pdf_path)
        error_log.close()
        block_report.close()
        print(f"Annotated PDF saved: {annotated_pdf_path}")
        print(f"Block report saved: {block_report_path}")
        print(f"Error log saved: {error_log_path}")

    except Exception as e:
        print(f"Critical error processing PDF: {e}")


def main():
    root = tk.Tk()
    root.withdraw()
    input_pdf_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    if not input_pdf_path:
        print("No file selected.")
        return

    output_csv_dir = os.path.splitext(input_pdf_path)[0] + "_csv_outputs"
    annotated_pdf_path = os.path.splitext(input_pdf_path)[0] + "_annotated.pdf"
    error_log_path = os.path.splitext(input_pdf_path)[0] + "_errorlog.txt"
    block_report_path = os.path.splitext(input_pdf_path)[0] + "_block_report.txt"

    # Create output directory for CSVs
    os.makedirs(output_csv_dir, exist_ok=True)

    extract_and_annotate_pdf(input_pdf_path, output_csv_dir, annotated_pdf_path, error_log_path, block_report_path)


if __name__ == "__main__":
    main()