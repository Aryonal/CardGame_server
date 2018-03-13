# -*-coding:utf-8-*-
from __future__ import unicode_literals
from flask import jsonify

import random as rd
import time

def res_0(d):
    '''
    d: {
        "userId": ,
        "statusCode":
    }
    '''
    #TODO: find user and list cards
    return {
        "code":0,
        "cards": [1]*50
    }

def res_1(d):
    '''
    d: {
        "userId": ,
        "statusCode": ,
        "cards": {"pool": [8], "board": [3]}
    }
    '''
    #TODO: match rival
    #TODO: waiting for room and rival
    #TODO: check if 8 cards in user's cards

    time.sleep(rd.randint(100, 3000) * 1.0/1000)
    return {
        "code":0,
        "rivalId":54321,
        "value": {"energy": 1, "magic": 1, "score":0}
    }

def res_2(d):
    return {
        "code": 1
    }

def res_3(d):
    '''
    d: {
        "userId": ,
        "statusCode": ,
        "cards": {"pool": [8], "board": [3],
        "value": {"energy": , "magic": , "score": }
    }
    '''
    #TODO: wait for rival post answer
    #TODO: update game value

    time.sleep(rd.randint(100, 3000) * 1.0/1000)
    return {
        "code": 0,
        "question": "what's the weather today",
        "value": d["value"]
    }

def res_4(d):
    return {
        "code": 1
    }

def res_5(d):
    '''
    d: {
        "statusCode": ,
        "userId": ,
        "answer": "great!",
        "value": {"energy": , "magic": , "score": }
    }
    '''

    time.sleep(rd.randint(100, 3000) * 1.0/1000)
    return {
        "code": 0,
        "isRight": True,
        "win": True,
        "value": d["value"]
    } if rd.randint(0, 10) < 5 else {
        "code": 3
    }

def res_6(d):
    return {
        "code": 1
    }


'''
get request data, return response data
'''
responses = [res_0, res_1, res_2, res_3,
             res_4, res_5, res_6]
