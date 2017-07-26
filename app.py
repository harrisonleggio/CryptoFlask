from flask import Flask, render_template, request, send_file
from pypoloniex import LoadPairs, TimeSeries
import pandas as pd
import matplotlib.pyplot as plt
import StringIO
import datetime
from datetime import timedelta, date



app = Flask(__name__, static_folder='/Users/Harrison/PycharmProjects/FlaskCrypto/static/images')


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
    coin_name = request.form['coin_name'].upper()
    duration = request.form['duration']
    return display_graph(coin_name)
    #return scrape_coins(coin_name, duration)

@app.route('/images/<coin_name>')
def display_graph(coin_name):
    return render_template("search_result.html", title=coin_name)


@app.route('/scrape_coins/<coin_name><duration>', methods=['GET'])
def scrape_coins(coin_name, duration):

    pair = ('USDT', coin_name)

    sess = TimeSeries()
    period = 86400
    end = datetime.date.today().strftime('%d/%-m/%Y')
    start = (datetime.date.today() - timedelta(days=int(duration))).strftime('%d/%-m/%Y')
    sess.getData(pair, period, start, end)

    df = sess.data

    print df

    graph = df.plot(x='date', y='close')
    fig = graph.get_figure()
    #filepath = 'static/images/graph.png'
    #fig.savefig(filepath)

    img = StringIO.StringIO()
    fig.savefig(img)
    img.seek(0)


    return send_file(img, mimetype='image/png')




if __name__ == '__main__':
    app.run(debug=True, port=8080)

