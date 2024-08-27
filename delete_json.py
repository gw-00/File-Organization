import os

def delete_json_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f'Deleted {file_path}')

# Replace 'your_flash_drive_path' with the path to your flash drive.
delete_json_files('/Volumes/GW PICS')
