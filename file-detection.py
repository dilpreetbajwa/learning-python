"""
File Detection
"""

import os

file_path = "./test.txt"

if os.path.exists(file_path):
    print("File exists")

    if os.path.isfile(file_path):
        print("File is a file")
else:
    print("File does not exist")
