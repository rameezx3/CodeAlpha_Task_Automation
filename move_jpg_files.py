import os
import shutil

# Step 1: Source folder (where JPG files are present)
source_folder = "source_images"

# Step 2: Destination folder (where JPG files will be moved)
destination_folder = "jpg_images"

# Step 3: Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Step 4: Loop through files in source folder
for file_name in os.listdir(source_folder):
    # Check if file ends with .jpg
    if file_name.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Move file
        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name}")

print("\nTask completed successfully!")
print("All .jpg files have been moved.")
