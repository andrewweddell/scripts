import os
import shutil
from datetime import datetime

# Set the path to your pictures folder
pictures_folder = "/Users/andrewweddell/Pictures/Pictures"
large_files_folder = os.path.join(pictures_folder, "Large Files")
empty_folder = os.path.join(pictures_folder, "Empty")
file_size_limit = 100 * 1024 * 1024  # 100 MB
current_date = datetime.now().strftime('%Y%m%d%H%M%S')
log_file_path = f"/Users/andrewweddell/Documents/Support/Scripts/pictures_log_{current_date}.txt"

# Ensure the large files folder and empty folder exist
if not os.path.exists(large_files_folder):
    os.makedirs(large_files_folder)
if not os.path.exists(empty_folder):
    os.makedirs(empty_folder)

def move_file_with_unique_name(src, dst):
    # Generate a unique filename by appending '_dup' if necessary
    if os.path.exists(dst):
        base, ext = os.path.splitext(dst)
        i = 1
        while os.path.exists(f"{base}_dup{i}{ext}"):
            i += 1
        dst = f"{base}_dup{i}{ext}"
    shutil.move(src, dst)

# Write to the log file
def write_log(log_message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message + '\n')
    print(log_message)

# Walk through the directory structure
for dirpath, dirnames, filenames in os.walk(pictures_folder):
    initial_count = len(filenames)
    write_log(f"\nFolder '{dirpath}' initially has {initial_count} files.")
    
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_size = os.path.getsize(file_path)
        
        # Check if the file is larger than the limit
        if file_size > file_size_limit:
            move_file_with_unique_name(file_path, os.path.join(large_files_folder, filename))
            write_log(f"Moved '{filename}' to 'Large Files' folder.")
            continue
        
        # Get the creation date of the file
        creation_timestamp = os.stat(file_path).st_birthtime
        creation_date = datetime.fromtimestamp(creation_timestamp)
        
        # Create the folder name based on the creation date
        folder_name = creation_date.strftime("%Y-%m-%d")
        new_folder_path = os.path.join(pictures_folder, folder_name)
        
        # Ensure the new folder exists
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        
        # Move the file to the new folder
        move_file_with_unique_name(file_path, os.path.join(new_folder_path, filename))
        write_log(f"Moved '{filename}' to '{folder_name}' folder.")
    
    final_count = len(os.listdir(dirpath))
    write_log(f"Folder '{dirpath}' now has {final_count} files.\n")

# Check for empty folders and move them to the 'Empty' folder
for dirpath, dirnames, filenames in os.walk(pictures_folder):
    if not dirnames and not filenames and dirpath != empty_folder:
        new_empty_folder_path = os.path.join(empty_folder, os.path.basename(dirpath))
        move_file_with_unique_name(dirpath, new_empty_folder_path)
        write_log(f"Moved empty folder '{dirpath}' to 'Empty' folder.")

write_log("Pictures have been organized.")
