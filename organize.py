import os
import shutil

def organize_by_extension(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext[1:].lower() if ext else "no_extension"

        dest_folder = os.path.join(folder_path, ext)
        os.makedirs(dest_folder, exist_ok=True)

        dest_path = os.path.join(dest_folder, filename)
        shutil.copy2(file_path, dest_path)

        print(f"Copied: {filename} -> {dest_folder}")

    print("\n All files have been organized by extension.")

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize_by_extension(folder)
