import mysql.connector as sql
import os, random
from colorama import Fore
# ToDo update{username,password,name} delete {account}
pysever = sql.connect(host="localhost",
                      user="root",
                      passwd="1234",
                      database="python")
cmd = pysever.cursor()
register_query = "INSERT IGNORE INTO users (username, name, pass) VALUES (%s, %s, %s)"


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clr()

cy = Fore.CYAN
m = Fore.GREEN
reset = Fore.RESET
logo = r"""
  ____                        ___      _             ____        _ 
 |  _ \  _____   __          / _ \ ___| |__   ___   |  _ \ __ _ (_)
 | | | |/ _ \ \ / /  _____  | | | / __| '_ \ / _ \  | |_) / _` || |
 | |_| |  __/\ V /  |_____| | |_| \__ \ | | | (_) | |  _ < (_| || |
 |____/ \___| \_/            \___/|___/_| |_|\___/  |_| \_\__,_|/ |
                                                               |__/ 
"""
print(f'{cy}{logo}')
option = r"""
╦═╗┌─┐┌─┐┬┌─┐┌┬┐┌─┐┬─┐  ┌─┐┬─┐  ╦  ┌─┐┌─┐┬┌┐┌
╠╦╝├┤ │ ┬│└─┐ │ ├┤ ├┬┘  │ │├┬┘  ║  │ ││ ┬││││
╩╚═└─┘└─┘┴└─┘ ┴ └─┘┴└─  └─┘┴└─  ╩═╝└─┘└─┘┴┘└┘
"""



print(f"{m}{option}")
print(f"{reset}")

def login():
    print("\n<<<Login>>>\n")
    username = str(input("Username : "))
    cmd.execute("SELECT pass FROM users WHERE username=%s", (username,))
    saved_pass = cmd.fetchall()
    if saved_pass:
        password = str(input("Password : "))
        saved_pass = cmd.execute("SELECT pass FROM users WHERE username=%s", (username,))
        print(saved_pass)
    else:
        retry = str(input("Username doesn't exists\nWould you like to login again or register[L/R] : ").upper())
        if retry == "L":
            login()
        elif retry == "R":
            register()


def register():
    def savepw():
        if password != confirm:
            print("Invalid Credentials [PASSWORD]\n\n")
            register()
        else:
            values = (username, name, password)
            cmd.execute(register_query, values)
            pysever.commit()
            if cmd.rowcount == 1:
                print("Account created!!\n")
            else:
                print("Username already exists. \n")
                register()

    print("\n<<<Register>>>\n")
    username = (str(input("Username : ")))
    if len(username) > 20 or len(username) < 6:
        print("Username must be within 6-20 characters.\n")
        register()
    else:
        name = str(input("Name : "))
        if len(name) > 255:
            print("Name can't exceed 255 characters.\n")
            register()
        else:
            password = str(input("Password : "))
            if len(password) < 8 or len(password) > 64:
                print("Password must be from 8-64 chars.\n")
                register()
            elif password == "password":
                print("Password can't be 'password'")
                register()
            else:
                confirm = str(input("Confirm Password : "))
                savepw()


def choice():
    option = str(input("[R/L] : "))
    if option == "R" or option == "r":
        register()
    elif option == "L" or option == "l":
        login()
    else:
        print("<INVALID INPUT>")
        choice()


choice()
