# -*-coding:utf-8-*-
import time
import random as rd
from models import *
import db


'''
player class

id: int: user id
cards: list[Cards]
win_rate: float: win rate
chrct: characteristics #TODO: how
'''
class Player(object):
    def __init__(self, user):
        self.user = user
        self.magic = 0,
        self.score = 0,
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
        self.question = ''

    def add_guest(self, user_id):
        if self.n == 2:
            raise RoomTooCrowdingError()
        #TODO: read user profile
        user = db.user.find_user_by_id(user_id)
        self.guests[user_id] = User(user)

'''
room_id: int: room id
user_id: int: user id
conn: multiprocessing.Pipe: pipe between room and arena
'''
def room_work(room_id, user_id, conn):
    print("[Room{0}/room_work]: 房间{1}开张啦！".format(room_id, room_id))
    # preprocessing
    room = Room(room_id)
    room.add_guest(user_id)

    while True:
        if conn.poll():
            msg = conn.recv()
            if not msg.id == room_id:
                raise MisMatchRoomIdError()
            src = msg.src
            data = msg.data
            print("[Room{0}/room_work]: Receive Msg from {1}, data is {2}".format(room_id, src, data))
            #TODO: handle data
            if src == 'arena' and data['cmd'] == 'close_room':
                break
            conn.send(msg)
        else:
            time.sleep(rd.random()/1.0)
            continue

if __name__ == '__main__':
    main()
