import sys
from pathlib import Path

#get requested file into array.
output = open(sys.argv[1], "r")
array = Path(sys.argv[1]).read_text().split('\n')

def print_lines_containing_sequence(sequence):
        for line in array:
            if sequence in line.lower():
                print(line.strip())

if __name__ == "__main__":
    while True:
        user_input = input("Enter a sequence of letters (or 'exit' to quit): ").lower()
        print(user_input)
        print_lines_containing_sequence(user_input)
        if user_input.lower() == 'exit':
            break

