import requests
import os
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import sys

def emptyLine(line):
    return len(line.strip()) == 0
    
def haveWords(line):
    xwords = ["googletag.cmd.push", "<!--", "-->", "\/\/", "OA_show"]
    pattern = r"|".join(xwords)
    return not re.search(pattern, str(line)) == None

def sterilization(line):
    line = re.sub(r'\,\.', " ", line)
    return re.sub(r'[\t\"]', "", line).lower()

opt = sys.argv
if len(opt) <= 1:
    print("Url not found")
    sys.exit()

url = opt[1]
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find(id="detikdetailtext")
text = content.get_text()

# remove empty line & googletag
lines = []
for line in text.splitlines():
    if not emptyLine(line):
        if not haveWords(line):
            lines.append(line)

text = " ".join(lines)
text = sterilization(text)
words = text.split(" ")

print("Url :", url)
print("Judul berita :", soup.find("h1").get_text())
print("Terdiri dari sekitar", len(words), "kata")
