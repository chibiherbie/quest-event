import db

db_user = ''


def check_user(id):
    if id:
        print("ID игрока - ", id)
        return True
    return False


def story(user_id):
    if check_user(user_id):
        pass


def init():
    global db_user

    db_user = db.DataBase()


if __name__ == '__main__':
    print('Hi man')