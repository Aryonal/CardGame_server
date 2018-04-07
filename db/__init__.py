from pymongo import MongoClient

client = MongoClient('localhost', 27017)
user = client['ub_game']['user']
card = client['ub_game']['card']
ques = client['ub_game']['question']

__all__ = ['user', 'card']
