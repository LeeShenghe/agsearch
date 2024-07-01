import os
import sys
import re

def search_pattern_in_file(pattern, file_path):
    with open(file_path, 'r', errors='ignore') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if re.search(pattern, line):
                print(f"{file_path}:{line_number}:{line.strip()}")

def search_pattern_in_directory(pattern, directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            search_pattern_in_file(pattern, file_path)

def main():
    if len(sys.argv) < 2:
        print("Usage: ag PATTERN [PATH]")
        return

    pattern = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "."

    if os.path.isdir(path):
        search_pattern_in_directory(pattern, path)
    elif os.path.isfile(path):
        search_pattern_in_file(pattern, path)
    else:
        print(f"Error: {path} is not a valid file or directory")

if __name__ == "__main__":
    main()
