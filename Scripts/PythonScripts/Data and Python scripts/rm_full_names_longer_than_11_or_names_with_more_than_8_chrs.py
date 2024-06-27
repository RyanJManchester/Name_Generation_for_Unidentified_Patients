import sys
file_path = sys.argv[1]

# Read the content of the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Filter lines based on length criteria
filtered_lines = [line.strip() for line in lines if len(line) <= 13 and all(len(word) <= 8 for word in line.split())]

    
# Write the filtered content back to the same file
with open(file_path, 'w') as file:
    file.write('\n'.join(filtered_lines))

print(f"Lines removed based on criteria in {file_path}.")