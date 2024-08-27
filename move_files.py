import os
import shutil

def move_all_files(src_folder, dest_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            src_file = os.path.join(root, file)
            if not os.path.isfile(src_file):
                continue
            # Ensure the destination directory exists
            os.makedirs(os.path.join(dest_folder, root[len(src_folder):]), exist_ok=True)
            dest_file = os.path.join(dest_folder, root[len(src_folder):], file)
            # If a file with the same name exists at the destination, append a unique suffix
            suffix = 0
            while os.path.exists(dest_file):
                suffix += 1
                filename, extension = os.path.splitext(file)
                dest_file = os.path.join(dest_folder, root[len(src_folder):], f"{filename}_{suffix}{extension}")
            shutil.move(src_file, dest_file)
            print(f'Moved {file} to {dest_file}')

# Replace with your actual folder paths
src_folder_path = '/Volumes/GW PICS/Google Photos/Videos'  # path to source flash drive
dest_folder_path = '/Volumes/KINGSTON/Movies'  # path to destination flash drive

move_all_files(src_folder_path, dest_folder_path)
