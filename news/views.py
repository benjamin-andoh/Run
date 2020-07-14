from django.shortcuts import render
from newsapi import NewsApiClient


def Index(request):
    # create an object of the api client
    newsapi = NewsApiClient(api_key="1a1c45f7b3a94ced97a3a921ce8148b8")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    my_list = zip(news, desc, img)
    return render(request, 'index.html', context={'mylist': my_list})


def bbc(request):
    # create an object of the api client
    newsapi = NewsApiClient(api_key="1a1c45f7b3a94ced97a3a921ce8148b8")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    my_list = zip(news, desc, img)
    return render(request, 'bbc.html', context={'mylist': my_list})
