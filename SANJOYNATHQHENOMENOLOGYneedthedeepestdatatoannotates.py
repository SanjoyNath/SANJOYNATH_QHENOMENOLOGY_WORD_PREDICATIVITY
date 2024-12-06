import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
import csv
import os


import fitz  # PyMuPDF
import os
import uuid





import fitz  # PyMuPDF
import ezdxf  # For DXF generation


def draw_dxf_text_with_block_level_color(x_data, y_data, z_data, rotation, text_height, layer_name, text_data, xdata_text, block_level_color, handle_value_for_dxf):
    """
    Generate the DXF content for a TEXT entity with block level color and extended data (xdata).

    :param x_data: X position of the text
    :param y_data: Y position of the text
    :param z_data: Z position of the text
    :param rotation: Rotation angle of the text
    :param text_height: Height of the text
    :param layer_name: Layer name where the text is placed
    :param text_data: The actual text to be written
    :param xdata_text: Extended data text to be included
    :param block_level_color: Block color (0 to 254)
    :param handle_value_for_dxf: Incremental handle value for the DXF entity
    :return: DXF string for the TEXT entity
    """
    # Initialize the DXF content
    dxf_content = []

    handle_value_for_dxf += 1  # Increment the handle for each entity
    handle_value = "20F" + str(handle_value_for_dxf)

    # Start of the TEXT entity
    dxf_content.append("  0")
    dxf_content.append("TEXT")
    dxf_content.append("  5")
    dxf_content.append(handle_value)  # Handle value for the entity

    # Layer for the TEXT entity
    dxf_content.append("  8")
    dxf_content.append(layer_name)

    # Block level color (0 to 254)
    dxf_content.append("  62")
    dxf_content.append(f"    {block_level_color}")

    # Position (x, y, z)
    dxf_content.append(" 10")
    dxf_content.append(str(x_data))
    dxf_content.append(" 20")
    dxf_content.append(str(y_data))
    dxf_content.append(" 30")
    dxf_content.append(str(z_data))

    # Text height
    dxf_content.append(" 40")
    dxf_content.append(str(text_height))

    # The text data (ensure it's a string)
    dxf_content.append("  1")
    dxf_content.append(text_data)

    # Rotation angle
    dxf_content.append(" 50")
    dxf_content.append(str(rotation))

    # ACAD extended data (xdata)
    dxf_content.append("1001")
    dxf_content.append("ACAD")
    dxf_content.append("1002")
    dxf_content.append("{")
    dxf_content.append("1000")
    dxf_content.append(xdata_text)  # xdata as string
    dxf_content.append("1002")
    dxf_content.append("}")

    return "\n".join(dxf_content)


# # # def draw_dxf_text_with_block_level_color(x_data, y_data, z_data, rotation, text_height, layer_name, text_data, xdata_text, block_level_color, handle_value_for_dxf):
    # # # """
    # # # Generate the DXF content for a TEXT entity with block level color and extended data (xdata).

    # # # :param x_data: X position of the text
    # # # :param y_data: Y position of the text
    # # # :param z_data: Z position of the text
    # # # :param rotation: Rotation angle of the text
    # # # :param text_height: Height of the text
    # # # :param layer_name: Layer name where the text is placed
    # # # :param text_data: The actual text to be written
    # # # :param xdata_text: Extended data text to be included
    # # # :param block_level_color: Block color (0 to 254)
    # # # :param handle_value_for_dxf: Incremental handle value for the DXF entity
    # # # :return: DXF string for the TEXT entity
    # # # """
    # # # # Initialize the DXF content
    # # # dxf_content = []

    # # # handle_value_for_dxf += 1  # Increment the handle for each entity
    # # # handle_value = "20F" + str(handle_value_for_dxf)

    # # # # Start of the TEXT entity
    # # # dxf_content.append("  0")
    # # # dxf_content.append("TEXT")
    # # # dxf_content.append("  5")
    # # # dxf_content.append(handle_value)  # Handle value for the entity

    # # # # Layer for the TEXT entity
    # # # dxf_content.append("  8")
    # # # dxf_content.append(layer_name)

    # # # # Block level color (0 to 254)
    # # # dxf_content.append("  62")
    # # # dxf_content.append(f"    {block_level_color}")

    # # # # Position (x, y, z)
    # # # dxf_content.append(" 10")
    # # # dxf_content.append(str(x_data))
    # # # dxf_content.append(" 20")
    # # # dxf_content.append(str(y_data))
    # # # dxf_content.append(" 30")
    # # # dxf_content.append(str(z_data))

    # # # # Text height
    # # # dxf_content.append(" 40")
    # # # dxf_content.append(str(text_height))

    # # # # The text data
    # # # dxf_content.append("  1")
    # # # dxf_content.append(text_data)

    # # # # Rotation angle
    # # # dxf_content.append(" 50")
    # # # dxf_content.append(str(rotation))

    # # # # ACAD extended data (xdata)
    # # # dxf_content.append("1001")
    # # # dxf_content.append("ACAD")
    # # # dxf_content.append("1002")
    # # # dxf_content.append("{")
    # # # dxf_content.append("1000")
    # # # dxf_content.append(xdata_text)
    # # # dxf_content.append("1002")
    # # # dxf_content.append("}")

    # # # return "\n".join(dxf_content)


