,eval
import requests
from bs4 import BeautifulSoup

songs = []
url = "https://www.last.fm/user/osho_2808"
r = requests.get(url)
soup = BeautifulSoup(r.content)
song_list = soup.find_all('a', class_ = "chartlist-play-button")
for song in song_list:
    songs.append(song)
s = str(songs[0])
ns = s.index("data-track-name")+17
ne = s.index("data-track-url")-2
ls = s.index('href')+6
le = ls+43
await event.respond(f"[{s[ns:ne]}]({str(s)[ls:le]})", link_preview=False)