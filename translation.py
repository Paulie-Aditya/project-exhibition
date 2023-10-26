import urllib
import requests
import json
def translate(text):
    text = text.replace(" ","%20")
    apiUrl = f'https://api.mymemory.translated.net/get?q={text}&langpair=en-GB|hi-IN'

    webUrl = urllib.request.urlopen(apiUrl)
    stuff = webUrl.read()
    stuff= str(stuff,'UTF-8')
    stuff.replace("'",'"')
    stuff = json.loads(stuff)
    output = stuff['responseData']['translatedText']
    #print(output)
    return output