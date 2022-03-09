import sqlite3
import config
import os


class DataBase:
    def __init__(self):
        if not os.path.isfile(config.DATABASEPATH):
            open("BabyFile.sqlite", "w+")

            self.con = sqlite3.connect(config.DATABASEPATH)
            self.cur = self.con.cursor()
            self.cur.execute('''CREATE TABLE user (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, story_num TEXT);''')

            print('DataBase create')
            return

        self.con = sqlite3.connect(config.DATABASEPATH)
        self.cur = self.con.cursor()

        print('DataBase connect')

    def get_id(self, id):
        return self.cur.execute('''SELECT user_id FROM user WHERE user_id=? ''', (id, )).fetchone()

    def insert_id(self, id):
        self.cur.execute('''INSERT INTO user(user_id) VALUES(?);''', (id, ))
        self.con.commit()