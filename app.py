from flask import Flask, render_template
from pypoloniex import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.finance import _candlestick


app = Flask(__name__)


@app.route('/')
def index():
    scrape_coins()
    return render_template('index.html')



def scrape_coins():

    sess = TimeSeries()
    pair = ('BTC', 'LTC')
    period = 86400
    start = '1/7/2017'
    end = '3/7/2017'

    sess.getData(pair, period, start, end)
    sess.show()
    df = sess.data
    df.set_index('date', inplace=True)
    print df.tail()




if __name__ == '__main__':
    app.run(debug=True)

