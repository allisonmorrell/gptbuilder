import glob
import os

# Get list of all .md files
md_files = glob.glob('better-gpt-builder/files/*.md')

for file_path in md_files:
    with open(file_path, 'r') as file:
        content = file.read()
        filename = os.path.basename(file_path)
        print(f"Filename: {filename} - Characters: {len(content)}")
        if len(content) > 500:
            print("OVER")