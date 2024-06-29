import sys
from pathlib import Path


filterList = ["word_filters/full-list-of-bad-words_text-file_2022_05_05.txt", "word_filters/unfavorable_words.txt", "word_filters/summarised.txt"]

def mergeAndRemoveDupes(firstlist, seclist):
    for word in seclist:
        if word not in firstlist:
            firstlist.append(word)
    return firstlist

filtered = []
def clean(wordlist, filterlist):
    
    count = 0
    filteredoutput = []
    for word in wordlist:
        if word not in filterlist:
            goodword = True
            for bad in filterlist:
                if bad in word:
                    goodword = False
                    count += 1
                    print("removed " + word)
            if goodword:
                filteredoutput.append(word)
            else:
                filtered.append(word + ", ")
        else:
            filtered.append(word + ", ")
            print("removed " + word)
            count += 1
    print("identified " + str(count) + "words")
    return filteredoutput


#get requested file to filter into array.
words = Path(sys.argv[1]).read_text().split('\n')


filtered = []

for filter in filterList:
    slurs = Path(filter).read_text().split('\n')
    cleaned = clean(words, slurs)
    filtered = mergeAndRemoveDupes(filtered, cleaned)



filename = sys.argv[1].split('.')[0] + "_filtered.txt"
output = open(filename, "w")
output.write("\n".join(cleaned))
output.close()
print("filtered, removed " + str(len(words) - len(cleaned))  + " words. output = " + filename)
#print()
#print(filtered)