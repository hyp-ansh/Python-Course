"""
import os
import time
import pyautogui as gui
import subprocess
import sys
import speech_recognition as sr
import contextlib
import random
from datetime import datetime
with contextlib.redirect_stdout(None):
    import pygame
    from pygame import mixer
import keyboard
import webbrowser as web
from youtubesearchpython import VideosSearch, Playlist
import requests as req
from bs4 import BeautifulSoup
import screen_brightness_control as sbc
import win32gui
import win32con
import randomstuff
from pydub import AudioSegment
from pydub.playback import play
"""

"""
import urllib.parse as up
import psycopg2

up.uses_netloc.append("postgres")
url = up.urlparse('postgres://qztlpnum:oh_0gqcd9spr7MzT4OFfMG-nMUFAykUm@chunee.db.elephantsql.com/qztlpnum')
fridaydb = psycopg2.connect(database=url.path[1:],
                        user=url.username,
                        password=url.password,
                        host=url.hostname,
                        port=url.port
                        )
call_query = fridaydb.cursor()
call_query.execute('select * from test')
names = call_query.fetchone()
new_name = "'david'"
for old_name in names:
    old_name = f"'{old_name}'"
    call_query.execute(f"UPDATE test SET name={new_name} WHERE name={old_name}")
call_query.execute('select * from test')
a = call_query.fetchone()
print(a)
call_query.close()
"""
