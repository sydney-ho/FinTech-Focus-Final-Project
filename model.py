import requests

def getData(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    bullish = round(response['stockTwitsPercentBullish'],2)
    bearish = round(response['stockTwitsPercentBearish'],2)
    neutral = round(response['stockTwitsPercentNeutral'],2)
    sentiment = [bullish, bearish, neutral]
    return sentiment

def getName(query):
    response = requests.get(f'https://www.styvio.com/api/sentiment/{query}').json()
    return response['name']