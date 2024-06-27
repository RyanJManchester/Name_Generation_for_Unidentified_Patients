from pathlib import Path
import sys
import random

if (len(sys.argv) != 4):
    print("usage = <input_first> <input_last> <output_file_name>")
else:
        
    #----parse script inputs-------------------
    first_file = sys.argv[1]
    sec_file = sys.argv[2]


    #--Functions-------------------------------
    def returnListFromFile(filename):
        txt = Path(filename).read_text()
        return txt.split('\n')

    def combine(a, b):
        combined = []
        for first in a[0:len(a) - 1]:
            for last in b[0:len(b) - 1]:
                combined.append(first + " " + last)
        return combined
        
    #-- Script --------------------------------

    #bring the lists in - 
        # lists to be used as a base
    prefixes = returnListFromFile(first_file)
    print("processed " + first_file + "into list.")
    suffixes = returnListFromFile(sec_file)
    print("processed " + sec_file + " into list.")

    final_list = []

    #if len(prefixes) < len (suffixes):
    final_list = combine(prefixes, suffixes)
    #else:
    #   final_list = combine(suffixes, prefixes)

    random.shuffle(final_list)
    print("\n".join(final_list))
    # "a" specifies that it will overwrite any existing content.


    output = sys.argv[3] + ".txt"    
    file = open(output, "a")
    print(output)
    file.write("\n".join(final_list))
    file.close()
