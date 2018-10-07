import requests
import re
import sys

def usage():
	print("""\n**** lfpscrape.py ****\n
[x] Usage: python lfpscrape.py (URI)
[x]
[x] Example: python lfpscrape.py http://example.com
[x]
[x] Url Format: http/https://(url)
[x]
[x] This tool scrapes local file paths from a given webpage.
[x] WARNING THIS MAY THROW FALSE POSITIVES
""")

def main(url):
    try:
    	response = requests.get(url)
	print("[x] Results")
    	for path in re.findall('"([^"]*)"', response.text):
		if(path[:2] == "//"):
			pass
		elif(path[:1] == "/"):
			print(path)
		elif(path[:2] == "./"):
			print(path)
		elif(path[:3] == "../"):
			print(path)
		elif("//" or "\\" or "<" or ">"in path):
			pass
		elif("/" in path):
			print(path)

    except Exception as e:
	print("[x] Encountered the following error")
	print(str(e))
    print("[x] Finished")


if __name__ == '__main__':
   if(len(sys.argv) != 2):
	usage()
   else:
      main(sys.argv[1])
