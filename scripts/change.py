import sys

input_file_path = sys.argv[1]
output_file_path = "output.txt"

with open(input_file_path, 'r') as input_file:
    content = input_file.read()

content_with_newlines = content.replace(' ', '\n')

with open(output_file_path, 'w') as output_file:
    output_file.write(content_with_newlines)

print(f"Spaces in {input_file_path} replaced with newlines. Result saved to {output_file_path}.")
