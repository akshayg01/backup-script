import os
import shutil
from datetime import datetime

def backup_folders(src, dest, exclude=None,createDateFolder=True):
    if exclude is None:
        exclude = []

    if createDateFolder:
        # Get today's date in yyyy-mm-dd format
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Create the backup directory with today's date
        backup_dir = os.path.join(dest, today)
        os.makedirs(backup_dir, exist_ok=True)
    else:
        backup_dir = dest
        
    # Walk through the source directory
    for root, dirs, files in os.walk(src):
        # Skip directories in the exclude list
        dirs[:] = [d for d in dirs if d not in exclude]
        
        # Determine the relative path and construct the corresponding path in the backup directory
        rel_path = os.path.relpath(root, src)
        dest_path = os.path.join(backup_dir, rel_path)
        
        # Create the destination directory if it doesn't exist
        os.makedirs(dest_path, exist_ok=True)
        
        # Copy files
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)
            shutil.copy2(src_file, dest_file)
            print(f'Copied {src_file} to {dest_file}')

if __name__ == '__main__':
    # Configuration
    
    source_folder = 'D:\\workspace\\ai-search-demo'  # Example source folder path
    destination_folder = 'D:\\workspace\\backup'  # Example destination folder path
    folders_to_skip = ['node_modules', '.git', '__pycache__', 'backend_env', '.azure', '.github','.vscode','data','docs']  # Folders to skip


    backup_folders(source_folder, destination_folder, folders_to_skip,False)
