# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getStockTwitsData, getRedditStockData, getRedditMarketData, getName, getLogo
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/yoursentiment', methods=['GET','POST'])
def yoursentiment():
    userStockChoice = request.form['stockchoice']
    stock_name = getName(userStockChoice)
    stock_twits_sentiment = getStockTwitsData(userStockChoice)
    reddit_stock_sentiment = getRedditStockData(userStockChoice)
    reddit_market_sentiment = getRedditMarketData(userStockChoice)
    stock_logo = getLogo(userStockChoice)
    return render_template('sentiment.html', time = datetime.now(), stock_twits = stock_twits_sentiment, reddit_stock = reddit_stock_sentiment,
    reddit_market = reddit_market_sentiment, name = stock_name, logo = stock_logo)