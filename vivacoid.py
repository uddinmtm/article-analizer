import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup

def getData(content):
    soup = BeautifulSoup(content, 'html.parser')
    content = soup.find(id="article-detail-content")
    text = content.get_text()

    lines = []
    xwords = ["googletag.cmd.push", "<!--", "-->", "\/\/", "OA_show"]
    pattern = r"|".join(xwords)

    for line in text.splitlines():
        if len(line.strip()) > 0:
            if re.search(pattern, str(line)) == None:
                lines.append(line)

    text = " ".join(lines)
    text = re.sub(u'\xa0', "", text).lower()
    text = re.sub(r'\,', "", text)
    text = re.sub(r'\.', " ", text)
    text = re.sub(r'\t|\"|\'', "", text).lower()
    title = soup.find("h1").get_text()
    words = text.split(" ")
    
    return[title, len(words)]