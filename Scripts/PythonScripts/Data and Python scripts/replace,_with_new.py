import sys
file_path = sys.argv[1]

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Replace ", " with a newline character
modified_content = content.replace(", ", "\n")

# Write the modified content back to the same file
with open(file_path, 'w') as file:
    file.write(modified_content)

print(f"Replacement completed in {file_path}.")