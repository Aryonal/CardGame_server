# -*-coding:utf-8-*-
from flask import Flask
from arena import Arena

app = Flask(__name__)

arena = Arena.Arena(10)

__all__ = ['routes', 'process']
from app import routes
