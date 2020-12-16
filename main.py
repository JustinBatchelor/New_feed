# This is a sample Python script.

import new_api as news


def getAllArticles():
    sources = []
    ap = news.getAPHeadline()
    cnn = news.getCNNHeadline()
    bbc = news.getBBCHeadline()
    fox = news.getFoxHeadline()
    sources.append(ap)
    sources.append(cnn)
    sources.append(bbc)
    sources.append(fox)
    return sources


def printArticle(source, title, des, author, url):
    print("Source: ", source)
    print("Article Title: ", title)
    print("Description: ", des)
    print("Author: ", author)
    print("Link: ", url)
    print("==" * 100)
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    articles = getAllArticles()
    for source in articles:
        for article in source:
            printArticle(article['source']['name'], article['title'], article['description'],
                         article['author'], article['url'])
