# -*-coding:utf-8-*-
import time
import random as rd
from models import *


'''
room_id: int: room id
user_id: int: user id
conn: multiprocessing.Pipe: pipe between room and arena
'''
def room_work(room_id, user_id, conn):
    print "room/room_work: 房间" + str(room_id) + "开张啦！"
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
            #TODO: handle data
            conn.send(msg)
        else:
            time.sleep(rd.random()/1.0)
            continue

def onRivalReady(rival, conn, data, cb=lambda conn, data: 0):
    while not rival.ready:
        time.sleep(rd.random()/1.0)
    cb(conn, data)
