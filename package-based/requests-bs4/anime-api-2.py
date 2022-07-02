import requests
from random import choice
sfw = ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']
nsfw = ['waifu', 'neko', 'trap', 'blowjob']
types = ['sfw', 'nsfw']
types = choice(types)
if types == "sfw":
    cat = choice(sfw)
    link = f"https://api.waifu.pics/sfw/{cat}"
else:
    cat = choice(nsfw)
    link = f"https://api.waifu.pics/nsfw/{cat}"
    
link_ = requests.get(link)
link_ = link_.json()
print(link['url'])