Implemented the VADER (Valence Aware Dictionary for sEntiment Reasoning) model to do Sentiment Analysis on Movie Reviews which will be scraped from IMDB

**__Explanation of the Code__**

We first run our sentiment analyser on a labelled dataset of IMDB reviews to check our accuracy before applying the same to live reviews.

We first preprocess the data. In usual cases we convert the reviews to lowercase and also remove punctuation but the VADER model takes the both of them as major heuristics, hence those haven't been processed and we have only removed the html tags. <br>
More info about how VADER Model works can be seen here: https://medium.com/@piocalderon/vader-sentiment-analysis-explained-f1c4f9101cd9 <br><br>

Then we do basic NLTK stuff which is currently not of any use to us but we may require the same in the case of implementation of other algorithms or models. We tokenize the sentence we are going to examine.


We now initiate our Sentiment Analyzer. <br>
Information about the VADER Model can be seen here: https://github.com/cjhutto/vaderSentiment/blob/master/README.rst and https://www.nltk.org/_modules/nltk/sentiment/vader.html which provide useful insights to what a powerful model we are using. <br>




The compound score is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive). This is equivalent to a 'normalized, weighted composite score'. <br>
Lastly we apply the following criteria to determine the actual sentiment. <br>

positive sentiment: compound score >= 0.05 <br>
neutral sentiment: (compound score > -0.05) and (compound score < 0.05) <br>
negative sentiment: compound score <= -0.05 <br><br>


Finally, this prediction is sent to the backend to be further processed and refined to be served to the end user.
