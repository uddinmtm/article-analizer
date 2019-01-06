import requests
import sys
import detikcom
import vivacoid

def getHostname(url):
    tmp = url.split('://', 1)
    _tmp = tmp[1].split('/', 1)
    return _tmp[0]

opt = sys.argv
if len(opt) <= 1:
    print("Url not found")
    sys.exit()

url = opt[1]
host = getHostname(url)
page = requests.get(url)

if host == "www.viva.co.id":
    title, word = vivacoid.getData(page.content)
elif host == "news.detik.com":
    title, word = detikcom.getData(page.content)

print("Host :", host)
print("Url :", url)
print("Judul berita :", title)
print("Terdiri dari sekitar", word, "kata")
