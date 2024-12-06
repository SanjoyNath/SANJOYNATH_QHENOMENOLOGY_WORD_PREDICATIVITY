import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
import csv
import os
#dont change the coding structures
#i need the subtypes objects data also with complete details 
#i need all the details for the (Oval)/Subtype/Circle/ kind of details also in the log
#i need the Filter[/FlateDecode]/FormType  deepest level details from the pages 
###dont change the orgiinal structured
#enhance the new needs features
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects

###dont change the orgiinal structured
#enhance the new needs features
def extract_and_annotate_pdf(input_pdf, output_csv_dir, regenerated_pdf_path, original_pdf_annotated_path, error_log_path, block_report_path):
    try:
###dont change the orgiinal structured
#enhance the new needs features	
        # Open the input PDF
        doc = fitz.open(input_pdf)
        error_log = open(error_log_path, 'w', encoding='utf-8')
        block_report = open(block_report_path, 'w', encoding='utf-8')

        # Create a new PDF document for regeneration
        new_doc = fitz.open()
        block_report.write("Page#\tBlock#\tType\tBBox\tContent\n")
###dont change the orgiinal structured
#enhance the new needs features	
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also
	

        # Iterate through pages
        for page_num in range(len(doc)):
            try:
                page = doc.load_page(page_num)
                csv_file_path = os.path.join(output_csv_dir, f"page_{page_num + 1}.csv")

                with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    blocks = page.get_text("dict")["blocks"]
					#i need report for all blocks and for all the types of pdf objects
					#i need the report for the graphic objects detailed reports and also for the shape objects in the pdf fles
					#  need the detailed reports for all the coordinates of the svg lke data , all coordnates data for the shape objects or whatever is there in the pdf files page wise
					#if any exception is there then log that records in the exceptions logger and not not stop the task instead log that and continue

                    # Create a new blank page with the same dimensions
                    new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects

                    for block_num, block in enumerate(blocks, start=1):
                        block_type = block["type"]
                        bbox = block["bbox"]
                        rect = fitz.Rect(bbox)
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects
						
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 						
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects

                        if rect.is_empty or rect.is_infinite:
                            continue
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects
							
# need the loggng of these cases properly n the excepton fle with the object data , exceptions reasons
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 							

                        # Extract block content
                        block_content = ""
                        if block_type == 0:  # Text block
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects
						
                            for line in block["lines"]:
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects
							
                                row = []
                                for span in line["spans"]:
                                    text = span["text"].replace(",", "_").replace("\n", "_")
                                    row.append(text)
                                    block_content += f"{text} "
                                    # Add text to the new page in blush color
                                    text_rect = fitz.Rect(span["bbox"])
									#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects

#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 	
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects
								
                                    new_page.insert_textbox(
                                        text_rect,
                                        text,
                                        fontsize=span["size"],
                                        color=(1, 0.5, 0.5),  # Blush color
                                        fontname="helv",  # Fallback font
                                    )
									#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects

                                csv_writer.writerow(row)

                        # Log block data
                        error_log.write(f"Page {page_num + 1}, Block {block_num}\n")
                        error_log.write(f"Block type: {block_type}, BBox: {bbox}\n")
                        error_log.write(f"Block content: {block}\n\n")

                        # Add block details to the structured report
                        block_report.write(f"{page_num + 1}\t{block_num}\t{block_type}\t{bbox}\t{block_content.strip()}\n")
                          #i need the detaled reports for all types of the blocks , coordinates of the graphic blocks , shape blocks and all kinds of objects data
						  #if there s exception then log that exception n detail in the seperate exception log fle and continue the processing
						  
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects
						  
                        # Annotate the block on the original page
                        page.draw_rect(rect, color=(0, 1, 0), width=1, dashes=[3, 3])  # Green dotted box
						#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects

                        # Write x, y coordinates for each corner of the bounding box
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 						
                        page.insert_text(
                            (rect.x0, rect.y0 - 10),
                            f"({rect.x0:.2f}, {rect.y0:.2f})",
                            fontsize=6,
                            color=(1, 0, 0),  # Red color for the coordinates
                            fontname="helv",
                        )
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 						
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
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 						

                        # Place small red circle at the insertion point (top-left of the bbox)
                        page.draw_circle((rect.x0, rect.y0), 3, color=(1, 0, 0), fill=True)
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects
						
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 						
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects

                        page.insert_textbox(
                            rect,
                            f"Block: {block_num}\nType: {block_type}\nContent: {block_content[:30]}...",
                            fontsize=6,
                            color=(0, 0, 0),
                            fontname="helv",
                        )
#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects
						
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 
						

                        # Annotate the block on the new page
                        new_page.draw_rect(rect, color=(0, 1, 0), width=1, dashes=[3, 3])  # Green dotted box
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 						
                        new_page.insert_textbox(
                            rect,
                            f"Block: {block_num}\nType: {block_type}\nContent: {block_content[:30]}...",
                            fontsize=6,
                            color=(0, 0, 0),
                            fontname="helv",
                        )
						#i need the annotations , annots , graphics , shapes everything logged and shown with the bounding boxes of different colors for different type of objects


#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 
						
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

#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 
						
            except Exception as page_error:
                error_log.write(f"Error on page {page_num + 1}: {page_error}\n")

        # Save the original annotated PDF
        doc.save(original_pdf_annotated_path)
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 		

        # Save the new regenerated PDF
        new_doc.save(regenerated_pdf_path)
#i need that you read the content from the orignal page and regenerate that data to the new_page step wise for all the objects
#dont miss any objects from the original read page and log the page width , page height also and recalculate the coordinates wth x,page_height-y   (since (x,y) to get from the left bottom corner of page
#if any matrix handlng is done to transform then write and log that also

#if there is any excepton then log that in the page rewriting 		

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

    # Create output directory for CSVs
    os.makedirs(output_csv_dir, exist_ok=True)

    extract_and_annotate_pdf(
        input_pdf_path, output_csv_dir, regenerated_pdf_path, original_pdf_annotated_path, error_log_path, block_report_path
    )


if __name__ == "__main__":
    main()
