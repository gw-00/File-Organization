import os
import shutil

# Define file extensions for movies and images
movie_extensions = {'.mp4', '.MP4', '.avi', '.mov', '.MOV', '.mkv', '.flv', '.wmv'}
image_extensions = {'.jpeg', '.jpg', '.JPG', '.JPEG', '.png', '.PNG',  '.bmp', '.gif', '.GIF', '.tiff', '.ico', '.jfif', '.heic', '.HEIC', '.WEBP', '.webp'}

def move_files(src_folder, dest_folder_movies, dest_folder_images):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # Skip metadata files on macOS
            if file.startswith('._'):
                continue

            # Get the file extension
            filename, extension = os.path.splitext(file)
            
            # Check the file type and move accordingly
            if extension.lower() in movie_extensions:
                dest_folder = dest_folder_movies
            elif extension.lower() in image_extensions:
                dest_folder = dest_folder_images
            else:
                continue  # Skip files with unknown file types
            
            dest_file = os.path.join(dest_folder, file)

            # Check if file exists and append a unique suffix if it does
            suffix = 0
            while os.path.exists(dest_file):
                suffix += 1
                dest_file = os.path.join(dest_folder, f"{filename}_{suffix}{extension}")

            shutil.move(os.path.join(root, file), dest_file)
            print(f'Moved {file} to {dest_file}')
    
# Replace with your actual folder paths
src_folder_path = '/Volumes/Kingston/'
dest_folder_movies_path = '/Volumes/Kingston/Movies'
dest_folder_images_path = '/Volumes/Kingston/Images'

move_files(src_folder_path, dest_folder_movies_path, dest_folder_images_path)
