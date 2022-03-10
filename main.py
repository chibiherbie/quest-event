from db import DataBase
from player import Player
import config

db_user = DataBase()


def data_user(id, msg=''):
    if db_user.get_id(id):

        print("ID игрока - ", id)
        return db_user.get_data(id)

    # TEST PASSWORD
    if msg != config.PASSWORD:
        return None
    # ------------

    db_user.create_player(id)

    print("Игрок добавлен с ID - ", id)
    return db_user.get_data(id)


def story(user_id, msg=''):
    data_player = data_user(user_id, msg)

    print(data_player)

    if data_player:
        player = Player(data_player[2])

        #
        # ACTION
        #

        db_user.update_story(user_id, player.story_num + 1)

        return 'sdf'
    return 'отказано'


def init():
    global db_user


if __name__ == '__main__':
    print('Hi man. Stop!')