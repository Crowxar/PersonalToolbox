import os


def check_config():
    ...


def create_default_config():
    ...




# Define the path to the file you want to check
folder_name = "other_folder"
file_name = "file.txt"
file_path = os.path.join(folder_name, file_name)

# Check if the file exists
if os.path.exists(file_path):
    print(f"The file '{file_name}' exists in '{folder_name}'.")
else:
    print(f"The file '{file_name}' does not exist in '{folder_name}'.")