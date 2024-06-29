from pathlib import Path
import sys
import random

#----parse script inputs-------------------
first_file = sys.argv[1]
sec_file = sys.argv[2]


#--Functions-------------------------------
def returnListFromFile(filename):
    txt = Path(filename).read_text()
    return txt.split('\n')

def mergeAndRemoveDupes(firstlist, seclist):
    for word in seclist:
        if word not in firstlist:
            firstlist.append(word)
    return firstlist




wordlist = mergeAndRemoveDupes(returnListFromFile(first_file), returnListFromFile(sec_file))

output = open(first_file + "_summarised_.txt", "w")
output.write("\n".join(wordlist))
output.close()