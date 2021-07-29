# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request, redirect
from datetime import datetime
from model import getStockTwitsData, getRedditStockData, getRedditMarketData, getTotalData, getName, getLogo, getPrices
from flask_pymongo import PyMongo

import os


# -- Initialization section --
app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.getenv('DBNAME')
DBNAME = app.config['MONGO_DBNAME']    
app.config['USER'] = os.getenv('DBUSER')
USER = app.config['USER']    
app.config['MONGO_PWD'] = os.getenv('DBPWD')   
PWD = app.config['MONGO_PWD']    
# URI of database   
# app.config['MONGO_URI'] = f"mongodb+srv://{USER}:{PWD}@cluster0.vmzkd.mongodb.net/{DBNAME}?retryWrites=true&w=majority"
app.config['MONGO_URI'] = f"mongodb+srv://{USER}:{PWD}@cluster0.4hkah.mongodb.net/{DBNAME}?retryWrites=true&w=majority"

is_prod = os.environ.get('IS_HEROKU', None)
			if is_prod:
    				key = os.environ.get("GIPHY_KEY")

mongo = PyMongo(app)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/about')
def get_about():
    return render_template('about.html',title="About")

@app.route('/contact')
def get_contact():
    return render_template('contact.html', title="Contact Us")

@app.route('/yoursentiment', methods=['GET','POST'])
def yoursentiment():
    userStockChoice = request.form['stockchoice']
    stock_name = getName(userStockChoice)
    stock_twits_sentiment = getStockTwitsData(userStockChoice)
    reddit_stock_sentiment = getRedditStockData(userStockChoice)
    reddit_market_sentiment = getRedditMarketData(userStockChoice)
    total_sentiment = getTotalData(userStockChoice)
    stock_logo = getLogo(userStockChoice)
    stock_price = getPrices(userStockChoice)
    return render_template('sentiment.html', time = datetime.now(), stock_twits = stock_twits_sentiment, reddit_stock = reddit_stock_sentiment,
    reddit_market = reddit_market_sentiment, total = total_sentiment, name = stock_name, logo = stock_logo, price = stock_price)

@app.route('/add', methods=['GET', 'POST'])
def add():
    # connect to the database
    userEmail = request.form['emailChoice']
    userQuestion = request.form['questionChoice']
    collection = mongo.db.contactInfo
    collection.insert_one({'email':userEmail, 'question':userQuestion})
    return render_template('contact.html', title="Contact Us")