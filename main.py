import requests
import sys
import detikcom

opt = sys.argv
if len(opt) <= 1:
    print("Url not found")
    sys.exit()

url = opt[1]
page = requests.get(url)
title, word = detikcom.getData(page.content)

print("Url :", url)
print("Judul berita :", title)
print("Terdiri dari sekitar", word, "kata")
