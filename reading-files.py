"""
Reading files
"""

file_path = "output.txt"

try:
    with open(file_path, "r") as file:
        txt_data = file.read()
        print(f"Data read from {file_path}: {txt_data}")
except FileNotFoundError:
    print(f"File {file_path} not found")
except PermissionError:
    print(f"Permission denied for file {file_path}")
