from flask import Flask, render_template, abort,jsonify, request, redirect, url_for
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

@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
    if request.method == 'POST':
        print('hello')
        card = {'question':request.form['question'],
                'answer':request.form['answer']
                }
        db.append(card)
        return redirect(url_for('welcome'))
    return render_template('add_card.html')

@app.route('/remove_card/<int:index>', methods=['GET', 'POST'])
def remove_card(index):
    if request.method == 'POST':
        db.pop(index)
        return redirect(url_for('welcome'))
    return render_template('remove_card.html', card=db[index], index=index)

# APIs
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

