import os
import shutil


def move_files_based_on_trim(source_folder, destination_folder):
    # Ensure the source and destination folders exist
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    if not os.path.exists(destination_folder):
        print(f"Destination folder '{
              destination_folder}' does not exist. Creating it...")
        os.makedirs(destination_folder)

    # Recursively iterate through files in the source folder and its subfolders
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            source_path = os.path.join(root, filename)

            # Check if the file name ends with "Trim.mp4"
            if filename.endswith("Trim.mp4"):
                destination_path = os.path.join(destination_folder, filename)

                # Move the file to the destination folder
                shutil.move(source_path, destination_path)

                print(f"Moved '{filename}' to '{destination_folder}'.")


if __name__ == "__main__":
    # Set the source folder to the Downloads folder
    source_folder = r"c:\Users\Anan\Downloads"

    # Replace this path with your actual destination folder path
    destination_folder = r"c:\Users\Anan\Desktop\redirect"

    move_files_based_on_trim(source_folder, destination_folder)
