import sys
file_path = sys.argv[1]

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.readlines()

# Sort the lines alphabetically
sorted_content = sorted(content)

# Write the sorted content back to the same file
with open(file_path, 'w') as file:
    file.writelines(sorted_content)

print(f"File sorted alphabetically: {file_path}.")
