# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getData, getName
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
    stock_sentiment = getData(userStockChoice)
    return render_template('sentiment.html', time = datetime.now(), sentiment = stock_sentiment, name = stock_name)