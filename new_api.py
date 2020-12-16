from newsapi import NewsApiClient

api_key = "0fa08811927849299931087429d6ce1b"
news_api = NewsApiClient(api_key)


def getBBCHeadline():
    return news_api.get_top_headlines(sources='bbc-news')['articles']

def getAPHeadline():
    return news_api.get_top_headlines(sources='associated-press')['articles']

def getCNNHeadline():
    return news_api.get_top_headlines(sources='cnn')['articles']

def getFoxHeadline():
    return news_api.get_top_headlines(sources='fox-news')['articles']
