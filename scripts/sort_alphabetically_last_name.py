import sys

file = sys.argv[1]
lines = open(file, "r").readlines()


def sort_by_last_name(lines):
    # Split each line into first name and last name
    names = [line.split() for line in lines]

    # Sort the names based on the last name (index 1)
    sorted_names = sorted(names, key=lambda x: x[1])

    return sorted_names

def main():
    # Read lines from a file
    input_file_path = sys.argv[1]  # Change this to your input file path

    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Sort the lines by last name
    sorted_names = sort_by_last_name(lines)

    # Save the sorted names to a new file
    with open(input_file_path, 'w') as output_file:
        for name in sorted_names:
            output_file.write(" ".join(name) + '\n')


if __name__ == "__main__":
    main()


