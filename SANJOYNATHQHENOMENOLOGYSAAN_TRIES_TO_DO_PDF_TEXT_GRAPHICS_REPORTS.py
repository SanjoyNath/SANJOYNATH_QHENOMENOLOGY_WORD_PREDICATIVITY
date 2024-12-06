import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog

def extract_pdf_info(pdf_path):
    doc = fitz.open(pdf_path)
    pdf_info = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_info = {
            "page_number": page_num + 1,
            "orientation": page.rotation,
            "texts": [],
            "images": [],
            "graphics": []
        }

        # Extract text information
        for text in page.get_text("dict")["blocks"]:
            if text["type"] == 0:  # Text block
                for line in text["lines"]:
                    for span in line["spans"]:
                        text_info = {
                            "text_string": span["text"],
                            "coordinates": (span["bbox"][0], span["bbox"][1]),
                            "text_height": span["size"],
                            "text_color": span["color"],
                            "text_font": span["font"],
                            "glyphs": span.get("glyphs", []),
                            "font_name": span.get("font_name", ""),
                            "text_rotations_in_radian": span.get("rotation", 0),
                            "text_rotation_in_degrees": span.get("rotation", 0) * (180 / 3.141592653589793)
                        }
                        page_info["texts"].append(text_info)

        # Extract image information
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_info = {
                "image_location": (img[1], img[2]),
                "image_size": (img[3], img[4]),
                "image_bytes": base_image["image"]
            }
            page_info["images"].append(image_info)

        # Extract graphics information
        for item in page.get_drawings():
            graphics_info = {
                "lines": item.get("lines", []),
                "points": item.get("points", []),
                "circles": item.get("circles", []),
                "graphics_matrix": item.get("matrix", [])
            }
            page_info["graphics"].append(graphics_info)

        pdf_info.append(page_info)

    return pdf_info

def save_pdf_info(pdf_info, output_file):
### i need a seperate report wth all these data in single row for each texts entries in for text in page['texts']: and report that clubbed for all texts with text entry counter in a seperate report like
###i need these  page_number###page_data_details ### seperated ### text_counter###... remaining all data in that report clubbed
###i need these  page_number###page_data_details ### seperated ###  ###graphics_counter###... remaining all data for that graphics  in that report clubbed
###i need these  page_number###page_data_details ### seperated ### image_counter###... remaining all data in that report clubbed
    with open(output_file, 'w', encoding='utf-8') as f:
        for page in pdf_info:
            f.write(f"Page Number: {page['page_number']}\n")
            f.write(f"Orientation: {page['orientation']}\n")
            
            f.write("Texts:\n")
            for text in page['texts']:
                f.write(f"  Text String: {text['text_string']}\n")
                f.write(f"  Coordinates: {text['coordinates']}\n")
                f.write(f"  Text Height: {text['text_height']}\n")
                f.write(f"  Text Color: {text['text_color']}\n")
                f.write(f"  Text Font: {text['text_font']}\n")
                f.write(f"  Glyphs: {text['glyphs']}\n")
                f.write(f"  Font Name: {text['font_name']}\n")
                f.write(f"  Text Rotations (radian): {text['text_rotations_in_radian']}\n")
                f.write(f"  Text Rotations (degrees): {text['text_rotation_in_degrees']}\n")

            f.write("Images:\n")
            for image in page['images']:
                f.write(f"  Image Location: {image['image_location']}\n")
                f.write(f"  Image Size: {image['image_size']}\n")

            f.write("Graphics:\n")
            for graphic in page['graphics']:
                f.write(f"  Lines: {graphic['lines']}\n")
                f.write(f"  Points: {graphic['points']}\n")
                f.write(f"  Circles: {graphic['circles']}\n")
                f.write(f"  Graphics Matrix: {graphic['graphics_matrix']}\n")

def main():
    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    
    if pdf_path:
        pdf_info = extract_pdf_info(pdf_path)
       ### output_file = filedialog.asksaveasfilename(title="Save PDF info as", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
       ###i need output_file = pdf_path + seperate_detailed_reports.txt                instead of this filedialog.asksaveasfilename(title="Save PDF info as", defaultextension=".txt", filetypes=[("Text files", "*.txt")]) 
       ###i need another_output_file = pdf_path + 3shashseperatedrows.txt
	   if output_file:
            save_pdf_info(pdf_info, output_file)
            print(f"PDF information saved to {output_file}")

if __name__ == "__main__":
    main()