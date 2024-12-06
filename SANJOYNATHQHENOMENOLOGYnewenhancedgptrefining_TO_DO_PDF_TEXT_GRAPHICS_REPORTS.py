import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog


import fitz  # PyMuPDF





import fitz  # PyMuPDF


import fitz  # PyMuPDF

def extract_pdf_info(pdf_path):
    doc = fitz.open(pdf_path)
    pdf_info = []
    font_wise_report = {}
    height_wise_report = {}

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        width, height = page.rect.width, page.rect.height
        orientation = "Landscape" if width > height else "Portrait"
        page_info = {
            "page_number": page_num + 1,
            "orientation": orientation,
            "page_width": width,
            "page_height": height,
            "texts": [],
            "images": [],
            "graphics": []
        }

        text_counter = 0  # Initialize text counter for each page

        # Extract text information
        for block in page.get_text("dict")["blocks"]:
            if block["type"] == 0:  # Text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        # Calculate percentage coordinates and bbox area percentage
                        x_percent = (span["bbox"][0] / width) * 100
                        y_percent = (span["bbox"][1] / height) * 100
                        bbox_area = (span["bbox"][2] - span["bbox"][0]) * (span["bbox"][3] - span["bbox"][1])
                        bbox_area_percent = (bbox_area / (width * height)) * 100

                        text_counter += 1  # Increment the text counter
                        text_info = {
                            "text_string": span["text"],
                            "coordinates": (span["bbox"][0], span["bbox"][1]),
                            "coordinates_percent": (x_percent, y_percent),
                            "bbox_area_percent": bbox_area_percent,
                            "text_height": span["size"],
                            "text_color": span["color"],
                            "text_font": span["font"],
                            "glyphs": span.get("glyphs", []),
                            "font_name": span.get("font_name", ""),
                            "text_rotations_in_radian": span.get("rotation", 0),
                            "text_rotation_in_degrees": span.get("rotation", 0) * (180 / 3.141592653589793)
                        }
                        page_info["texts"].append(text_info)

                        # Update font-wise report
                        font_key = (span["font"], span["color"])
                        if font_key not in font_wise_report:
                            font_wise_report[font_key] = []
                        font_wise_report[font_key].append({
                            "page": page_num + 1,
                            "text": span["text"],
                            "bbox_area_percent": bbox_area_percent,
                            "coordinates_percent": (x_percent, y_percent)
                        })

                        # Update height-wise report
                        height_key = round(span["size"], 1)  # Group by rounded text height
                        if height_key not in height_wise_report:
                            height_wise_report[height_key] = []
                        height_wise_report[height_key].append({
                            "page": page_num + 1,
                            "text": span["text"],
                            "text_font": span["font"],
                            "text_color": span["color"]
                        })

        # Extract image information
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_info = {
                "image_location": (img[1], img[2]),
                "image_size": (img[3], img[4]),
                "image_bytes": base_image["image"],
                "image_ext": base_image["ext"],
                "image_colorspace": base_image["colorspace"]
            }
            page_info["images"].append(image_info)

        # Extract graphics information
        graphics_data = page.get_drawings()
        if graphics_data:
            for graphic in graphics_data:
                graphics_info = {
                    "lines": graphic.get("lines", []),
                    "points": graphic.get("points", []),
                    "circles": graphic.get("circles", []),
                    "rectangles": graphic.get("rectangles", []),
                    "polygons": graphic.get("polygons", []),
                    "graphics_matrix": graphic.get("matrix", [])
                }
                page_info["graphics"].append(graphics_info)
        else:
            print(f"No graphics found on Page {page_num + 1}")

        # Fallback for alternate vector representation
        if not page_info["graphics"]:
            page_info["graphics"].append({
                "message": "No explicit graphics detected; check PDF structure."
            })

        pdf_info.append(page_info)

    return pdf_info, font_wise_report, height_wise_report


