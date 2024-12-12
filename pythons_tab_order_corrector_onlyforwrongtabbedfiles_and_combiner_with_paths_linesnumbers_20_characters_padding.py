import os
from datetime import datetime

def get_file_info(root_folder):
    file_info_list = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            try:
                if file.endswith('.py'):  # Only process Python files
                    file_path = os.path.join(root, file)
                    creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    file_extension = os.path.splitext(file)[1].lower()
                    file_info_list.append([file, file_path, creation_time, modified_time, file_extension, root])
            except Exception as e:
                print(f"Error processing file {file}: {e}")
    file_info_list.sort(key=lambda x: (x[2], x[3], len(x[0]), x[4]))  # Sorting files
    return file_info_list

def process_file(file_info_list):
    combined_output = []
    for idx, (file_name, file_path, creation_time, modified_time, file_extension, root) in enumerate(file_info_list):
        last_folder_name = os.path.basename(root)

        # Prepare the file header with path and dates
        file_header = f"File {idx + 1} - {file_name} - Path: {file_path}\n" \
                      f"Creation Date: {creation_time}\n" \
                      f"Last Modified Date: {modified_time}\n" \
                      f"Last Folder Name: {last_folder_name}\n"

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

            # Replace tabs with spaces (4 spaces per tab) and remove comments and blank lines
            original_content = content  # Store the original content for comparison
            content = "\n".join([line.replace("\t", "    ") for line in content.split('\n') if line.strip() and not line.strip().startswith("#")])

            # Check if tab corrections were needed
            if original_content != content:
                # Create a copy with tab corrections
                corrected_file_path = os.path.join(root, f"sngttabscorrected_{file_name}")
                with open(corrected_file_path, 'w', encoding='utf-8') as corrected_file:
                    corrected_file.write(content)

            # Process each line with padding and line number
            processed_lines = []
            for i, line in enumerate(content.split('\n')):
                leading_spaces = len(line) - len(line.lstrip(' '))
                line_number_str = f"{i+1}: ({leading_spaces})"
                padding = ' ' * (20 - len(line_number_str))
                processed_line = f"{line_number_str}{padding}{line}"
                processed_lines.append(processed_line)
            content_with_line_numbers = "\n".join(processed_lines)

            # Add file header and the processed content
            combined_output.append(file_header)
            combined_output.append(content_with_line_numbers)
            combined_output.append("\n" + "-"*40 + "\n")

    return combined_output

# Set the root folder path
root_folder_path = '.'  # Set this to the desired folder

# Get file information and process files
file_info_list = get_file_info(root_folder_path)
combined_output = process_file(file_info_list)

# Save the processed data to an output file
output_file = 'combined_python_files_with_tabs_corrected.txt'
with open(output_file, 'w', encoding='utf-8') as logfile:
    logfile.write("\n".join(combined_output))

print(f"Processed file info logged to {output_file}")