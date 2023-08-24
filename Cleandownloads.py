import os
import shutil
from datetime import datetime

downloads_path = os.path.expanduser('~/Downloads')  # Define the path to your downloads folder
destination_path = '/Users/andrewweddell/Documents'  # Define the path to the destination folder
pictures_path = '/Users/andrewweddell/Pictures'  # Define the path to the pictures folder
log_folder = os.path.join(destination_path, 'logs')  # Define the path to the logs folder
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

def classify_file(file_extension):
    """Classify file based on its extension."""
    images = ['.jpg', '.jpeg', '.png', '.gif']
    documents = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt']
    videos = ['.mp4', '.mkv', '.avi', '.flv']
    if file_extension in images:
        return 'Images'
    elif file_extension in documents:
        return 'Documents'
    elif file_extension in videos:
        return 'Videos'
    else:
        return 'Others'

moved_files = []

for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    if os.path.isfile(file_path):
        # Get the modification date of the file
        modification_time = os.path.getmtime(file_path)
        modification_date = datetime.fromtimestamp(modification_time)
        
        # Create folder structure based on modification date
        file_extension = os.path.splitext(filename)[1]
        file_type = classify_file(file_extension)
        
        if file_type == 'Images':
            destination_folder = os.path.join(pictures_path, str(modification_date.year))
        else:
            destination_folder = os.path.join(destination_path, str(modification_date.year), file_type)
        
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        # Handle large files (greater than 10 MB)
        file_size = os.path.getsize(file_path)
        if file_size > 10 * 1024 * 1024:  # 10 MB in bytes
            large_files_folder = os.path.join(destination_path, 'Large Files')
            if not os.path.exists(large_files_folder):
                os.makedirs(large_files_folder)
            shutil.move(file_path, os.path.join(large_files_folder, filename))
            moved_files.append(filename)
            continue  # Skip remaining processing for this file
        
        # Move file to appropriate folder
        shutil.move(file_path, os.path.join(destination_folder, filename))
        moved_files.append(filename)

# Print the count and names of the files moved
print(f"Total files moved: {len(moved_files)}")
print("Files moved:")
for file_name in moved_files:
    print(file_name)

# Write the results to a text file in the logs folder
current_date = datetime.now().strftime("%Y-%m-%d")
with open(os.path.join(log_folder, f'moved_files_{current_date}.txt'), 'w') as log_file:
    log_file.write(f"Total files moved: {len(moved_files)}\n")
    log_file.write("Files moved:\n")
    for file_name in moved_files:
        log_file.write(f"{file_name}\n")
