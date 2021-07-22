import requests

def getData(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    bullish = response['stockTwitsPercentBullish']
    bearish = response['stockTwitsPercentBearish']
    neutral = response['stockTwitsPercentNeutral']
    sentiment = [bullish, bearish, neutral]
    return sentiment

def getName(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    return response['name']