import requests

def getStockTwitsData(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    bullish = round(response['stockTwitsPercentBullish'],2)
    bearish = round(response['stockTwitsPercentBearish'],2)
    neutral = round(response['stockTwitsPercentNeutral'],2)
    sentiment = [bullish, bearish, neutral]
    return sentiment

def getRedditStockData(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    bullish = round(response['redditStocksPercentBullish'],2)
    bearish = round(response['redditStocksPercentBearish'],2)
    neutral = round(response['redditStocksPercentNeutral'],2)
    sentiment = [bullish, bearish, neutral]
    return sentiment

def getRedditMarketData(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    bullish = round(response['redditStockMarketPercentBullish'],2)
    bearish = round(response['redditStockMarketPercentBearish'],2)
    neutral = round(response['redditStockMarketPercentNeutral'],2)
    sentiment = [bullish, bearish, neutral]
    return sentiment

def getTotalData(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    bullish = round(response['redditStockMarketPercentBullish'],2)
    bearish = round(response['redditStockMarketPercentBearish'],2)
    total = response['totalSentiment']
    sentiment = [bullish, bearish, total]
    return sentiment

def getName(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    return response['name']

def getLogo(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    return response['logoURL']

def getPrices