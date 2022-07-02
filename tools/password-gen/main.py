
"""
• Make a new file 'used_pw.py'
<<<<Content>>>>
used = [
]
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
• Make a new file 'passwords.csv'
<<<<Content>>>>
email, password, site, time
use the same template as given
"""

import random as r
from used_pw import used
from datetime import datetime
import csv
from os import system

class Pw(object):
    s_alphabets = [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
                'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    b_alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
                'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+']
    sa_, ba_, n_, s_, length = 0, 0, 0, 0, 0



class InvalidInput(Exception):
    pass

def Email():
    email = input("Enter email >>>> ")
    return email

def Site():
    site = input("Enter site >>>> ")
    return site

def Password():
    pw = input("Enter password >>>> ")
    return pw

def gen_pw():
    pw = ""
    while Pw.length <= 16:
        type_ = r.choice(['s_alphabets', 'b_alphabets', 'numbers', 'symbols'])
        if type_ == 's_alphabets':
            Pw.sa_ += 1
            pw = pw+r.choice(Pw.s_alphabets)
        elif type_ == 'b_alphabets':
            Pw.ba_ += 1
            pw = pw+r.choice(Pw.b_alphabets)
        elif type_ == 'numbers':
            Pw.n_ += 1
            pw = pw+r.choice(Pw.numbers)
        elif type_ == 'symbols':
            Pw.s_ += 1
            pw = pw+r.choice(Pw.symbols)
        Pw.length += 1
        if Pw.length == 10:
            if pw in used:
                Pw.sa_, Pw.ba, Pw.n_, Pw.s_, Pw.length = 0, 0, 0, 0, 0
                pw = ""
            elif Pw.sa_ == 0 or Pw.ba_ == 0 or  Pw.n_ == 0 or Pw.s_ == 0:
                Pw.sa_, Pw.ba, Pw.n_, Pw.s_, Pw.length = 0, 0, 0, 0, 0
                pw = ""
    return pw


def pw_db(email, pw, site):
    return

def write_pw(pw, file_name='tools\\misc\\password-gen\\used_pw.py'):
    with open(file_name, 'r') as pw_file:
        lines = pw_file.readlines()
        lines[0] = lines[0]+f"r'{pw}',\n"
    with open(file_name, 'w') as pw_file:
        pw_file.writelines(lines)

def pw_csv(email, pw, site):
    file_name = 'tools\misc\password-gen\passwords.csv'
    with open(file_name) as csvfile:
        sets = csvfile.readlines()
        time = str(datetime.now())[0:19]
        sets[0] = sets[0]+f"{email}, {pw}, {site}, {time}\n"
    with open(file_name, 'w') as csvfile:
        csvfile.writelines(sets)
    write_pw(pw)

def add_pw(email, pw, site, time="Manually Added"):
    file_name = 'tools\misc\password-gen\passwords.csv'
    with open(file_name) as csvfile:
        sets = csvfile.readlines()
        sets[0] = sets[0]+f"{email}, {pw}, {site}, {time}\n"
    with open(file_name, 'w') as csvfile:
        csvfile.writelines(sets)

def get_pw(email, site):
    return

def main():
    print("""
<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>
Password Generator And Manager
<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>
    """)
    print("""What would you like to do:
1 • Generate password (Don't add to csv file)
2 • Generate password (Add to csv file)
3 • Add password
4 • Get a password 
""")
    def redo():
        global option
        try:
            option = int(input(">>> "))
            if option not in [1,2,3,4]:
                raise InvalidInput
        except InvalidInput:
            print("InvalidInput. Enter a valid input")
            redo()
        except ValueError:
            print("ValueError. Enter a integer value")
            redo()
        return option
    option = redo()
    if option == 1:
        print(f"Genrated password >>> {gen_pw()}")
        input("\nPress Enter to clear and exit...")
    system('cls')