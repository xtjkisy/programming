
#1
import os

def create_specific_files(directory):
    # Define the list of specific file names
    file_names = ["Vito Corleone.txt", "Michael Corleone.txt", "Apollonia Vitelli-Corleone.txt"]
    
    # Iterate over each file name and create the corresponding file
    for file_name in file_names:
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as f:
            f.write("Sample content for " + file_name + "\n")
            f.write("You can add more content here if needed.\n")

def main():
    # Prompt the user to enter the directory path where files will be created
    directory = input("Enter the directory path where you want to create the files: ")

    # Check if the directory path exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist. Please provide a valid directory path.")
        return

    # Create the specific files in the specified directory
    create_specific_files(directory)
    print("Files created successfully in", directory)

if __name__ == "__main__":
    main()


-------------------------------------------------------------------------------------------------------------------------

#2

import os
import time
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, directory):
        super(FileChangeHandler, self).__init__()
        self.directory = directory

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"Detected file change: {event.src_path}")
        self.handle_file(event.src_path)

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"Detected new file: {event.src_path}")
        self.handle_file(event.src_path)

    def handle_file(self, filepath):
        search_pattern = input("Enter search pattern: ")
        search_method = input("Choose search method (1: String, 2: Regex): ")

        if search_method == "1":  
            self.search_string(filepath, search_pattern)
        elif search_method == "2":
            self.search_regex(filepath, search_pattern)
        else:
            print("Invalid search method choice.")

    def search_string(self, filepath, pattern):
        try:
            with open(filepath, 'r') as file:
                content = file.read()
                if pattern in content:
                    print(f"File {filepath} matches the search pattern.")
        except FileNotFoundError:
            print(f"Error: File {filepath} not found.")

    def search_regex(self, filepath, pattern):
        try:
            with open(filepath, 'r') as file:
                content = file.read()
                if re.search(pattern, content):
                    print(f"File {filepath} matches the regex pattern.")
        except FileNotFoundError:
            print(f"Error: File {filepath} not found.")

