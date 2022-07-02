import time
import requests
from subprocess import run
from shutil import move

def Run(cmd):
    cmd = cmd.split(" ")
    run(cmd, capture_output=True, shell=True)

class UP(object):
    def Pic(img):
        r = requests.post(
        "https://api.deepai.org/api/waifu2x",
        files={'image': open(img, 'rb'),},
        headers={'api-key': '39678a25-4960-41ea-9bd7-4c8bbc4740eb'}
        )
        output = r.json()['output_url']
        return output 
        
    def Link(link):
        r = requests.post(
        "https://api.deepai.org/api/waifu2x",
        data={
            'image': link,
        },
        headers={'api-key': '39678a25-4960-41ea-9bd7-4c8bbc4740eb'}
        )
        output = r.json()['output_url']
        return output
    Input = input("Image Path/Link <> ")
    Input = Input.replace("\"", "")
    if "https" in Input: output = Link(Input)
    else: output = Pic(Input)

file_name =  time.strftime("%Y_%m_%d_%H_%M_%S.png")
Run(f"wget -O {file_name} {UP.output}")
move(f"{file_name}", f"D:/Upscaled/{file_name}")