import os
import shutil

# Define folder names
source_folder = "source_folder"
destination_folder = "destination_folder"

# Step 1: Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

moved_count = 0

# Step 2: Check if source_folder exists and process files
if os.path.exists(source_folder):
    for file in os.listdir(source_folder):
        # Check if the file is a JPG image
        if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            # Move the file to destination_folder
            shutil.move(source_path, destination_path)
            print(f"Moved: {file}")
            moved_count += 1

    if moved_count > 0:
        print(f"\nSuccessfully moved {moved_count} JPG file(s) to '{destination_folder}'!")
    else:
        print(f"\nNo .jpg files found inside '{source_folder}' to move.")
else:
    print(f"Error: '{source_folder}' does not exist. Please make sure the folder is created.")