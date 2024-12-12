import os
from datetime import datetime

def get_file_info(root_folder):
    file_info_list = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            try:
                # Check if the file is a Python file
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    # Get file times
                    creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    # Get file extension
                    file_extension = os.path.splitext(file)[1].lower()
                    
                    # Append file info to list
                    file_info_list.append([file, file_path, creation_time, modified_time, file_extension, root])
            except Exception as e:
                print(f"Error processing file {file}: {e}")

    # Sort the files by multiple criteria
    file_info_list.sort(key=lambda x: (x[2], x[3], len(x[0]), x[4]))  # Sort by creation, modification time, name length, extension
    return file_info_list
	
	
def process_file(file_info_list):
    combined_output = []
    for idx, (file_name, file_path, creation_time, modified_time, file_extension, root) in enumerate(file_info_list):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Remove Python comments and blank lines
            content = "\n".join([line for line in content.split('\n') if line.strip() and not line.strip().startswith("#")])
            # Renumber the lines
            content_with_line_numbers = "\n".join([f"{i+1}: {line}" for i, line in enumerate(content.split('\n'))])

            # Add file listing order and line number
            combined_output.append(f"File {idx + 1} - {file_name}:\n")
            combined_output.append(content_with_line_numbers)
            combined_output.append("\n" + "-"*40 + "\n")

    return combined_output	
# # # def process_file(file_info_list):
    # # # combined_output = []
	# # # for idx, (file_name, file_path, creation_time, modified_time, file_extension, root) in enumerate(file_info_list):
		# # # with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
			# # # content = f.read()
			# # # # Remove Python comments and blank lines
			# # # content = "\n".join([line for line in content.split('\n') if line.strip() and not line.strip().startswith("#")])
			# # # # Renumber the lines
			# # # content_with_line_numbers = "\n".join([f"{i+1}: {line}" for i, line in enumerate(content.split('\n'))])

			# # # # Add file listing order and line number
			# # # combined_output.append(f"File {idx + 1} - {file_name}:\n")
			# # # combined_output.append(content_with_line_numbers)
			# # # combined_output.append("\n" + "-"*40 + "\n")

	# # # return combined_output

# # # def process_file(file_info_list):
    # # # combined_output = []
    # # # for idx, (file_name, file_path, creation_time, modified_time, file_extension, root) in enumerate(file_info_list):
        # # # with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            # # # content = f.read()
            # # # # Remove Python comments
            # # # content = "\n".join([line for line in content.split('\n') if not line.strip().startswith("#")])
            # # # # Renumber the lines
            # # # content_with_line_numbers = "\n".join([f"{i+1}: {line}" for i, line in enumerate(content.split('\n'))])

            # # # # Add file listing order and line number
            # # # combined_output.append(f"File {idx + 1} - {file_name}:\n")
            # # # combined_output.append(content_with_line_numbers)
            # # # combined_output.append("\n" + "-"*40 + "\n")

    # # # return combined_output

# Set the root folder path
root_folder_path = '.'  # Set this to the desired folder

# Get file information and process files
file_info_list = get_file_info(root_folder_path)
combined_output = process_file(file_info_list)

# Save the processed data to an output file
output_file = 'combines_only_python_files_datewise_filewise_no_blank_lines_processed_python_files_output.txt'
with open(output_file, 'w', encoding='utf-8') as logfile:
    logfile.write("\n".join(combined_output))

print(f"Processed file info logged to {output_file}")