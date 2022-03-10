import sqlite3
import config
import os


class DataBase:
    def __init__(self):
        if not os.path.isfile(config.DATABASEPATH):
            open("BabyFile.sqlite", "w+")

            self.con = sqlite3.connect(config.DATABASEPATH)
            self.cur = self.con.cursor()
            self.cur.execute('''CREATE TABLE user (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL,
             story_num INTEGER);''')

            print('DataBase create')
            return

        self.con = sqlite3.connect(config.DATABASEPATH)
        self.cur = self.con.cursor()

        print('DataBase connect')

    def get_id(self, id):
        return self.cur.execute('''SELECT user_id FROM user WHERE user_id=? ''', (id, )).fetchone()

    def get_data(self, id):
        return self.cur.execute('''SELECT * FROM user WHERE user_id=? ''', (id,)).fetchone()

    def create_player(self, id):
        self.cur.execute('''INSERT INTO user(user_id, story_num) VALUES(?, ?);''', (id, 0))
        self.con.commit()

    def update_story(self, id, num):
        self.cur.execute('''UPDATE user SET story_num = ? WHERE user_id=?;''', (num, id))
        self.con.commit()
