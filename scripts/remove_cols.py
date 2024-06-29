from pathlib import Path
import sys
#split inputted file into list of lines
lines = Path(sys.argv[1]).read_text().split('\n')
#empty list to hold vals
cleaned = []
#loop through each line appending wanted vals to new file

for line in lines:
    values = line.split(',')
    if '"' in values[3]:
        print(values[1])
    cleaned.append(values[3] + ", " + values[1])
#write to file
file = open((sys.argv[1].split(".")[0] + ".txt"), "a")
file.write("\n".join(cleaned))
file.close()