from pymongo import MongoClient

client = MongoClient('localhost', 27017)
ur = client['ub_game']['user']
cd = client['ub_game']['card']
ques = client['ub_game']['question']

__all__ = ['user', 'card']
