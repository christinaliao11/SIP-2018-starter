'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

tweettext = []
tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet["text"]



# Continue your program below! 

# print(tweetstring)
tweetBlob = TextBlob(tweetstring)

print(tweetBlob.translate(to="es"))

blob_polarity = []
for blob in tweettext:
    blob_polarity.append(blob.polarity)

blob_subjectivity = []
for blob in tweettext:
    blob_subjectivity.append(blob.blob_subjectivity)

word_dict = {}

for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]

print(word_dict) 
#blob_polarity.sort()
#print(blob_polarity)

tb = TextBlob("You are a horrible person")
