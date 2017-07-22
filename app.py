from flask import Flask, render_template
from coinmarketcap import Market



app = Flask(__name__)


@app.route('/')
def index():
    scrape_coins()
    return render_template('index.html')



def scrape_coins():
    coinmarketcap = Market()
    data = coinmarketcap.ticker(convert="USD")
    print data


if __name__ == '__main__':
    app.run(debug=True)

