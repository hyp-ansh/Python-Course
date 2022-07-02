import requests as r
from bs4 import BeautifulSoup
link = "https://kanojo-okarishimasu.com/manga/rent-a-girlfriend-chapter-22/"
link = r.get(link)
pages = []
soup = BeautifulSoup(link.content, "html5lib")
imgs = soup.find_all('img')
for img in imgs:
    if not img['src'].endswith('_1.png'):
        pages.append(img['src'].replace('\n', ''))
print(pages)