import os
import csv
from datetime import datetime

def get_file_info(root_folder):
    folder_counter = 0
    file_counter = 0
    extension_counter = {}
    folder_sizes = {}
    file_info_list = []

    for root, dirs, files in os.walk(root_folder):
        folder_counter += 1
        folder_size = 0

        for file in files:
            file_counter += 1
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            folder_size += file_size

            # Get file extension
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension not in extension_counter:
                extension_counter[file_extension] = 0
            extension_counter[file_extension] += 1

            # Get file times
            creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            accessed_time = datetime.fromtimestamp(os.path.getatime(file_path))

            # Append file info to list
            file_info_list.append([
                folder_counter,
                file_counter,
                file_extension,
                folder_size,
                file_size,
                creation_time,
                modified_time,
                accessed_time,
                root,
                file
            ])

        # Store folder size
        folder_sizes[root] = folder_size

    return folder_counter, file_counter, extension_counter, folder_sizes, file_info_list

def write_file_info_to_csv(file_info_list, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='#')
        csvwriter.writerow([
            'Folder Counter',
            'File Counter',
            'File Extension',
            'Folder Size (bytes)',
            'File Size (bytes)',
            'Creation Time',
            'Modified Time',
            'Accessed Time',
            'Folder Path',
            'File Name'
        ])
        csvwriter.writerows(file_info_list)

# Set the root folder path and output CSV file path
root_folder_path = '.'  # Change this to the desired root folder path
output_csv_file = 'file_info_log.csv'

# Get file info and write to CSV
folder_counter, file_counter, extension_counter, folder_sizes, file_info_list = get_file_info(root_folder_path)
write_file_info_to_csv(file_info_list, output_csv_file)

print(f"File info logged to {output_csv_file}")