from flask import Flask, render_template, request
from pypoloniex import LoadPairs, TimeSeries
import pandas as pd
import matplotlib.pyplot as plt



app = Flask(__name__)


@app.route('/')
def index():
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
    return scrape_coins(coin_name)



def scrape_coins(coin_name):

    print coin_name

    pair = ('USDT', coin_name)

    sess = TimeSeries()
    period = 86400
    start = '1/3/2017'
    end = '23/7/2017'
    sess.getData(pair, period, start, end)

    #sess1.show()
    df = sess.data
    print df

    df['date'] = df['date'].map(lambda x: x.replace('20:00:00', ''))

    graph = df.plot(x='date', y='close')
    fig = graph.get_figure()
    fig.savefig('static/images/graph.png')

    return render_template('search_result.html', filename='/static/images/graph.png')




if __name__ == '__main__':
    app.run(debug=True, port=8080)

