import re
import requests
from bs4 import BeautifulSoup
import sentiment
from imdb import Cinemagoer
import json


# get input from user, taking sample input for now
input = 'Fight club'

def fetch_movie(input):
    ia = Cinemagoer()

    search = ia.search_movie(title=input)


    if(len(search)==0):
        print("Not Found")

    id = "tt"+search[0].movieID
    #print(search[0].data)

    url = f'https://www.imdb.com/title/{id}/reviews/'
    return url


def html_removal(text):
   text = re.compile(r'<[^>]+>').sub('', text)
   return text

def reviews_func(url):
    
    page = requests.get(url=url)

    soup = BeautifulSoup(page.content, "html.parser")

    reviews = soup.find_all("div",class_="text show-more__control")
    reviews = list(reviews)
    for i in range(len(reviews)):
        reviews[i] = html_removal(str(reviews[i]))
    return reviews

def sentiment_analysis(movie):
    url = fetch_movie(movie)
    reviews = reviews_func(url)
    analysis = dict()
    for review in reviews:
        analysis[review] = sentiment.calc_score(str(review))
    return analysis

#data = sentiment_analysis('Fight Club')

#print(data)