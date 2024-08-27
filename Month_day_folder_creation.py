import os
import datetime
import calendar

def create_monthly_folders(file_path):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # Determine the number of days in the current month
    _, num_days = calendar.monthrange(year, month)

    # Create folders for the remaining days of the month
    for day in range(day, num_days + 1):
        folder_name = f"{year}-{month:02d}-{day:02d}"
        folder_path = os.path.join(file_path, folder_name)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

# Usage example
file_path = "/Users/grahamward/Documents/Graham/Receipts/Jun"
create_monthly_folders(file_path)