def monitor_directory(directory):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    event_handler = FileChangeHandler(directory)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    print(f"Monitoring directory: {directory}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    directory_to_watch = input("Enter directory to monitor: ")
    monitor_directory(directory_to_watch)

--------------------------------------------------------------------------------------------------------------------------

#3

import os

def get_file_size(path):
    """Return size of file in bytes."""
    return os.path.getsize(path)

def calculate_directory_size(directory):
    """Calculate total size of all files in a directory (including subdirectories)."""
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += get_file_size(filepath)
    return total_size

def list_files_and_directories(root_directory):
    """List all files with their sizes and paths, and directories with their total file size."""
    file_details = []  
    directory_details = {} 
    
    for dirpath, _, filenames in os.walk(root_directory):
        dir_total_size = sum(get_file_size(os.path.join(dirpath, filename)) for filename in filenames)
        directory_details[dirpath] = dir_total_size
        
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_size = get_file_size(filepath)
            file_details.append((file_size, filepath))
    
    file_details.sort(reverse=True, key=lambda x: x[0])
    
    sorted_directory_details = sorted(directory_details.items(), key=lambda x: x[1], reverse=True)
    
    return file_details, sorted_directory_details

def main():
    root_directory = input("Enter the root directory path: ")

    if not os.path.isdir(root_directory):
        print("Error: Invalid directory path.")
        return
  
    file_details, directory_details = list_files_and_directories(root_directory)
  
    print("\n--- Files sorted by size ---")
    for size, path in file_details:
        print(f"Size: {size} bytes | Path: {path}")
    
    
    print("\n--- Directories sorted by total file size ---")
    for dirpath, total_size in directory_details:
        print(f"Directory: {dirpath} | Total Size: {total_size} bytes")

if __name__ == "__main__":
    main()
------------------------------------------------------------------------------------------------------------------


#4


import os
import datetime

def delete_files_older_than(directory, days_limit):
    """
    Delete files older than the specified number of days from the given directory.

    Args:
        directory (str): Path to the directory from which to delete files.
        days_limit (int): Number of days indicating the age limit for file deletion.
    """
    try:
        current_time = datetime.datetime.now()

        cutoff_time = current_time - datetime.timedelta(days=days_limit)

        for root, dirs, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                file_stat = os.stat(file_path)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                if file_mtime < cutoff_time:
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
    
    except Exception as ex:
        print(f"Error: {ex}")

def main():
    directory = input("Enter the directory path: ")
    days_limit = int(input("Enter the file age limit (in days): "))

    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return
    delete_files_older_than(directory, days_limit)

if __name__ == "__main__":
    main()
-------------------------------------------------------------------------------------------------------------------


#5 

import zipfile
import os
import datetime

def add_files_to_zip(zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, 'a') as zipf:
            file_to_add = input("Enter the path of the file to add: ")
            if os.path.exists(file_to_add):
                zipf.write(file_to_add, os.path.basename(file_to_add))
                print(f"File '{file_to_add}' added to '{zip_filename}' successfully.")
            else:
                print(f"Error: File '{file_to_add}' does not exist.")
    except Exception as e:
        print(f"Error adding file to ZIP: {e}")

def list_files_in_zip(zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            file_list = zipf.namelist()
            if file_list:
                print(f"Files in '{zip_filename}':")
                for file in file_list:
                    print(file)
            else:
                print(f"No files found in '{zip_filename}'.")
    except Exception as e:
        print(f"Error listing files in ZIP: {e}")

def extract_files_from_zip(zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            file_to_extract = input("Enter the name of the file to extract: ")
            if file_to_extract in zipf.namelist():
                zipf.extract(file_to_extract)
                print(f"File '{file_to_extract}' extracted successfully.")
            else:
                print(f"Error: File '{file_to_extract}' not found in '{zip_filename}'.")
    except Exception as e:
        print(f"Error extracting file from ZIP: {e}")

def delete_file_from_zip(zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, 'a') as zipf:
            file_to_delete = input("Enter the name of the file to delete: ")
            if file_to_delete in zipf.namelist():
                zipf.extract(file_to_delete)
                print(f"File '{file_to_delete}' deleted successfully from '{zip_filename}'.")
            else:
                print(f"Error: File '{file_to_delete}' not found in '{zip_filename}'.")
    except Exception as e:
        print(f"Error deleting file from ZIP: {e}")

def display_menu():
    print("\nZIP File Manager Menu:")
    print("1. Add file to ZIP")
    print("2. List files in ZIP")
    print("3. Extract file from ZIP")
    print("4. Delete file from ZIP")
    print("5. Exit")

def main():
    zip_filename = input("Enter the path to the ZIP file: ")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_files_to_zip(zip_filename)
        elif choice == '2':
            list_files_in_zip(zip_filename)
        elif choice == '3':
            extract_files_from_zip(zip_filename)
        elif choice == '4':
            delete_file_from_zip(zip_filename)
        elif choice == '5':
            print("Exiting ZIP File Manager.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
------------------------------------------------------------------------------------------------------------------------

#6

import csv
import json
import logging
from datetime import datetime

def validate_csv_row(row):
    """
    Validate a CSV row based on specified criteria.
    Returns True if the row is valid, False otherwise.
    """
    try:
        datetime.strptime(row[0], '%Y-%m-%d')

        if int(row[1]) <= 0:
            return False

        if not row[2].strip():
            return False

        return True

    except ValueError:
        return False

def convert_csv_to_json(csv_file, json_file, error_log_file):
    """
    Convert a CSV file to a JSON file, validating each row.
    Write validation errors to the error log file.
    """
    valid_data = []
    error_messages = []

    with open(csv_file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader) 

        for row in csv_reader:
            if validate_csv_row(row):
                valid_data.append({
                    "date": row[0],
                    "quantity": int(row[1]),
                    "description": row[2]
                })
            else:
                error_messages.append(f"Invalid row: {', '.join(row)}")

    with open(json_file, 'w') as jsonfile:
        json.dump(valid_data, jsonfile, indent=4)

    with open(error_log_file, 'w') as log_file:
        for error_message in error_messages:
            log_file.write(error_message + '\n')

def main():
    csv_file = input("Enter the path to the CSV file: ")
    json_file = input("Enter the path for the output JSON file: ")
    error_log_file = input("Enter the path for the error log file: ")

    convert_csv_to_json(csv_file, json_file, error_log_file)
    print("Conversion complete. JSON file and error log generated.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

