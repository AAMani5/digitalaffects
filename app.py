from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import requests
import json
import pickle
from twitterAPI import getTweets

with open('twitter_classifier.pickle', 'rb') as f:
    trainedNBClassifier = pickle.load(f)

with open('vocabulary.pickle', 'rb') as vocabulary_file:
    vocabulary = pickle.load(vocabulary_file)

app = Flask(__name__)

def extract_features(tweet):
  tweet_words=set(tweet)
  features={}
  for word in vocabulary:
      features[word]=(word in tweet_words)
  return features

@app.route("/")
def index():
    return render_template('index.html')
