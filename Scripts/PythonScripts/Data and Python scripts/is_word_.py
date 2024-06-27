import requests
import sys
import json

api_url = "https://en.wiktionary.org/w/api.php?action=query&titles=" + sys.argv[1] + "&format=json"
response = requests.get(api_url).json()['query']['pages']


offensive_url = "https://en.wiktionary.org/w/api.php?action=parse&page=" + sys.argv[1] + "&section=1&prop=wikitext&format=json"
#isOffensive = (requests.get(offensive_url).json()['parse']['wikitext']['*'])
#print(isOffensive)

if (list(response.keys())[0] != '-1') :
    print(sys.argv[1] + " is a word")
else:
    print(sys.argv[1] + " not a word!")

# if (isOffensive):
#     print("and is offensive")
# else:
#     print("not offensive")