# # # def extract_pdf_info(pdf_path):
    # # # doc = fitz.open(pdf_path)
    # # # pdf_info = []
    # # # font_wise_report = {}
    # # # height_wise_report = {}

    # # # for page_num in range(len(doc)):
        # # # page = doc.load_page(page_num)
        # # # width, height = page.rect.width, page.rect.height
        # # # orientation = "Landscape" if width > height else "Portrait"
        # # # page_info = {
            # # # "page_number": page_num + 1,
            # # # "orientation": orientation,
            # # # "page_width": width,
            # # # "page_height": height,
            # # # "texts": [],
            # # # "images": [],
            # # # "graphics": []
        # # # }

        # # # # Extract text information
        # # # for block in page.get_text("dict")["blocks"]:
            # # # if block["type"] == 0:  # Text block
                # # # for line in block["lines"]:
                    # # # for span in line["spans"]:
                        # # # # Calculate percentage coordinates and bbox area percentage
                        # # # x_percent = (span["bbox"][0] / width) * 100
                        # # # y_percent = (span["bbox"][1] / height) * 100
                        # # # bbox_area = (span["bbox"][2] - span["bbox"][0]) * (span["bbox"][3] - span["bbox"][1])
                        # # # bbox_area_percent = (bbox_area / (width * height)) * 100

                        # # # text_info = {
                            # # # "text_string": span["text"],
                            # # # "coordinates": (span["bbox"][0], span["bbox"][1]),
                            # # # "coordinates_percent": (x_percent, y_percent),
                            # # # "bbox_area_percent": bbox_area_percent,
                            # # # "text_height": span["size"],
                            # # # "text_color": span["color"],
                            # # # "text_font": span["font"],
                            # # # "glyphs": span.get("glyphs", []),
                            # # # "font_name": span.get("font_name", ""),
                            # # # "text_rotations_in_radian": span.get("rotation", 0),
                            # # # "text_rotation_in_degrees": span.get("rotation", 0) * (180 / 3.141592653589793)
                        # # # }
                        # # # page_info["texts"].append(text_info)

                        # # # # Update font-wise report
                        # # # font_key = (span["font"], span["color"])
                        # # # if font_key not in font_wise_report:
                            # # # font_wise_report[font_key] = []
                        # # # font_wise_report[font_key].append({
                            # # # "page": page_num + 1,
                            # # # "text": span["text"],
                            # # # "bbox_area_percent": bbox_area_percent,
                            # # # "coordinates_percent": (x_percent, y_percent)
                        # # # })

                        # # # # Update height-wise report
                        # # # height_key = round(span["size"], 1)  # Group by rounded text height
                        # # # if height_key not in height_wise_report:
                            # # # height_wise_report[height_key] = []
                        # # # height_wise_report[height_key].append({
                            # # # "page": page_num + 1,
                            # # # "text": span["text"],
                            # # # "text_font": span["font"],
                            # # # "text_color": span["color"]
                        # # # })

        # # # # Extract image information
        # # # for img in page.get_images(full=True):
            # # # xref = img[0]
            # # # base_image = doc.extract_image(xref)
            # # # image_info = {
                # # # "image_location": (img[1], img[2]),
                # # # "image_size": (img[3], img[4]),
                # # # "image_bytes": base_image["image"],
                # # # "image_ext": base_image["ext"],
                # # # "image_colorspace": base_image["colorspace"]
            # # # }
            # # # page_info["images"].append(image_info)

        # # # # Extract graphics information
        # # # graphics_data = page.get_drawings()
        # # # if graphics_data:
            # # # for graphic in graphics_data:
                # # # graphics_info = {
                    # # # "lines": graphic.get("lines", []),
                    # # # "points": graphic.get("points", []),
                    # # # "circles": graphic.get("circles", []),
                    # # # "rectangles": graphic.get("rectangles", []),
                    # # # "polygons": graphic.get("polygons", []),
                    # # # "graphics_matrix": graphic.get("matrix", [])
                # # # }
                # # # page_info["graphics"].append(graphics_info)
        # # # else:
            # # # print(f"No graphics found on Page {page_num + 1}")

        # # # # Fallback for alternate vector representation
        # # # if not page_info["graphics"]:
            # # # page_info["graphics"].append({
                # # # "message": "No explicit graphics detected; check PDF structure."
            # # # })

        # # # pdf_info.append(page_info)

    # # # return pdf_info, font_wise_report, height_wise_report

