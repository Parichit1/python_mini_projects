import os
import shutil


def create_subfolder(folder_path, sub_folder_name):
    sub_folder_path = os.path.join(folder_path, sub_folder_name)
    if not os.path.exists(sub_folder_path):
        os.makedirs(sub_folder_path)
    return sub_folder_path


def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                sub_folder_name = f"{file_extension} Files"
                sub_folder_path = create_subfolder(
                    folder_path, sub_folder_name)
                file_path = os.path.join(folder_path, filename)
                shutil.move(file_path, sub_folder_path)
                print(f"Moved: {filename} to {sub_folder_name}")


if __name__ == "__main__":
    print("Desktop Cleaner")
    folder_path = '/Users/psrichitupadhayay836gmailcom/Desktop/trial '  # your file path

    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning complete")
    else:
        print("Invalid folder path. Please enter a correct path")
