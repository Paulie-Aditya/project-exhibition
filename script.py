# get input from user, taking sample input for now
input = 'Fight Club'


from imdb import Cinemagoer

ia = Cinemagoer()

search = ia.search_movie(title=input)

if(len(search)<=0):
    print ("Not Found")
id = "tt"+search[0].movieID
#print(search[0].data)

url = f'https://www.imdb.com/title/{id}/reviews/'

import requests
from bs4 import BeautifulSoup

page = requests.get(url=url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("div",class_="text show-more__control")
print(len(results)) # 20-30 Reviews

import sentiment

for result in results:
    sentiment.calc_score(str(result))