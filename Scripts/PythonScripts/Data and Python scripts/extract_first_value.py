import sys
def extract_caps_strings(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()

        extracted_caps_strings = [word.strip() for line in lines for word in line.split(',') if word.isupper()]

        with open(input_file_path, 'w') as file:
            file.write('\n'.join(extracted_caps_strings))

        print(f"Extraction and rewriting completed successfully for {input_file_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage
input_file_path = sys.argv[1]  # Replace with the path to your input file
extract_caps_strings(input_file_path)