from flask import Flask, render_template, abort,jsonify
from model import db
app = Flask(__name__)
counter = 0

@app.route('/')
def welcome():
    cards = db
    return render_template('welcome.html', cards=cards)

@app.route('/card/<int:index>')
def cards(index):
    try:
        card = db[index]
        return render_template('cards.html', card=card, index=index, sizeOfCards=len(db)-1)
    except IndexError:
        abort(404)

@app.route('/api/cards/list/')
def cards_list():
    cards = db
    return jsonify(cards)

@app.route('/api/card/<int:index>')
def single_card(index):
    try:
        card = db[index]
        return jsonify(card)
    except IndexError:
        abort(404)
        