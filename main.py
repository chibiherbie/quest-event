import db
import config

db_user = db.DataBase()


def check_user(id, msg=''):
    if db_user.get_id(id):
        print("ID игрока - ", id)
        return True

    # TEST PASSWORD
    if msg != config.PASSWORD:
        return False
    # ------------

    db_user.insert_id(id)
    print("Игрок добавлен с ID - ", id)
    return True


def story(user_id, msg=''):
    if check_user(user_id, msg):
        return 'sdf'
    return 'отказано'


def init():
    global db_user


if __name__ == '__main__':
    print('Hi man. Stop!')