# -*-coding:utf-8-*-

import game

'''
msg to put into multiprocessing.Queue
id: int: msg send to room id
src: str: whom msg's from, 'client' or 'arena' or any other
data: dict: msg data
'''
class Msg(object):
    def __init__(self, id, src, data):
        self.id = id
        self.src = src
        self.data = data

'''
raise when no rest rooms
'''
class NoRestRoomError:
    pass

'''
raise when add guest to a full room
'''
class RoomTooCrowdingError:
    pass

'''
raise when send other room's msg to this room
'''
class MisMatchRoomIdError:
    pass


'''
Card class

id: card id
atk: atk
cost: cost
dscrpt: description
img: path/to/img
'''
class Card(object):
    def __init__(self, id, atk, cost, dscrpt, img):
        self.id = id
        self.atk = atk
        self.cost = cost
        self.dscrpt = dscrpt
        self.img = img


'''
user class

id: int: user id
cards: list[Cards]
win_rate: float: win rate
chrct: characteristics #TODO: how
'''
class User(object):
    def __init__(self, id, win_games, all_games):
        self.id = id
        self.cards = game.INIT_CARDS
        self.value = game.INIT_VALUE
        self.win_games = win_games
        self.all_games = all_games
        self.ready = False


'''
room class

id: int: room id
guest0: user id 0
guest1: user id 1
n: int: number of guests in this room
'''
class Room(object):

    def __init__(self, room_id):
        self.id = room_id
        self.guests = {}
        self.n = 0

    def add_guest(self, user_id):
        #TODO: read user profile
        win_games = 0
        all_games = 0
        if self.n == 2:
            raise RoomTooCrowdingError()
        self.guests[user_id] = User(user_id, win_games, all_games)
