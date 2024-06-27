import requests
import sys

url = "https://keyword-difficulty.p.rapidapi.com/data"
#request = sys.argv[1]
payload = {
	"keyword": "request",
	"search_engine": "google"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "83bbe23608mshe982a46039ab5a2p1fededjsn7e6855413332",
	"X-RapidAPI-Host": "keyword-difficulty.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())


# "a" specifies that it will overwrite any existing content.
output = open(sys.argv[3] + "_" + sys.argv[2] + "_sum.txt", "w")
output.write("\n".join(final_list))
output.close()
