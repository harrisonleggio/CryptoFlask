from flask import Flask, render_template, request
from pypoloniex import LoadPairs, TimeSeries
import pandas as pd
import matplotlib.pyplot as plt


app = Flask(__name__)


@app.route('/')
def index():
    scrape_coins()
    return render_template('index.html')


@app.route('/popular')
def popular_page():
    return 'In progress'


@app.route('/about')
def about_page():
    return "In progress"

"""
Testing dynamic routes. Maybe for ease of access?
i.e user appends to URL?
"""
@app.route('/coins/<coin>')
def get_coin(coin):
    return coin


"""
Getting data from search bar
"""
@app.route('/search', methods=['POST'])
def get_search():
    coin_name = request.form['coin_name']
    return render_template('search_result.html',coin_name=coin_name)


def scrape_coins():
    sess = LoadPairs()
    pair = ('BTC', 'LTC')
    ltc = sess.getPair(market='USDT', coin='LTC')
    print ltc


if __name__ == '__main__':
    app.run(debug=True, port=8080)

