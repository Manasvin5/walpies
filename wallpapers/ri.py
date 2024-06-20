import os
import re

# Define the folder path
folder_path = '/home/mana/Pictures/walpies'

# Get list of all files in the folder
files = os.listdir(folder_path)

# Filter out only the .png files
png_files = [file for file in files if file.endswith('.png')]

# Function to extract numbers from file names
def extract_number(file_name):
    match = re.search(r'(\d+)', file_name)
    return int(match.group(1)) if match else 0

# Sort files based on the number extracted from their names
png_files.sort(key=extract_number)

# Rename the files sequentially
for index, file_name in enumerate(png_files, start=1):
    new_name = f"{index}.png"
    old_path = os.path.join(folder_path, file_name)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed: {file_name} -> {new_name}")

print("Renaming completed.")
