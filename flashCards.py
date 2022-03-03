from glob import glob
from itertools import count
from flask import Flask
from datetime import datetime
app = Flask(__name__)
counter = 0
@app.route('/')
def welcome():
    return 'welcome to flash cards application'

@app.route('/date')
def date():
    return 'this is datetime {}'.format(datetime.now())

@app.route('/count-views')
def count_views():
    global counter
    counter = counter + 1
    return "number of viewers are {}".format(counter)