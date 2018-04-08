# -*-coding:utf-8-*-
import time
import random as rd
from models import *
import db


'''
player class

{user}: obj: user
'''
class Player(object):
    def __init__(self, user):
        self.user = user
        self.magic = 0,
        self.score = 0,
        self.ready = False

'''
room class

{id}: int: room id
{guest0}: user id 0
{guest1}: user id 1
{n}: int: number of guests in this room
'''
class Room(object):
    def __init__(self, room_id):
        self.id = room_id
        self.guests = []
        self.n = 0
        self.question = ''
        self.answer = 0

    def is_ready(self):
        if self.guests[0].ready and self.guests[1].ready:
            self.guests[0].ready = False
            self.guests[1].ready = False
            return True
        return False

    def add_guest(self, user_id):
        if self.n == 2:
            raise RoomTooCrowdingError()
        #TODO: read user profile
        user = db.user.find_user_by_id(user_id)
        self.guests[n] = Player(user)
        self.guests[n].ready = True
        n += 1

    def guest_leave(self, user_id):
        pass

'''
{room_id}: int: room id
{user_id}: int: user id
{conn}: multiprocessing.Pipe: pipe between room and arena
'''
def room_work(room_id, user_id, conn):
    print("[Room{0}/room_work]: 房间{1}开张啦！".format(room_id, room_id))
    # preprocessing
    room = Room(room_id)
    room.add_guest(user_id)

    while True:
        if conn.poll():
            msg = conn.recv()

            # check if illegal
            if not msg.id == room_id:
                raise MisMatchRoomIdError()

            src = msg.src
            data = msg.data
            print("[Room{0}/room_work]: Receive Msg from {1}, data is {2}".format(room_id, src, data))

            #TODO: handle data
            if src == 'arena':
                if data['cmd'] == 'close_room':
                    break
                elif data['cmd'] == 'add_guest':
                    #TODO: add user to room
                    room.add_guest(data['data']['userId'])
                    if room.is_ready():
                        #TODO: start game when there're 2 guests
                        pass
                    pass
                elif data['cmd'] == 'guest_leave':
                    pass
                elif data['cmd'] == 'question':
                    #TODO: prepare question
                    qs = db.question.pop_random_question()
                    msg.data = qs
                    room.question = qs['question']
                    room.answer = qs['answer']
                    conn.send(msg)
            elif src == 'client':
                pass

                conn.send(msg)
        else:
            time.sleep(rd.random()/1.0)
            continue

if __name__ == '__main__':
    main()
