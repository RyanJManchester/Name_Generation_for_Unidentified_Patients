import sys

def remove_duplicates(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        unique_lines = []
        seen_lines = set()

        for line in lines:
            # Strip leading and trailing whitespaces
            cleaned_line = line.strip()

            # Check if the cleaned line has not been seen before
            if cleaned_line not in seen_lines:
                seen_lines.add(cleaned_line)
                unique_lines.append(line)

        with open(output_file, 'w') as file:
            file.writelines(unique_lines)

        print(f"Duplicates removed. Result saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")

if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    remove_duplicates(input_file_path, output_file_path)
