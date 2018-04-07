# -*-coding:utf-8-*-
from flask import request, jsonify
from app import app, arena, socketio
from app.response import *

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'index'

@app.route('/stage', methods=['GET'])
def player_profile():
    data = request.get_json()


# @app.route("/", methods=["GET", "POST"])
# def init():
#     req_data = request.get_json()
#     # data = responses[req_data["statusCode"]](req_data)
#     # return jsonify(data)
#
#     #TODO: get user's cards
#     user_id = req_data["userId"]
#     # get cards of user_id
#     room_id = arena.new_guest(user_id)
#     return jsonify({
#         "code": 0,
#         "room": room_id,
#         "cards": [{
#             "id": 1,
#             "atk": 10,
#             "cost": 2
#         }]*30
#     })
#
# @app.route("/room/<int:id>", methods=["GET", "POST"])
# def room(id):
#     req_data = request.get_json()
#     data = arena.send_msg(id, req_data)
#     return jsonify(data)
