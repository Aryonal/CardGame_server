# -*-coding:utf-8-*-
from flask import Flask
from flask_socketio import SocketIO
from arena import Arena

app = Flask(__name__)
socketio = SocketIO(app)

arena = Arena.Arena(10)

__all__ = ['routes', 'process']
from app import routes
