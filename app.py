from flask import Flask, render_template, request
from pypoloniex import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



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
    sess = TimeSeries()
    pair = ('BTC', 'LTC')
    period = 86400
    start = '1/7/2017'
    end = '3/7/2017'

    sess.getData(pair, period, start, end)
    #sess.show()
    df = sess.data
    df.set_index('date', inplace=True)
    print df.tail()



if __name__ == '__main__':
    app.run(debug=True, port=8080)

