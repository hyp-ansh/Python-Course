import requests
from random import randint, choice
while True:
    no = str(randint(1,1000))
    if len(no) == 1:
        no = "00"+no
    elif len(no) == 2:
        no = "0"+no
    types= ['baka', 'bite', 'blush', 'bored', 'cry', 'cuddle', 'dance', 'facepalm', 'feed', 'happy', 'highfive', 'hug', 'kiss', 'laugh', 'pat', 'poke', 'pout', 'shrug', 'slap', 'sleep', 'smile', 'smug', 'stare', 'think', 'thumbsup', 'tickle', 'wave', 'wink']

    link = f"https://nekos.best/api/v1/{choice(types)}/{no}.gif"
    link_ = requests.get(link)
    if link_.ok:
        break
print(link)
