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
    def __str__(self):
        return "msg:\nto room: {0}\nfrom:{1}\ndata:{2}".format(self.id, self.src, self.data)

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
