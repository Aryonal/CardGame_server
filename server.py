# -*-coding:utf-8-*-
from __future__ import unicode_literals

from app import app, socketio

if __name__ == '__main__':
    #app.run(host="localhost", port=8083)
    socketio.run(app, host='localhost', port=3000, debug=True)
