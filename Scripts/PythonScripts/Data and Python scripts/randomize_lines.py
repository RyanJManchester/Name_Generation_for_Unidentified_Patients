import sys
import random
from pathlib import Path



#get requested file into array.
output = open(sys.argv[1], "a")
array = Path(sys.argv[1]).read_text().split('\n')
#randomize w/random

random.shuffle(array)
#write back to same file.
output = open(sys.argv[1], "w")
output.write("\n".join(array))
output.close()
print(sys.argv[1] + " sorted.")