import urllib
import time
from bs4 import BeautifulSoup

link = "https://anilist.co/user/iOsho/animelist/Planning"

header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
          "X-Requested-With": "XMLHttpRequest"}
page = urllib.request.Request(link, headers=header, cookies={
                              '__test': '2501c0bc9fd535a3dc831e57dc8b1eb0'})
result = urllib.request.urlopen(page)
resulttext = result.read()
soup = BeautifulSoup(result, "html.parser")
print(resulttext)
anime_list = soup.find_all('div', class_ = "list-entries")
anime_name = soup.find_all('div', class_ = "title")
# print(anime_list)
for _ in anime_name:
    print(_.text)
