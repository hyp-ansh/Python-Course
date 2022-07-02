#TODO next previous [pause if possible]
import os
import time
import sys
import subprocess as cmd
import random as r
import keyboard
playing_msg = """
  ___ __  __ ___    ___ _                   
 / __|  \/  |   \  | _ \ |__ _ _  _ ___ _ _ 
| (__| |\/| | |) | |  _/ / _` | || / -_) '_|
 \___|_|  |_|___/  |_| |_\__,_|\_, \___|_|  
                               |__/         
            
[-[-[-[-[ Currently Playing ]-]-]-]-]

{}"""
cdir = os.getcwd()
dir = os.listdir(cdir)
played = []
all_songs = []
for _ in dir:
    if _.endswith(".mp3"):
        each = r.choice(dir)
        all_songs.append(each)
        dir.remove(each)

def play(song):
    try:
        os.system("cls")
        played.append(song)
        all_songs.remove(song)
        print(playing_msg.format(song), end="\r")
        cmd.run(["play", f"{song}"], capture_output=True, shell=True)
    except KeyboardInterrupt:
        print("\nStopping Player...\n")
        time.sleep(3)
        os.system("cls")
        sys.exit()       

def shuffle(all_songs):
    while True:
        try:
            song = r.choice(all_songs)
            play(song)
        except IndexError:
            print("Playlist Ended")
            time.sleep(10)
            os.system("cls")
            break
        

shuffle(all_songs)