def pdf_to_dxf_with_custom_method(pdf_path, dxf_path):
    try:
        # Open the PDF
        pdf_document = fitz.open(pdf_path)
        print(f"Processing PDF: {pdf_path}")

        # Initialize the handle counter
        handle_value_for_dxf = 1000

        # Initialize the list for the DXF content
        dxf_content = []

        # Process each page
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            print(f"Processing Page {page_number + 1}")

            # Extract text blocks with positions
            blocks = page.get_text("blocks")  # [(x0, y0, x1, y1, "text", block_no), ...]

            for block_index, block in enumerate(blocks):
                if len(block) < 5:
                    continue

                x0, y0, x1, y1, text = block[:5]
                text = text.strip() or "EMPTY"

                # Generate DXF text for each block with appropriate values
                dxf_text = draw_dxf_text_with_block_level_color(
                    x0, y0, 0, 0, 0.1,  # Assume rotation 0 and text height 0.1 for now
                    "TextLayer", text, "Some xdata", 8, handle_value_for_dxf
                )
                dxf_content.append(dxf_text)

        # Write the DXF content to the output file
        with open(dxf_path, 'w') as dxf_file:
            # Write DXF header and entities
            dxf_file.write("0\nSECTION\n2\nHEADER\n0\nENDSEC\n")
            dxf_file.write("0\nSECTION\n2\nTABLES\n0\nENDSEC\n")
            dxf_file.write("0\nSECTION\n2\nBLOCKS\n0\nENDSEC\n")
            dxf_file.write("0\nSECTION\n2\nENTITIES\n")

            # Write the accumulated DXF content (TEXT entities)
            dxf_file.write("\n".join(dxf_content))

            # Write DXF footer
            dxf_file.write("\n0\nENDSEC\n0\nEOF\n")

        print(f"DXF file created at: {dxf_path}")

    except Exception as e:
        print(f"Error: {e}")