def save_enhanced_reports(pdf_info, font_wise_report, height_wise_report, output_file, detailed_report_file, font_report_file, height_report_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for page in pdf_info:
            f.write(f"Page Number: {page['page_number']}\n")
            f.write(f"Orientation: {page['orientation']}\n")
            f.write(f"Page Width: {page['page_width']}\n")
            f.write(f"Page Height: {page['page_height']}\n")

            text_counter = 0  # Initialize text counter for each page
            f.write("Texts:\n")
            for text in page['texts']:
                text_counter += 1
                f.write(f"  Text Counter: {text_counter}\n")
                f.write(f"  Text String: {text['text_string']}\n")
                f.write(f"  Coordinates: {text['coordinates']}\n")
                f.write(f"  Coordinates (%): {text['coordinates_percent']}\n")
                f.write(f"  BBox Area (%): {text['bbox_area_percent']}\n")
                f.write(f"  Text Height: {text['text_height']}\n")
                f.write(f"  Text Color: {text['text_color']}\n")
                f.write(f"  Text Font: {text['text_font']}\n")
                f.write(f"  Glyphs: {text['glyphs']}\n")
                f.write(f"  Font Name: {text['font_name']}\n")
                f.write(f"  Text Rotations (radian): {text['text_rotations_in_radian']}\n")
                f.write(f"  Text Rotations (degrees): {text['text_rotation_in_degrees']}\n")

    # Font-wise report
    with open(font_report_file, 'w', encoding='utf-8') as fr:
        fr.write("Font-Wise Content Report\n")
        for font_key, entries in font_wise_report.items():
            fr.write(f"Font: {font_key[0]}, Color: {font_key[1]}\n")
            for entry in entries:
                fr.write(f"  Page: {entry['page']} | Text: {entry['text']} | BBox Area (%): {entry['bbox_area_percent']} | Coordinates (%): {entry['coordinates_percent']}\n")

    # Height-wise report
    with open(height_report_file, 'w', encoding='utf-8') as hr:
        hr.write("Text Height Pivot Report\n")
        for height_key, entries in height_wise_report.items():
            hr.write(f"Text Height: {height_key}\n")
            for entry in entries:
                hr.write(f"  Page: {entry['page']} | Text: {entry['text']} | Font: {entry['text_font']} | Color: {entry['text_color']}\n")

# # # def extract_pdf_info(pdf_path):
    # # # doc = fitz.open(pdf_path)
    # # # pdf_info = []
    # # # font_wise_report = {}
    # # # height_wise_report = {}

    # # # for page_num in range(len(doc)):
        # # # page = doc.load_page(page_num)
        # # # width, height = page.rect.width, page.rect.height
        # # # orientation = "Landscape" if width > height else "Portrait"
        # # # page_info = {
            # # # "page_number": page_num + 1,
            # # # "orientation": orientation,
            # # # "page_width": width,
            # # # "page_height": height,
            # # # "texts": [],
            # # # "images": [],
            # # # "graphics": []
        # # # }

        # # # # Extract text information
        # # # for block in page.get_text("dict")["blocks"]:
            # # # if block["type"] == 0:  # Text block
                # # # for line in block["lines"]:
                    # # # for span in line["spans"]:
                        # # # # Calculate percentage coordinates and bbox area percentage
                        # # # x_percent = (span["bbox"][0] / width) * 100
                        # # # y_percent = (span["bbox"][1] / height) * 100
                        # # # bbox_area = (span["bbox"][2] - span["bbox"][0]) * (span["bbox"][3] - span["bbox"][1])
                        # # # bbox_area_percent = (bbox_area / (width * height)) * 100

                        # # # text_info = {
                            # # # "text_string": span["text"],
                            # # # "coordinates_percent": (x_percent, y_percent),
                            # # # "bbox_area_percent": bbox_area_percent,
                            # # # "text_height": span["size"],
                            # # # "text_color": span["color"],
                            # # # "text_font": span["font"],
                            # # # "glyphs": span.get("glyphs", []),
                            # # # "font_name": span.get("font_name", ""),
                            # # # "text_rotations_in_radian": span.get("rotation", 0),
                            # # # "text_rotation_in_degrees": span.get("rotation", 0) * (180 / 3.141592653589793)
                        # # # }
                        # # # page_info["texts"].append(text_info)

                        # # # # Update font-wise report
                        # # # font_key = (span["font"], span["color"])
                        # # # if font_key not in font_wise_report:
                            # # # font_wise_report[font_key] = []
                        # # # font_wise_report[font_key].append({
                            # # # "page": page_num + 1,
                            # # # "text": span["text"],
                            # # # "bbox_area_percent": bbox_area_percent,
                            # # # "coordinates_percent": (x_percent, y_percent)
                        # # # })

                        # # # # Update height-wise report
                        # # # height_key = round(span["size"], 1)  # Group by rounded text height
                        # # # if height_key not in height_wise_report:
                            # # # height_wise_report[height_key] = []
                        # # # height_wise_report[height_key].append({
                            # # # "page": page_num + 1,
                            # # # "text": span["text"],
                            # # # "text_font": span["font"],
                            # # # "text_color": span["color"]
                        # # # })

        # # # # Extract image information
        # # # for img in page.get_images(full=True):
            # # # xref = img[0]
            # # # base_image = doc.extract_image(xref)
            # # # image_info = {
                # # # "image_location": (img[1], img[2]),
                # # # "image_size": (img[3], img[4]),
                # # # "image_bytes": base_image["image"],
                # # # "image_ext": base_image["ext"],
                # # # "image_colorspace": base_image["colorspace"]
            # # # }
            # # # page_info["images"].append(image_info)

        # # # # Extract graphics information
        # # # graphics_data = page.get_drawings()
        # # # if graphics_data:
            # # # for graphic in graphics_data:
                # # # graphics_info = {
                    # # # "lines": graphic.get("lines", []),
                    # # # "points": graphic.get("points", []),
                    # # # "circles": graphic.get("circles", []),
                    # # # "rectangles": graphic.get("rectangles", []),
                    # # # "polygons": graphic.get("polygons", []),
                    # # # "graphics_matrix": graphic.get("matrix", [])
                # # # }
                # # # page_info["graphics"].append(graphics_info)
        # # # else:
            # # # print(f"No graphics found on Page {page_num + 1}")

        # # # # Fallback for alternate vector representation
        # # # if not page_info["graphics"]:
            # # # page_info["graphics"].append({
                # # # "message": "No explicit graphics detected; check PDF structure."
            # # # })

        # # # pdf_info.append(page_info)

    # # # return pdf_info, font_wise_report, height_wise_report

# # # def extract_pdf_info(pdf_path):
    # # # doc = fitz.open(pdf_path)
    # # # pdf_info = []
    # # # for page_num in range(len(doc)):
        # # # page = doc.load_page(page_num)
        # # # width, height = page.rect.width, page.rect.height
        # # # orientation = "Landscape" if width > height else "Portrait"
        # # # page_info = {
            # # # "page_number": page_num + 1,
            # # # "orientation": orientation,
            # # # "page_width": width,
            # # # "page_height": height,
            # # # "texts": [],
            # # # "images": [],
            # # # "graphics": []
        # # # }
        # # # # Extract text information
        # # # for block in page.get_text("dict")["blocks"]:
            # # # if block["type"] == 0:  # Text block
                # # # for line in block["lines"]:
                    # # # for span in line["spans"]:
                        # # # text_info = {
                            # # # "text_string": span["text"],
                            # # # "coordinates": (span["bbox"][0], span["bbox"][1]),
                            # # # "text_height": span["size"],
                            # # # "text_color": span["color"],
                            # # # "text_font": span["font"],
                            # # # "glyphs": span.get("glyphs", []),
                            # # # "font_name": span.get("font_name", ""),
                            # # # "text_rotations_in_radian": span.get("rotation", 0),
                            # # # "text_rotation_in_degrees": span.get("rotation", 0) * (180 / 3.141592653589793)
                        # # # }
                        # # # page_info["texts"].append(text_info)
        # # # # Extract image information
        # # # for img in page.get_images(full=True):
            # # # xref = img[0]
            # # # base_image = doc.extract_image(xref)
            # # # image_info = {
                # # # "image_location": (img[1], img[2]),
                # # # "image_size": (img[3], img[4]),
                # # # "image_bytes": base_image["image"],
                # # # "image_ext": base_image["ext"],
                # # # "image_colorspace": base_image["colorspace"]
            # # # }
            # # # page_info["images"].append(image_info)
        # # # # Extract graphics information
        # # # graphics_data = page.get_drawings()
        # # # if graphics_data:
            # # # for graphic in graphics_data:
                # # # graphics_info = {
                    # # # "lines": graphic.get("lines", []),
                    # # # "points": graphic.get("points", []),
                    # # # "circles": graphic.get("circles", []),
                    # # # "rectangles": graphic.get("rectangles", []),
                    # # # "polygons": graphic.get("polygons", []),
                    # # # "graphics_matrix": graphic.get("matrix", [])
                # # # }
                # # # page_info["graphics"].append(graphics_info)
        # # # else:
            # # # print(f"No graphics found on Page {page_num + 1}")
        # # # # Fallback for alternate vector representation
        # # # if not page_info["graphics"]:
            # # # page_info["graphics"].append({
                # # # "message": "No explicit graphics detected; check PDF structure."
            # # # })
        # # # pdf_info.append(page_info)
    # # # return pdf_info
# # # def extract_pdf_info(pdf_path):
    # # # doc = fitz.open(pdf_path)
    # # # pdf_info = []
    # # # for page_num in range(len(doc)):
        # # # page = doc.load_page(page_num)
        # # # width, height = page.rect.width, page.rect.height
        # # # orientation = "Landscape" if width > height else "Portrait"
        # # # page_info = {
            # # # "page_number": page_num + 1,
            # # # "orientation": orientation,
            # # # "page_width": width,
            # # # "page_height": height,
            # # # "texts": [],
            # # # "images": [],
            # # # "graphics": []
        # # # }
        # # # # Extract text information
        # # # for block in page.get_text("dict")["blocks"]:
            # # # if block["type"] == 0:  # Text block
                # # # for line in block["lines"]:
                    # # # for span in line["spans"]:
                        # # # text_info = {
                            # # # "text_string": span["text"],
                            # # # "coordinates": (span["bbox"][0], span["bbox"][1]),
                            # # # "text_height": span["size"],
                            # # # "text_color": span["color"],
                            # # # "text_font": span["font"],
                            # # # "glyphs": span.get("glyphs", []),
                            # # # "font_name": span.get("font_name", ""),
                            # # # "text_rotations_in_radian": span.get("rotation", 0),
                            # # # "text_rotation_in_degrees": span.get("rotation", 0) * (180 / 3.141592653589793)
                        # # # }
                        # # # page_info["texts"].append(text_info)
        # # # # Extract image information
        # # # for img in page.get_images(full=True):
            # # # xref = img[0]
            # # # base_image = doc.extract_image(xref)
            # # # image_info = {
                # # # "image_location": (img[1], img[2]),
                # # # "image_size": (img[3], img[4]),
                # # # "image_bytes": base_image["image"],
                # # # "image_ext": base_image["ext"],
                # # # "image_colorspace": base_image["colorspace"]
            # # # }
            # # # page_info["images"].append(image_info)
        # # # # Extract graphics information
        # # # graphics_data = page.get_drawings()
        # # # if graphics_data:
            # # # for graphic in graphics_data:
                # # # graphics_info = {
                    # # # "lines": graphic.get("lines", []),
                    # # # "points": graphic.get("points", []),
                    # # # "circles": graphic.get("circles", []),
                    # # # "rectangles": graphic.get("rectangles", []),
                    # # # "polygons": graphic.get("polygons", []),
                    # # # "graphics_matrix": graphic.get("matrix", [])
                # # # }
                # # # page_info["graphics"].append(graphics_info)
        # # # else:
            # # # print(f"No graphics found on Page {page_num + 1}")
        # # # # Fallback for alternate vector representation
        # # # if not page_info["graphics"]:
            # # # page_info["graphics"].append({
                # # # "message": "No explicit graphics detected; check PDF structure."
            # # # })
        # # # pdf_info.append(page_info)
    # # # return pdf_info
# # # def extract_pdf_info(pdf_path):
    # # # doc = fitz.open(pdf_path)
    # # # pdf_info = []
    # # # for page_num in range(len(doc)):
        # # # page = doc.load_page(page_num)
        # # # width, height = page.rect.width, page.rect.height
        # # # orientation = "Landscape" if width > height else "Portrait"
        # # # page_info = {
            # # # "page_number": page_num + 1,
            # # # "orientation": orientation,
            # # # "page_width": width,
            # # # "page_height": height,
            # # # "texts": [],
            # # # "images": [],
            # # # "graphics": []
        # # # }
        # # # # Extract text information
        # # # for block in page.get_text("dict")["blocks"]:
            # # # if block["type"] == 0:  # Text block
                # # # for line in block["lines"]:
                    # # # for span in line["spans"]:
                        # # # text_info = {
                            # # # "text_string": span["text"],
                            # # # "coordinates": (span["bbox"][0], span["bbox"][1]),
                            # # # "text_height": span["size"],
                            # # # "text_color": span["color"],
                            # # # "text_font": span["font"],
                            # # # "glyphs": span.get("glyphs", []),
                            # # # "font_name": span.get("font_name", ""),
                            # # # "text_rotations_in_radian": span.get("rotation", 0),
                            # # # "text_rotation_in_degrees": span.get("rotation", 0) * (180 / 3.141592653589793)
                        # # # }
                        # # # page_info["texts"].append(text_info)
        # # # # Extract image information
        # # # for img in page.get_images(full=True):
            # # # xref = img[0]
            # # # base_image = doc.extract_image(xref)
            # # # image_info = {
                # # # "image_location": (img[1], img[2]),
                # # # "image_size": (img[3], img[4]),
                # # # "image_bytes": base_image["image"],
                # # # "image_ext": base_image["ext"],
                # # # "image_colorspace": base_image["colorspace"]
            # # # }
            # # # page_info["images"].append(image_info)
        # # # # Extract graphics information
        # # # for item in page.get_drawings():
            # # # graphics_info = {
                # # # "lines": item.get("lines", []),
                # # # "points": item.get("points", []),
                # # # "circles": item.get("circles", []),
                # # # "rectangles": item.get("rectangles", []),
                # # # "polygons": item.get("polygons", []),
                # # # "graphics_matrix": item.get("matrix", [])
            # # # }
            # # # page_info["graphics"].append(graphics_info)
        # # # pdf_info.append(page_info)
    # # # return pdf_info
# # # def save_pdf_info(pdf_info, output_file, detailed_report_file):
    # # # with open(output_file, 'w', encoding='utf-8') as f:
        # # # for page in pdf_info:
            # # # f.write(f"Page Number: {page['page_number']}\n")
            # # # f.write(f"Orientation: {page['orientation']}\n")
            # # # f.write(f"Page Width: {page['page_width']}\n")
            # # # f.write(f"Page Height: {page['page_height']}\n")
            # # # f.write("Texts:\n")
            # # # for text in page['texts']:
                # # # f.write(f"  Text String: {text['text_string']}\n")
                # # # f.write(f"  Coordinates: {text['coordinates']}\n")
                # # # f.write(f"  Text Height: {text['text_height']}\n")
                # # # f.write(f"  Text Color: {text['text_color']}\n")
                # # # f.write(f"  Text Font: {text['text_font']}\n")
                # # # f.write(f"  Glyphs: {text['glyphs']}\n")
                # # # f.write(f"  Font Name: {text['font_name']}\n")
                # # # f.write(f"  Text Rotations (radian): {text['text_rotations_in_radian']}\n")
                # # # f.write(f"  Text Rotations (degrees): {text['text_rotation_in_degrees']}\n")
            # # # f.write("Images:\n")
            # # # for image in page['images']:
                # # # f.write(f"  Image Location: {image['image_location']}\n")
                # # # f.write(f"  Image Size: {image['image_size']}\n")
                # # # f.write(f"  Image Extension: {image['image_ext']}\n")
                # # # f.write(f"  Image Colorspace: {image['image_colorspace']}\n")
            # # # f.write("Graphics:\n")
            # # # for graphic in page['graphics']:
                # # # f.write(f"  Lines: {graphic['lines']}\n")
                # # # f.write(f"  Points: {graphic['points']}\n")
                # # # f.write(f"  Circles: {graphic['circles']}\n")
                # # # f.write(f"  Rectangles: {graphic['rectangles']}\n")
                # # # f.write(f"  Polygons: {graphic['polygons']}\n")
                # # # f.write(f"  Graphics Matrix: {graphic['graphics_matrix']}\n")
    # # # with open(detailed_report_file, 'w', encoding='utf-8') as detailed_f:
        # # # for page in pdf_info:
            # # # page_details = f"Page {page['page_number']} | Orientation: {page['orientation']}"
            # # # for text in page['texts']:
                # # # detailed_f.write(f"{page_details} | Text: {text['text_string']} | Coordinates: {text['coordinates']} | Rotation (deg): {text['text_rotation_in_degrees']}\n")
            # # # for image in page['images']:
                # # # detailed_f.write(f"{page_details} | Image at: {image['image_location']} | Size: {image['image_size']}\n")
            # # # for graphic in page['graphics']:
                # # # detailed_f.write(f"{page_details} | Graphics: {graphic}\n")
def save_pdf_info(pdf_info, output_file, detailed_report_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for page in pdf_info:
            f.write(f"Page Number: {page['page_number']}\n")
            f.write(f"Orientation: {page['orientation']}\n")
            f.write(f"Page Width: {page['page_width']}\n")
            f.write(f"Page Height: {page['page_height']}\n")
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
            f.write("Graphics:\n")
            for graphic in page['graphics']:
                lines = graphic.get("lines", "N/A")
                points = graphic.get("points", "N/A")
                f.write(f"  Lines: {lines}\n")
                f.write(f"  Points: {points}\n")
                f.write(f"  Circles: {graphic.get('circles', 'N/A')}\n")
                f.write(f"  Rectangles: {graphic.get('rectangles', 'N/A')}\n")
                f.write(f"  Polygons: {graphic.get('polygons', 'N/A')}\n")
                f.write(f"  Graphics Matrix: {graphic.get('graphics_matrix', 'N/A')}\n")
    with open(detailed_report_file, 'w', encoding='utf-8') as detailed_f:
        for page in pdf_info:
            page_details = f"Page {page['page_number']} | Orientation: {page['orientation']}"
            for text in page['texts']:
                detailed_f.write(f"{page_details} | Text: {text['text_string']} | Coordinates: {text['coordinates']} | Rotation (deg): {text['text_rotation_in_degrees']}\n")
            for graphic in page['graphics']:
                detailed_f.write(f"{page_details} | Graphics: {graphic}\n")
# # # def main():
    # # # root = tk.Tk()
    # # # root.withdraw()
    # # # pdf_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    # # # if pdf_path:
        # # # pdf_info = extract_pdf_info(pdf_path)
        # # # output_file = pdf_path + "_summary.txt"
        # # # detailed_report_file = pdf_path + "_detailed.txt"
        # # # save_pdf_info(pdf_info, output_file, detailed_report_file)
        # # # print(f"PDF summary saved to {output_file}")
        # # # print(f"Detailed PDF report saved to {detailed_report_file}")
		
def save_enhanced_reports(pdf_info, font_wise_report, height_wise_report, output_file, detailed_report_file, font_report_file, height_report_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for page in pdf_info:
            f.write(f"Page Number: {page['page_number']}\n")
            f.write(f"Orientation: {page['orientation']}\n")
            f.write(f"Page Width: {page['page_width']}\n")
            f.write(f"Page Height: {page['page_height']}\n")

            f.write("Texts:\n")
            for text in page['texts']:
                f.write(f"  Text String: {text['text_string']}\n")
                f.write(f"  Coordinates (%): {text['coordinates_percent']}\n")
                f.write(f"  BBox Area (%): {text['bbox_area_percent']}\n")
                f.write(f"  Text Height: {text['text_height']}\n")
                f.write(f"  Text Color: {text['text_color']}\n")
                f.write(f"  Text Font: {text['text_font']}\n")

    with open(font_report_file, 'w', encoding='utf-8') as fr:
        fr.write("Font-Wise Content Report\n")
        for font_key, entries in font_wise_report.items():
            fr.write(f"Font: {font_key[0]}, Color: {font_key[1]}\n")
            for entry in entries:
                fr.write(f"  Page: {entry['page']} | Text: {entry['text']} | BBox Area (%): {entry['bbox_area_percent']} | Coordinates (%): {entry['coordinates_percent']}\n")

    with open(height_report_file, 'w', encoding='utf-8') as hr:
        hr.write("Text Height Pivot Report\n")
        for height_key, entries in height_wise_report.items():
            hr.write(f"Text Height: {height_key}\n")
            for entry in entries:
                hr.write(f"  Page: {entry['page']} | Text: {entry['text']} | Font: {entry['text_font']} | Color: {entry['text_color']}\n")
		
		
def main():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])

    if pdf_path:
        pdf_info, font_wise_report, height_wise_report = extract_pdf_info(pdf_path)
        output_file = pdf_path + "_summary.txt"
        detailed_report_file = pdf_path + "_detailed.txt"
        font_report_file = pdf_path + "_font_report.txt"
        height_report_file = pdf_path + "_height_report.txt"

        save_enhanced_reports(pdf_info, font_wise_report, height_wise_report, output_file, detailed_report_file, font_report_file, height_report_file)
        print(f"Reports saved to:\n{output_file}\n{detailed_report_file}\n{font_report_file}\n{height_report_file}")

# # # # # # # if __name__ == "__main__":
    # # # # # # # main()

	
if __name__ == "__main__":
    main()