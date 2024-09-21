"""
Writing files
"""

txt_data = "Hello, World!"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"Data written to {file_path}")
