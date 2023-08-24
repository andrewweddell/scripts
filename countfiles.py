import os
import datetime

def log_subfolders_and_files(directory, log_dir):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    log_filename = f"log_{timestamp}.txt"
    log_filepath = os.path.join(log_dir, log_filename)
    
    total_files = 0
    with open(log_filepath, 'w') as log_file:
        log_file.write(f"Log file created on {datetime.datetime.now()}\n")
        log_file.write("=" * 80 + "\n")
        log_file.write(f"Directory: {directory}\n")
        log_file.write("=" * 80 + "\n")
        
        for root, dirs, files in os.walk(directory):
            for sub_dir in dirs:
                sub_dir_path = os.path.join(root, sub_dir)
                log_file.write(f"Subdirectory: {sub_dir_path}\n")
                
                sub_dir_files = []
                for sub_root, sub_dirs, sub_files in os.walk(sub_dir_path):
                    sub_dir_files.extend(sub_files)
                
                file_count = len(sub_dir_files)
                total_files += file_count
                
                log_file.write(f"File Count: {file_count}\n")
                for file_name in sub_dir_files:
                    log_file.write(f"File: {file_name}\n")
                log_file.write("=" * 80 + "\n")
        
        log_file.write(f"Total Files in All Subdirectories: {total_files}\n")

if __name__ == "__main__":
    directory = "/Users/andrewweddell/Pictures/Pictures" # Replace with your directory path
    log_dir = "/Users/andrewweddell/Documents/Support/Scripts/logs" # Replace with your log directory path
    log_subfolders_and_files(directory, log_dir)
