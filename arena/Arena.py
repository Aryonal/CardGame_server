# -*-coding:utf-8-*-
import multiprocessing as mp
import room
from models import *
import random as rd
import time, threading

class Arena(object):

    '''
    vol: volume of this arena
    '''
    def __init__(self, vol):
        self._rooms_map = {} # {id:(process, pipe)}
        self._rest_ids = list(map(lambda n: 'r'+str(n), range(100)))
        self._waiting_rooms = [] #[(room_id:user_id)]
        self._threads = []


    '''
    generate a new room id
    '''
    def _new_room_id(self):
        if len(self._rest_ids) == 0:
            raise NoRestRoomError()
        room_id = self._rest_ids.pop(0)
        return room_id

    '''
    user join room
    '''
    def _join_room(self, room_id, user_id):
        # send msg to room to add new guest
        msg = Msg(room_id, 'arena', {
            "cmd": "add guest",
            "data": {
                "userId": user_id
            }
        })
        print("[Arena/Arena._join_room]: 房间 "+ str(room_id) + "接客啦！" + str(user_id) + "里边请～")
        self._rooms_map[room_id][1].send(msg)

    '''
    room_id: int: room id
    '''
    def _new_room(self, room_id, user_id):
        print("[Arena/Arena._newroom]: 为客人新开一间房间 " + str(room_id))
        p,c = mp.Pipe()
        rm = mp.Process(target=room.room_work, args=[room_id, user_id, c])
        rm.start()
        self._rooms_map[room_id] = (rm, p)

    '''
    user_id: int: user id
    match proper rival for user id, return room id
    '''
    def _match_rival(self, user_id):
        #TODO: better match
        room_id, rival_id = self._waiting_rooms.pop(0)
        print("[Arena/Arena._match_rival]: 客人请进入房间 " + str(room_id) + "，对手是 " + str(rival_id))
        return room_id

    '''
    new guest, called when a new user request for a new room
    user_id: int: user id
    return room id
    '''
    def new_guest(self, user_id):
        print("[Arena/Arena.new_guest]: 有客人来啦！" + str(user_id))
        if len(self._waiting_rooms) == 0:
            room_id = self._new_room_id()
            self._new_room(room_id, user_id)
            self._waiting_rooms.append((room_id, user_id))
            return room_id

        room_id = self._match_rival(user_id)
        self._join_room(room_id, user_id)
        return room_id

    '''
    called when game is ended
    '''
    def close_room(self, room_id):
        print("[Arena/Arena.close_room]: 关闭房间 " + str(room_id))
        msg = Msg(room_id, 'arena', {
            "cmd": "close_room"
        })
        room,p = self._rooms_map[room_id]
        p.send(msg)
        p.close()
        room.join()
        del self._rooms_map[room_id]
        self._rest_ids.append(room_id)

    def close(self):
        print("[Arena/Arena.close]: 打烊啦！各回各家")

        for id,pk in self._rooms_map.items():
            msg = Msg(id, 'arena', {
                    "cmd": "close_room"
                })
            pk[1].send(msg)
            pk[1].close()
            pk[0].join()
        for t in self._threads:
            t.join()

    '''
    room_id: int: room id
    data: dict: request.json()
    '''
    def send_msg(self, room_id, data, cb=lambda data: 0):
        print("[Arena/Arena.send_msg]: 下面播送一条通知：" + str(room_id) + "房间请注意, " + data.src + "对你说：" + str(data))
        p = self._rooms_map[room_id][1] # pipe with room id
        p.send(Msg(room_id, 'client', data))
        try:
            t = threading.Thread(target=_postprocessing_msg, args=(p, room_id, cb))
            self._threads.append(t)
            t.start()
        except:
            raise

'''
postprocessing msg function
'''
def _postprocessing_msg(p, room_id, cb):
    while True:
        if p.poll():
            msg = p.recv()
            if not msg.id == room_id:
                raise MisMatchRoomIdError()
            if msg.src == 'client':
                data = msg.data
                cb(data)
            else:
                pass
        else:
            time.sleep(rd.random()/1.0)
            continue
