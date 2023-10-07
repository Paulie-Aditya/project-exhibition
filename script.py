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
    data = search[0].data
    #{'title': 'Fight Club', 'year': 1999, 'kind': 'movie', 'cover url': 'https://m.media-amazon.com/images/M/MV5BODQ0OWJiMzktYjNlYi00MzcwLThlZWMtMzRkYTY4ZDgxNzgxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UX50_CR0,1,50,74_.jpg'}
    title = data['title']
    release_year = data['year']
    poster_url = data['cover url']
    url = f'https://www.imdb.com/title/{id}/reviews/'
    return url, title, release_year, poster_url


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
    analysis = dict()
    url, title, release_year, poster_url = fetch_movie(movie)
    analysis['title'] = title
    analysis['release_year'] = release_year
    analysis['poster_url'] = poster_url
    reviews = reviews_func(url)
    analysis["reviews"] = dict()
    for review in reviews:
        analysis['reviews'][review] = sentiment.calc_score(str(review))
    return analysis

#data = sentiment_analysis('Fight Club')

#print(data)