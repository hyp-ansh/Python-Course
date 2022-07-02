import mysql.connector as sql

server = sql.connect(host="localhost",
                     user="root",
                     passwd="1234",
                     database="test")
cmd = server.cursor()
query = "INSERT IGNORE INTO users (username, pass) VALUES (%s, %s)"


def register():
    username = str(input("Username : "))
    if len(username) > 20:
        print("username must be within 20 chars")
        register()
    password = str(input("Password : "))
    if len(password) < 8:
        print("Password too short")
        register()
    elif len(password) > 20:
        print("password must be within 20 chars")
        register()
    else:
        values = (username, password)
        cmd.execute(query, values)
        server.commit()
        if cmd.rowcount == 1:
            print("Account created!!")
        else:
            print("A error occurred while creating account")


#register()


def login():
    username = str(input("Username : "))
    cmd.execute("SELECT pass FROM users WHERE username=%s", (username,))
    saved_pass = cmd.fetchall()
    for pw in saved_pass:
        if pw:
            print("Exists")
        else:
            retry = input("Username doesn't exists\nWould you like to login again or register[L/R]")
            if retry == "L" or retry == "l":
                login()
            elif retry == "R" or retry == "r":
                register()


login()