def pdf_to_dxf_with_ezdxf(pdf_path, dxf_path):
    try:
        # Open the PDF
        pdf_document = fitz.open(pdf_path)
        print(f"Processing PDF: {pdf_path}")

        # Create a new DXF document
        dxf_document = ezdxf.new()

        # Add layers for different types of entities
        text_layer = dxf_document.layers.new(name="TextLayer")
        boundary_layer = dxf_document.layers.new(name="BoundaryLayer")

        # Get the modelspace (where entities are added)
        msp = dxf_document.modelspace()

        # Process each page
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            print(f"Processing Page {page_number + 1}")

            # Extract text blocks with positions
            blocks = page.get_text("blocks")  # [(x0, y0, x1, y1, "text", block_no), ...]

            for block_index, block in enumerate(blocks):
                if len(block) < 5:
                    continue

                x0, y0, x1, y1, text = block[:5]
                text = text.strip() or "EMPTY"

                # Add the text entity with proper positioning
                msp.add_text(
                    text,
                    dxfattribs={
                        "layer": "TextLayer",
                        "height": 0.1,  # Text height
                        "style": "Standard",  # Optional: can define your own style
                    },
                ).set_pos((x0, y0))  # Positioning text at (x0, y0)

                # Add a rectangle for the bounding box
                msp.add_lwpolyline(
                    [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                    close=True,
                    dxfattribs={"layer": "BoundaryLayer"},
                )

        # Save the DXF file
        dxf_document.saveas(dxf_path)
        print(f"DXF file created at: {dxf_path}")

    except Exception as e:
        print(f"Error: {e}")




# # # def pdf_to_dxf_with_ezdxf(pdf_path, dxf_path):
    # # # try:
        # # # # Open the PDF
        # # # pdf_document = fitz.open(pdf_path)
        # # # print(f"Processing PDF: {pdf_path}")

        # # # # Create a new DXF document
        # # # dxf_document = ezdxf.new()

        # # # # Add layers for different types of entities
        # # # text_layer = dxf_document.layers.new(name="TextLayer")
        # # # boundary_layer = dxf_document.layers.new(name="BoundaryLayer")

        # # # # Get the modelspace (where entities are added)
        # # # msp = dxf_document.modelspace()

        # # # # Process each page
        # # # for page_number in range(len(pdf_document)):
            # # # page = pdf_document[page_number]
            # # # print(f"Processing Page {page_number + 1}")

            # # # # Extract text blocks with positions
            # # # blocks = page.get_text("blocks")  # [(x0, y0, x1, y1, "text", block_no), ...]

            # # # for block_index, block in enumerate(blocks):
                # # # if len(block) < 5:
                    # # # continue

                # # # x0, y0, x1, y1, text = block[:5]
                # # # text = text.strip() or "EMPTY"

                # # # # Add the text entity with proper positioning
                # # # msp.add_text(
                    # # # text,
                    # # # insert=(x0, y0),  # Position specified here
                    # # # height=0.1,  # Text height
                    # # # layer="TextLayer"  # Layer assignment
                # # # )

                # # # # Add a rectangle for the bounding box
                # # # msp.add_lwpolyline(
                    # # # [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                    # # # close=True,
                    # # # dxfattribs={"layer": "BoundaryLayer"},
                # # # )

        # # # # Save the DXF file
        # # # dxf_document.saveas(dxf_path)
        # # # print(f"DXF file created at: {dxf_path}")

    # # # except Exception as e:
        # # # print(f"Error: {e}")

		
# # # def pdf_to_dxf_with_ezdxf(pdf_path, dxf_path):
    # # # try:
        # # # # Open the PDF
        # # # pdf_document = fitz.open(pdf_path)
        # # # print(f"Processing PDF: {pdf_path}")

        # # # # Create a new DXF document
        # # # dxf_document = ezdxf.new()

        # # # # Add layers for different types of entities
        # # # text_layer = dxf_document.layers.new(name="TextLayer")
        # # # boundary_layer = dxf_document.layers.new(name="BoundaryLayer")

        # # # # Get the modelspace (where entities are added)
        # # # msp = dxf_document.modelspace()

        # # # # Process each page
        # # # for page_number in range(len(pdf_document)):
            # # # page = pdf_document[page_number]
            # # # print(f"Processing Page {page_number + 1}")

            # # # # Extract text blocks with positions
            # # # blocks = page.get_text("blocks")  # [(x0, y0, x1, y1, "text", block_no), ...]

            # # # for block_index, block in enumerate(blocks):
                # # # if len(block) < 5:
                    # # # continue

                # # # x0, y0, x1, y1, text = block[:5]
                # # # text = text.strip() or "EMPTY"

                # # # # Add the text entity with proper positioning
                # # # msp.add_text(
                    # # # text,
                    # # # dxfattribs={
                        # # # "layer": "TextLayer",
                        # # # "height": 0.1,  # Text height
                    # # # }
                # # # ).set_pos((x0, y0))

                # # # # Add a rectangle for the bounding box
                # # # msp.add_lwpolyline(
                    # # # [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                    # # # close=True,
                    # # # dxfattribs={"layer": "BoundaryLayer"},
                # # # )

        # # # # Save the DXF file
        # # # dxf_document.saveas(dxf_path)
        # # # print(f"DXF file created at: {dxf_path}")

    # # # except Exception as e:
        # # # print(f"Error: {e}")



# def pdf_to_dxf_with_ezdxf(pdf_path, dxf_path):
    # try:
        # # Open the PDF
        # pdf_document = fitz.open(pdf_path)
        # print(f"Processing PDF: {pdf_path}")

        # # Create a new DXF document
        # dxf_document = ezdxf.new()

        # # Add layers for different types of entities
        # text_layer = dxf_document.layers.new(name="TextLayer")
        # boundary_layer = dxf_document.layers.new(name="BoundaryLayer")

        # # Get the modelspace (where entities are added)
        # msp = dxf_document.modelspace()

        # # Process each page
        # for page_number in range(len(pdf_document)):
            # page = pdf_document[page_number]
            # print(f"Processing Page {page_number + 1}")

            # # Extract text blocks with positions
            # blocks = page.get_text("blocks")  # [(x0, y0, x1, y1, "text", block_no), ...]

            # for block_index, block in enumerate(blocks):
                # if len(block) < 5:
                    # continue

                # x0, y0, x1, y1, text = block[:5]
                # text = text.strip() or "EMPTY"

                # # Add the text entity
                # msp.add_text(
                    # text,
                    # dxfattribs={
                        # "layer": "TextLayer",
                        # "height": 0.1,  # Text height
                    # },
                # ).set_pos((x0, y0), align="LEFT")

                # # Add a rectangle for the bounding box
                # msp.add_lwpolyline(
                    # [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                    # close=True,
                    # dxfattribs={"layer": "BoundaryLayer"},
                # )

        # # Save the DXF file
        # dxf_document.saveas(dxf_path)
        # print(f"DXF file created at: {dxf_path}")

    # except Exception as e:
        # print(f"Error: {e}")



# def pdf_to_dxf_with_ezdxf(pdf_path, dxf_path):
    # try:
        # # Open the PDF
        # pdf_document = fitz.open(pdf_path)
        # print(f"Processing PDF: {pdf_path}")

        # # Create a new DXF document
        # dxf_document = ezdxf.new()

        # # Add layers for different types of entities
        # text_layer = dxf_document.layers.new(name="TextLayer")
        # boundary_layer = dxf_document.layers.new(name="BoundaryLayer")

        # # Get the modelspace (where entities are added)
        # msp = dxf_document.modelspace()

        # # Process each page
        # for page_number in range(len(pdf_document)):
            # page = pdf_document[page_number]
            # print(f"Processing Page {page_number + 1}")

            # # Extract text blocks with positions
            # blocks = page.get_text("blocks")  # [(x0, y0, x1, y1, "text", block_no), ...]

            # for block_index, block in enumerate(blocks):
                # if len(block) < 5:
                    # continue

                # x0, y0, x1, y1, text = block[:5]
                # text = text.strip() or "EMPTY"

                # # Add the text entity
                # msp.add_text(
                    # text,
                    # dxfattribs={
                        # "layer": "TextLayer",
                        # "height": 0.1,  # Text height
                    # },
                # ).set_pos((x0, y0), align="LEFT")

                # # Add a rectangle for the bounding box
                # msp.add_lwpolyline(
                    # [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                    # close=True,
                    # dxfattribs={"layer": "BoundaryLayer"},
                # )

        # # Save the DXF file
        # dxf_document.saveas(dxf_path)
        # print(f"DXF file created at: {dxf_path}")

    # except Exception as e:
        # print(f"Error: {e}")

def generate_dxf_handle():
    """Generate a unique DXF handle."""
    return uuid.uuid4().hex[:6].upper()


	
	
	
def pdf_to_dxf(pdf_path, dxf_path):
    try:
        # Open the PDF
        pdf_document = fitz.open(pdf_path)
        print(f"Processing PDF: {pdf_path}")
        
        # Create DXF file
        with open(dxf_path, 'w') as dxf_file:
            # Write DXF Header
            write_dxf_header(dxf_file)

            # Process each page
            for page_number in range(len(pdf_document)):
                page = pdf_document[page_number]
                print(f"Processing Page {page_number + 1}")

                # Extract text blocks with positions
                blocks = page.get_text("blocks")  # List of (x0, y0, x1, y1, "text", block_no)

                for block_index, block in enumerate(blocks):
                    if len(block) < 5:
                        continue
                    x0, y0, x1, y1, text = block[:5]
                    text = text.strip() or "EMPTY"

                    # Generate handles for unique identification
                    line_handle = generate_dxf_handle()
                    text_handle = generate_dxf_handle()

                    # Write line entity (bounding box edges)
                    write_dxf_line(dxf_file, line_handle, x0, y0, x1, y0)  # Bottom line
                    write_dxf_line(dxf_file, generate_dxf_handle(), x1, y0, x1, y1)  # Right line
                    write_dxf_line(dxf_file, generate_dxf_handle(), x1, y1, x0, y1)  # Top line
                    write_dxf_line(dxf_file, generate_dxf_handle(), x0, y1, x0, y0)  # Left line

                    # Write text entity
                    write_dxf_text(dxf_file, text_handle, x0 + 0.03, y0 + 0.03, text, block_index)

            # Write DXF Footer
            write_dxf_footer(dxf_file)

        print(f"DXF file created at: {dxf_path}")

    except Exception as e:
        print(f"Error: {e}")


def write_dxf_header(dxf_file):
    """Write DXF file header."""
    dxf_file.write("0\nSECTION\n2\nHEADER\n0\nENDSEC\n")
    dxf_file.write("0\nSECTION\n2\nTABLES\n0\nENDSEC\n")
    dxf_file.write("0\nSECTION\n2\nBLOCKS\n0\nENDSEC\n")
    dxf_file.write("0\nSECTION\n2\nENTITIES\n")


# # # def write_dxf_line(dxf_file, handle, x0, y0, x1, y1):
    # # # """
    # # # Write LINE entity in DXF format.
    # # # """
    # # # dxf_file.write("0\nLINE\n")
    # # # dxf_file.write(f"  5\n{handle}\n")  # Unique handle
    # # # dxf_file.write("  8\nChecking_lines_layers\n")  # Layer name
    # # # dxf_file.write(" 62\n    8\n")  # Color index
    # # # dxf_file.write(f" 10\n{x0}\n 20\n{y0}\n 30\n-3000\n")  # Start point
    # # # dxf_file.write(f" 11\n{x1}\n 21\n{y1}\n 31\n-3000\n")  # End point
    # # # dxf_file.write("1001\nACAD\n1002\n{\n")
    # # # dxf_file.write("1000\nchecking_lines_xdata\n")  # XData tag
    # # # dxf_file.write("1002\n}\n")


# # # def write_dxf_text(dxf_file, handle, x, y, text, block_index):
    # # # """
    # # # Write TEXT entity in DXF format.
    # # # """
    # # # dxf_file.write("0\nTEXT\n")
    # # # dxf_file.write(f"  5\n{handle}\n")  # Unique handle
    # # # dxf_file.write("  8\nlines_link_relations_logger\n")  # Layer name
    # # # dxf_file.write(" 62\n    9\n")  # Color index
    # # # dxf_file.write(f" 10\n{x}\n 20\n{y}\n 30\n-3000\n")  # Insertion point
    # # # dxf_file.write(" 40\n0.06\n")  # Text height
    # # # dxf_file.write(f"  1\n{text}\n")  # Text content
    # # # dxf_file.write(" 50\n0\n")  # Rotation
    # # # dxf_file.write("1001\nACAD\n1002\n{\n")
    # # # dxf_file.write("1000\nlines_address_index\n")  # XData tag
    # # # dxf_file.write("1002\n}\n")


# # # def write_dxf_footer(dxf_file):
    # # # """Write DXF file footer."""
    # # # dxf_file.write("0\nENDSEC\n0\nEOF\n")


# # # def pdf_to_dxf(pdf_path, dxf_path):
    # # # try:
        # # # # Open the PDF
        # # # pdf_document = fitz.open(pdf_path)
        # # # print(f"Processing PDF: {pdf_path}")
        
        # # # # Create DXF file
        # # # with open(dxf_path, 'w') as dxf_file:
            # # # # Write DXF Header
            # # # write_dxf_header(dxf_file)

            # # # # Process each page
            # # # for page_number in range(len(pdf_document)):
                # # # page = pdf_document[page_number]
                # # # print(f"Processing Page {page_number + 1}")

                # # # # Extract text blocks with positions
                # # # blocks = page.get_text("blocks")  # List of (x0, y0, x1, y1, "text", block_no)

                # # # for block in blocks:
                    # # # # Ensure the block contains valid data
                    # # # if len(block) < 5:
                        # # # continue

                    # # # x0, y0, x1, y1, text = block[:5]
                    # # # tag = f"Page_{page_number + 1}_Block_{blocks.index(block)}"  # Tagging
                    # # # write_dxf_text(dxf_file, x0, y0, x1, y1, text, tag)

            # # # # Write DXF Footer
            # # # write_dxf_footer(dxf_file)

        # # # print(f"DXF file created at: {dxf_path}")

    # # # except Exception as e:
        # # # print(f"Error: {e}")


# # # def write_dxf_header(dxf_file):
    # # # """Write DXF file header."""
    # # # dxf_file.write("0\nSECTION\n2\nHEADER\n0\nENDSEC\n")
    # # # dxf_file.write("0\nSECTION\n2\nTABLES\n0\nENDSEC\n")
    # # # dxf_file.write("0\nSECTION\n2\nBLOCKS\n0\nENDSEC\n")
    # # # dxf_file.write("0\nSECTION\n2\nENTITIES\n")


# # # def write_dxf_text(dxf_file, x0, y0, x1, y1, text, tag):
    # # # """
    # # # Write text block as DXF TEXT entity with proper tagging.
    # # # """
    # # # # Normalize text to avoid empty or invalid values
    # # # text = text.strip() if text else "EMPTY"

    # # # # Write text entity
    # # # dxf_file.write("0\nTEXT\n")
    # # # dxf_file.write(f"8\nLayer1\n")  # Default Layer
    # # # dxf_file.write(f"10\n{x0}\n20\n{y0}\n30\n0\n")  # Lower-left corner
    # # # dxf_file.write(f"40\n10\n")  # Text height
    # # # #dxf_file.write(f"1\n{text}\n")  # Text content
    # # # #dxf_file.write(f"999\n{tag}\n")  # Tagging for identification

    # # # # Write boundary box
    # # # dxf_file.write("0\nLINE\n")  # Bottom line
    # # # dxf_file.write(f"8\nLayer1\n10\n{x0}\n20\n{y0}\n30\n0\n")
    # # # dxf_file.write(f"11\n{x1}\n21\n{y0}\n31\n0\n")
    # # # dxf_file.write("0\nLINE\n")  # Right line
    # # # dxf_file.write(f"10\n{x1}\n20\n{y0}\n30\n0\n")
    # # # dxf_file.write(f"11\n{x1}\n21\n{y1}\n31\n0\n")
    # # # dxf_file.write("0\nLINE\n")  # Top line
    # # # dxf_file.write(f"10\n{x1}\n20\n{y1}\n30\n0\n")
    # # # dxf_file.write(f"11\n{x0}\n21\n{y1}\n31\n0\n")
    # # # dxf_file.write("0\nLINE\n")  # Left line
    # # # dxf_file.write(f"10\n{x0}\n20\n{y1}\n30\n0\n")
    # # # dxf_file.write(f"11\n{x0}\n21\n{y0}\n31\n0\n")


# # # def write_dxf_footer(dxf_file):
    # # # """Write DXF file footer."""
    # # # dxf_file.write("0\nENDSEC\n0\nEOF\n")

	
	
	
# # # def pdf_to_dxf(pdf_path, dxf_path):
    # # # try:
        # # # # Open the PDF
        # # # pdf_document = fitz.open(pdf_path)
        # # # print(f"Processing PDF: {pdf_path}")
        
        # # # # Create DXF file
        # # # with open(dxf_path, 'w') as dxf_file:
            # # # # Write DXF Header
            # # # write_dxf_header(dxf_file)

            # # # # Process each page
            # # # for page_number in range(len(pdf_document)):
                # # # page = pdf_document[page_number]
                # # # print(f"Processing Page {page_number + 1}")

                # # # # Extract text blocks with positions
                # # # blocks = page.get_text("blocks")  # [(x0, y0, x1, y1, "text", block_no), ...]

                # # # for block in blocks:
                    # # # x0, y0, x1, y1, text, block_no = block
                    # # # tag = f"Page_{page_number+1}_Block_{block_no}"  # Tagging
                    # # # write_dxf_text(dxf_file, x0, y0, x1, y1, text, tag)

            # # # # Write DXF Footer
            # # # write_dxf_footer(dxf_file)

        # # # print(f"DXF file created at: {dxf_path}")

    # # # except Exception as e:
        # # # print(f"Error: {e}")


# # # def write_dxf_header(dxf_file):
    # # # """Write DXF file header."""
    # # # dxf_file.write("0\nSECTION\n2\nHEADER\n0\nENDSEC\n")
    # # # dxf_file.write("0\nSECTION\n2\nTABLES\n0\nENDSEC\n")
    # # # dxf_file.write("0\nSECTION\n2\nBLOCKS\n0\nENDSEC\n")
    # # # dxf_file.write("0\nSECTION\n2\nENTITIES\n")


# # # def write_dxf_text(dxf_file, x0, y0, x1, y1, text, tag):
    # # # """
    # # # Write text block as DXF TEXT entity with proper tagging.
    # # # """
    # # # dxf_file.write("0\nTEXT\n")
    # # # dxf_file.write(f"8\nLayer1\n")  # Default Layer
    # # # dxf_file.write(f"10\n{x0}\n20\n{y0}\n")  # Lower-left corner
    # # # dxf_file.write(f"40\n10\n")  # Text height
    # # # dxf_file.write(f"1\n{text.strip()}\n")  # Text content
    # # # dxf_file.write(f"999\n{tag}\n")  # Tagging for identification
    # # # dxf_file.write(f"0\nLINE\n")  # Add boundary box for the text
    # # # dxf_file.write(f"8\nLayer1\n10\n{x0}\n20\n{y0}\n30\n0\n")
    # # # dxf_file.write(f"11\n{x1}\n21\n{y0}\n31\n0\n")  # Bottom line
    # # # dxf_file.write(f"0\nLINE\n10\n{x1}\n20\n{y0}\n30\n0\n")
    # # # dxf_file.write(f"11\n{x1}\n21\n{y1}\n31\n0\n")  # Right line
    # # # dxf_file.write(f"0\nLINE\n10\n{x1}\n20\n{y1}\n30\n0\n")
    # # # dxf_file.write(f"11\n{x0}\n21\n{y1}\n31\n0\n")  # Top line
    # # # dxf_file.write(f"0\nLINE\n10\n{x0}\n20\n{y1}\n30\n0\n")
    # # # dxf_file.write(f"11\n{x0}\n21\n{y0}\n31\n0\n")  # Left line


# # # def write_dxf_footer(dxf_file):
    # # # """Write DXF file footer."""
    # # # dxf_file.write("0\nENDSEC\n0\nEOF\n")


# # # # Example usage
# # # if __name__ == "__main__":
    # # # input_pdf = "example.pdf"  # Path to the input PDF
    # # # output_dxf = "output.dxf"  # Path for the output DXF

    # # # if os.path.exists(input_pdf):
        # # # pdf_to_dxf(input_pdf, output_dxf)
    # # # else:
        # # # print(f"Input PDF does not exist: {input_pdf}")

def extract_and_annotate_pdf(input_pdf, output_csv_dir, regenerated_pdf_path, original_pdf_annotated_path, error_log_path, block_report_path):
    try:
        # Open the input PDF
        doc = fitz.open(input_pdf)
        error_log = open(error_log_path, 'w', encoding='utf-8')
        block_report = open(block_report_path, 'w', encoding='utf-8')
        
        # Create a new PDF document for regeneration
        new_doc = fitz.open()
        block_report.write("Page#\tBlock#\tType\tBBox\tContent\n")
        
        # Iterate through pages
        for page_num in range(len(doc)):
            try:
                page = doc.load_page(page_num)
                csv_file_path = os.path.join(output_csv_dir, f"page_{page_num + 1}.csv")
                with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    blocks = page.get_text("dict")["blocks"]
                    
                    # Create a new blank page with the same dimensions
                    new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
                    
                    for block_num, block in enumerate(blocks, start=1):
                        block_type = block["type"]
                        bbox = block["bbox"]
                        rect = fitz.Rect(bbox)
                        
                        if rect.is_empty or rect.is_infinite:
                            continue
                        
                        # Extract block content
                        block_content = ""
                        if block_type == 0:  # Text block
                            for line in block["lines"]:
                                row = []
                                for span in line["spans"]:
                                    text = span["text"].replace(",", "_").replace("\n", "_")
                                    row.append(text)
                                    block_content += f"{text} "
                                    
                                    # Add text to the new page in blush color
                                    text_rect = fitz.Rect(span["bbox"])
                                    new_page.insert_textbox(
                                        text_rect,
                                        text,
                                        fontsize=span["size"],
                                        color=(1, 0.5, 0.5),  # Blush color
                                        fontname="helv",  # Fallback font
                                    )
                                csv_writer.writerow(row)
                        
                        # Log block data
                        error_log.write(f"Page {page_num + 1}, Block {block_num}\n")
                        error_log.write(f"Block type: {block_type}, BBox: {bbox}\n")
                        error_log.write(f"Block content: {block}\n\n")
                        
                        # Add block details to the structured report
                        block_report.write(f"{page_num + 1}\t{block_num}\t{block_type}\t{bbox}\t{block_content.strip()}\n")
                        
                        # Annotate the block on the original page
                        page.draw_rect(rect, color=(0, 1, 0), width=1, dashes=[3, 3])  # Green dotted box
                        
                        # Write x, y coordinates for each corner of the bounding box
                        page.insert_text(
                            (rect.x0, rect.y0 - 10),
                            f"({rect.x0:.2f}, {rect.y0:.2f})",
                            fontsize=6,
                            color=(1, 0, 0),  # Red color for the coordinates
                            fontname="helv",
                        )
                        page.insert_text(
                            (rect.x1, rect.y0 - 10),
                            f"({rect.x1:.2f}, {rect.y0:.2f})",
                            fontsize=6,
                            color=(1, 0, 0),  # Red color for the coordinates
                            fontname="helv",
                        )
                        page.insert_text(
                            (rect.x0, rect.y1 + 5),
                            f"({rect.x0:.2f}, {rect.y1:.2f})",
                            fontsize=6,
                            color=(1, 0, 0),  # Red color for the coordinates
                            fontname="helv",
                        )
                        page.insert_text(
                            (rect.x1, rect.y1 + 5),
                            f"({rect.x1:.2f}, {rect.y1:.2f})",
                            fontsize=6,
                            color=(1, 0, 0),  # Red color for the coordinates
                            fontname="helv",
                        )
                        
                        # Place small red circle at the insertion point (top-left of the bbox)
                        page.draw_circle((rect.x0, rect.y0), 3, color=(1, 0, 0), fill=True)
                        
                        # Annotate the block on the new page
                        new_page.draw_rect(rect, color=(0, 1, 0), width=1, dashes=[3, 3])  # Green dotted box
                        new_page.insert_textbox(
                            rect,
                            f"Block: {block_num}\nType: {block_type}\nContent: {block_content[:30]}...",
                            fontsize=6,
                            color=(0, 0, 0),
                            fontname="helv",
                        )
                        
                        # Write BBox percentage info
                        bbox_area = rect.width * rect.height
                        page_area = page.rect.width * page.rect.height
                        percentage = (bbox_area / page_area) * 100
                        text_position = (rect.x0, rect.y0 - 10)
                        new_page.insert_textbox(
                            fitz.Rect(*text_position, rect.x0 + 50, rect.y0),
                            f"BBox %: {percentage:.2f}%",
                            fontsize=6,
                            color=(0, 0, 0),
                            fontname="helv",
                        )
                        
                        # Log subtypes and other details
                        if "subtype" in block:
                            subtype = block["subtype"]
                            error_log.write(f"Subtype: {subtype}\n")
                            block_report.write(f"\tSubtype: {subtype}\n")
                        
                        if "matrix" in block:
                            matrix = block["matrix"]
                            error_log.write(f"Matrix: {matrix}\n")
                            block_report.write(f"\tMatrix: {matrix}\n")
                        
                        if "stream" in block:
                            stream = block["stream"]
                            error_log.write(f"Stream: {stream}\n")
                            block_report.write(f"\tStream: {stream}\n")
            
            except Exception as page_error:
                error_log.write(f"Error on page {page_num + 1}: {page_error}\n")
        
        # Save the original annotated PDF
        doc.save(original_pdf_annotated_path)
        
        # Save the new regenerated PDF
        new_doc.save(regenerated_pdf_path)
        
        error_log.close()
        block_report.close()
        
        print(f"Original annotated PDF saved: {original_pdf_annotated_path}")
        print(f"Regenerated PDF saved: {regenerated_pdf_path}")
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
    regenerated_pdf_path = os.path.splitext(input_pdf_path)[0] + "_regenerated.pdf"
    original_pdf_annotated_path = os.path.splitext(input_pdf_path)[0] + "_original_annotated.pdf"
    error_log_path = os.path.splitext(input_pdf_path)[0] + "_errorlog.txt"
    block_report_path = os.path.splitext(input_pdf_path)[0] + "_block_report.txt"
    output_dxf=os.path.splitext(input_pdf_path)[0] + "__saan_generates_dxf.dxf"

    
    # Create output directory for CSVs
    os.makedirs(output_csv_dir, exist_ok=True)
    
    extract_and_annotate_pdf(
        input_pdf_path, output_csv_dir, regenerated_pdf_path, original_pdf_annotated_path, error_log_path, block_report_path
    )
    ###pdf_to_dxf(input_pdf_path, output_dxf)	
    ###pdf_to_dxf_with_ezdxf(input_pdf_path, output_dxf)
    pdf_to_dxf_with_custom_method(input_pdf_path, output_dxf)
	
    # # # if os.path.exists(input_pdf_path):
    # # # #    pdf_to_dxf(input_pdf_path, output_dxf)
    # # # else:
        # # # print(f"Input PDF does not exist: {input_pdf}")	

if __name__ == "__main__":
    main()