import os
from datetime import datetime
from collections import Counter

def get_file_info(root_folder):
    folder_counter = 0
    file_counter = 0
    extension_counter = {}
    folder_sizes = {}
    file_info_list = []
    readable_extensions = ['.txt', '.py', '.cs', '.cpp', '.h', '.pyi', '.java', '.ini', '.cfg', '.xml']

    for root, dirs, files in os.walk(root_folder):
        folder_counter += 1
        folder_size = 0

        for file in files:
            try:
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
                hours_unaccessed = (datetime.now() - accessed_time).total_seconds() / 3600

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
                    hours_unaccessed,
                    root,
                    file
                ])

                # If the file is readable, append its content and line count
                if file_extension in readable_extensions:
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            line_count = content.count('\n') + 1
                            content_with_line_numbers = '\n'.join(f"{i+1}: {line}" for i, line in enumerate(content.split('\n')))
                            file_info_list.append([
                                'File Content:',
                                content_with_line_numbers,
                                'Line Count:',
                                line_count
                            ])
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")

            except Exception as e:
                print(f"Error processing file {file}: {e}")

        # Store folder size
        folder_sizes[root] = folder_size

    return folder_counter, file_counter, extension_counter, folder_sizes, file_info_list

def write_file_info_to_log(file_info_list, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as logfile:
            logfile.write('Folder Counter###File Counter###File Extension###Folder Size (bytes)###File Size (bytes)###Creation Time###Modified Time###Accessed Time###Hours Unaccessed###Folder Path###File Name\n')
            for info in file_info_list:
                logfile.write('###'.join(map(str, info)) + '\n')
    except Exception as e:
        print(f"Error writing to log file {output_file}: {e}")

def write_file_summary_to_log(file_info_list, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as logfile:
            logfile.write('Folder Counter###File Counter###File Extension###Folder Size (bytes)###File Size (bytes)###Creation Time###Modified Time###Accessed Time###Hours Unaccessed###Folder Path###File Name\n')
            for info in file_info_list:
                if isinstance(info[0], int):  # Only write the summary lines (not the content lines)
                    logfile.write('###'.join(map(str, info)) + '\n')
    except Exception as e:
        print(f"Error writing to summary log file {output_file}: {e}")

def write_extension_size_distribution(file_info_list, output_file):
    try:
        extension_size = {}
        for info in file_info_list:
            if isinstance(info[0], int):  # Only process the summary lines
                extension = info[2]
                size = info[4]
                if extension not in extension_size:
                    extension_size[extension] = 0
                extension_size[extension] += size

        with open(output_file, 'w', encoding='utf-8') as logfile:
            logfile.write('Extension###Size (bytes)\n')
            for ext, size in extension_size.items():
                logfile.write(f"{ext}###{size}\n")
    except Exception as e:
        print(f"Error writing to extension size distribution log file {output_file}: {e}")

def write_keyword_frequency(file_info_list, output_file):
    try:
        keyword_counter = Counter()
        for info in file_info_list:
            if isinstance(info[0], list) and info[0] == 'File Content:':
                content = info[1]
                words = content.split()
                keyword_counter.update(words)

        with open(output_file, 'w', encoding='utf-8') as logfile:
            logfile.write('Keyword###Frequency\n')
            for word, freq in keyword_counter.items():
                logfile.write(f"{word}###{freq}\n")
    except Exception as e:
        print(f"Error writing to keyword frequency log file {output_file}: {e}")

# Set the root folder path and output log file path with timestamp
root_folder_path = '.'  # Change this to the desired root folder path
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
base_folder_name = os.path.basename(os.path.abspath(root_folder_path))
output_log_file = f'{base_folder_name}_file_info_log_{timestamp}.saan_file_log'
output_summary_file = f'{base_folder_name}_file_summary_{timestamp}.saan_file_log'
output_extension_size_file = f'{base_folder_name}_extension_size_{timestamp}.saan_file_log'
output_keyword_file = f'{base_folder_name}_keyword_frequency_{timestamp}.saan_file_log'

try:
    # Get file info and write to log files
    folder_counter, file_counter, extension_counter, folder_sizes, file_info_list = get_file_info(root_folder_path)
    write_file_info_to_log(file_info_list, output_log_file)
    write_file_summary_to_log(file_info_list, output_summary_file)
    write_extension_size_distribution(file_info_list, output_extension_size_file)
    write_keyword_frequency(file_info_list, output_keyword_file)

    print(f"File info logged to {output_log_file}")
    print(f"File summary logged to {output_summary_file}")
    print(f"Extension size distribution logged to {output_extension_size_file}")
    print(f"Keyword frequency logged to {output_keyword_file}")
except Exception as e:
    print(f"Error during processing: {e}")

# Additional reports can be generated similarly by processing the file_info_list