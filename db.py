import sqlite3
import config
import os


class DataBase:
    def __init__(self):
        if not os.path.isfile(config.DATABASEPATH):
            open("BabyFile.sqlite", "w+")

            self.con = sqlite3.connect(config.DATABASEPATH)
            self.cur = self.con.cursor()
            self.cur.execute('''CREATE TABLE user (id INTEGER PRIMARY KEY, user_id TEXT NOT NULL, story_num TEXT);''')

            print('DataBase create')
            return

        self.con = sqlite3.connect(config.DATABASEPATH)
        self.cur = self.con.cursor()

        print('DataBase connect')
