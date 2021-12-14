import os

from flask import Flask

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')

@app.route('/off')
def off():
    os.system("amixer set Capture 0%")
    return "off"

@app.route('/on')
def on():
    os.system("amixer set Capture 100%")
    return "on"

@app.route('/<volume>')
def volume(volume):
    os.system("amixer set Capture " + volume + "%")
    return "volume"
