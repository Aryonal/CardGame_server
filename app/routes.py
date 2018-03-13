# -*-coding:utf-8-*-
from __future__ import unicode_literals
from flask import request, jsonify
from app import app
from app.gaming import *

@app.route("/", methods=["GET", "POST"])
def response():
    req_data = request.get_json()
    data = responses[req_data["statusCode"]](req_data)
    return jsonify(data)
