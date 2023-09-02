import nltk
#nltk.download('punkt')
#nltk.download('vader_lexicon')


import re
 
def html_removal(text):
   text = re.compile(r'<[^>]+>').sub('', text)
   return text

from nltk.sentiment.vader import SentimentIntensityAnalyzer 

sia = SentimentIntensityAnalyzer()

def calc_score(text:str):
    text = html_removal(text)
    score = sia.polarity_scores(text)

    if(score['compound']>=0.05):
        print("Positive")
    elif(score['compound']<0.05 and score['compound']>-0.05):
        print("Neutral")
    else:
        print("Negative")