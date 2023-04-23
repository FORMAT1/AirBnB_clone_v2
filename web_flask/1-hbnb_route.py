#!/usr/bin/python3
"""
    A script that start Flask  web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
"""returns Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
"""returns HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
