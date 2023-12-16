import os
import zipfile

def unzip_all_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            filepath = os.path.join(directory, filename)
            with zipfile.ZipFile(filepath, "r") as zip_ref:
                zip_ref.extractall(directory)
                print(f"Unzipped: {filepath}")

# Specify the directory where the zip files are located
directory_path = "/home/easgrad/ninadnar/cse666/data"

# Call the function to unzip all files in the directory
unzip_all_files(directory_path)