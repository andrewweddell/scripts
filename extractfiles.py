import os
import shutil

def move_files_recursively(source_folder, dest_folder):
    print(f"Processing folder: {source_folder}")  # Print the source folder being processed
    # Ensure the destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    file_count = 0  # Initialize the file counter

    # Loop through the subdirectories and files
    for item in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item)
        if os.path.isdir(item_path):
            # Recursively move files from the subfolder
            file_count += move_files_recursively(item_path, dest_folder)
        elif os.path.isfile(item_path):
            # Skip temporary files
            if not item.startswith("~$"):
                # Move the file to the destination folder
                shutil.move(item_path, os.path.join(dest_folder, item))
                print(f"Moved: {item}")  # Print the name of the moved file
                file_count += 1  # Increment the file counter

    return file_count

# Define the root folder and destination folder
root_folder = "/Users/andrewweddell/Downloads/2023"
dest_folder = "/Users/andrewweddell/Downloads/2023/MovedFiles"

# Call the function to move the files
total_files_moved = move_files_recursively(root_folder, dest_folder)
print(f"\nTotal number of files moved: {total_files_moved}")
