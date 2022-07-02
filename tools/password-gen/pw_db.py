import urllib.parse as up
import psycopg2
from config import Config
from main import gen_pw, Email, Site
from datetime import datetime


def pwDB():  # email, password, site
    # email = Email()
    # password = gen_pw()
    # site = Site()
    # time = str(datetime.now())[0:19]
    up.uses_netloc.append("postgres")
    url = up.urlparse(Config.DB_URL)
    pw_db = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port
                            )
    cmd = pw_db.cursor()
    print(cmd.is_connected())
    # query = "INSERT IGNORE INTO pw (email, pass, site, time) VALUES (%s, %s, %s, %s)"
    # creds = (email, password, site, time)
    # print(cmd.execute("SELECT * FROM pw"))
    cmd.close()

pwDB()