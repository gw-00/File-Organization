import os
import random

# Function to securely delete a file by overwriting its contents
def secure_delete_file(file_path):
    with open(file_path, "rb+") as file:
        file_size = os.path.getsize(file_path)
        file.seek(0)
        file.write(os.urandom(file_size))  # Overwrite the file with random data
        file.flush()
        os.fsync(file.fileno())  # Ensure the changes are flushed to disk

        # Truncate the file to a random size
        random_size = random.randint(0, file_size)
        file.truncate(random_size)
        file.flush()
        os.fsync(file.fileno())

        # Repeat the overwrite and truncate process multiple times
        num_iterations = 10  # Number of secure deletion passes
        for _ in range(num_iterations):
            file.seek(0)
            file.write(os.urandom(random_size))  # Overwrite the file with random data
            file.flush()
            os.fsync(file.fileno())

            random_size = random.randint(0, random_size)
            file.truncate(random_size)
            file.flush()
            os.fsync(file.fileno())

    # Remove the file from the file system
    os.remove(file_path)

# Example usage:
file_path = "/Users/grahamward/Desktop/Passwords.csv"
secure_delete_file(file_path)
