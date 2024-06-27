import sys
count = 0

def count_lines_by_first_character(file_path):
    # Initialize a dictionary to store the counts for each character
    character_counts = {}
    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            count += 1
            # Remove leading and trailing whitespaces
            line = line.strip()

            # Check if the line is not empty
            if line:
                # Get the first character of the line
                first_character = line[0].lower()  # Convert to lowercase for case-insensitivity

                # Update the count for the first character in the dictionary
                character_counts[first_character] = character_counts.get(first_character, 0) + 1

    return character_counts

# Example usage:
file_path = sys.argv[1]
result = count_lines_by_first_character(file_path)
print("")
print(f" '{sys.argv[1]}' - total lines: '{count}" )
print(f" '{sys.argv[1]}' - count for each letter:")
# Print the result
for char, count in result.items():
    print(f"'{char}': {count}", end=" ")
