import re
import requests
from bs4 import BeautifulSoup
import sentiment
from imdb import Cinemagoer
import json
import urllib
import translation


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
    #release_year = data['year']
    poster_url = data['cover url']
    url = f'https://www.imdb.com/title/{id}/reviews/'
    return url, title, poster_url


def movie_details(title):
    title = title.replace(" ","_")
    url = f'https://www.omdbapi.com/?t=${title}&apikey=16ba5256'
    webUrl = urllib.request.urlopen(url)
    data= webUrl.read()

    data = str(data,'UTF-8')
    data.replace("'",'"')
    data  = json.loads(data)

    release_year = data['Released']
    plot = data['Plot'] 
    genre = data['Genre'] 
    director = data['Director'] 
    cast = data['Actors'] 
    imdbRating = data['imdbRating']

    return release_year, plot, genre, director, cast, imdbRating
    

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

def sentiment_analysis(movie, language = "English"):
    analysis = dict()
    url, title, poster_url = fetch_movie(movie)
    analysis['title'] = title
    #analysis['release_year'] = release_year
    analysis['poster_url'] = poster_url
    release_year, plot, genre, director, cast, imdbRating = movie_details(title)

    analysis['release_year'] = release_year
    analysis['plot'] = plot
    analysis['genre'] = genre
    analysis['director'] = director
    analysis['cast'] = cast
    analysis['imdbRating'] = imdbRating

    reviews = reviews_func(url)
    analysis["reviews"] = dict()
    total = len(reviews)
    positive = 0
    negative = 0
    for review in reviews:
        score = sentiment.calc_score(str(review))
        analysis['reviews'][review] = score

        if score == 'Positive':
            positive+=1
        elif score == 'Negative':
            negative+=1
    
    if(positive>negative):
        overall_sentiment = 'Positive'
        percentage = f"{round((positive/total),2)*100}%"
    elif(positive<negative):
        overall_sentiment = 'Negative'
        percentage = f"{round((negative/total),2)*100}%"
    else:
        overall_sentiment = 'Neutral'
        percentage = "50%"
    
    analysis['sentiment'] = overall_sentiment
    analysis['percentage'] = percentage

    #analysis['sentiment'] = final

    colors = {"Positive": "rgb(11, 241, 11)", "Negative": "rgb(247, 0, 0)"}
    analysis['color'] = colors[overall_sentiment]

    # Check for the language
    # Stuff we're actually using: title, plot, genre, cast, director, sentiment
    if(language == "English"):
        return analysis
    elif(language == "Hindi"):
        for stuff in ['title','plot','genre','cast','director','sentiment']:
            if(stuff != 'sentiment'):
                analysis[stuff] = translation.translate(analysis[stuff])
            else:
                if(analysis['sentiment'] == "Positive"):
                    analysis['sentiment'] = 'उत्तम'
                elif(analysis['sentiment'] == "Negative"):
                    analysis['sentiment'] = 'खराब'

    return analysis

#data = sentiment_analysis('Fight Club')

#print(data)