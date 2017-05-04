from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import requests
import json
import pickle
from twitterAPI import getTweets
from nltk.tokenize import word_tokenize
with open('naivebayes.pickle', 'rb') as f:
    trainedNBClassifier = pickle.load(f)

with open('ref_word_features.pickle', 'rb') as vocabulary_file:
    vocabulary = pickle.load(vocabulary_file)

app = Flask(__name__)

def extract_features(tweet):
  tweet_words= word_tokenize("\n".join(tweet))
  print(tweet_words)
  features={}
  for word in vocabulary:
      features[word]=(word in tweet_words)
  return features

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/json")
def json():
    results = session['results']
    text = session['text']
    tweets = session['tweets']
    values = [results.count('positive'), results.count('negative')]
    return render_template('results.html', values=values, text=text, tweets=tweets)

@app.route("/results", methods=['POST'])
def results():
    if request.method == 'POST':
        text = request.form['userinput']
        tweets = getTweets(text)
        results = []
        for tweet in tweets:
            problemInstance = tweet.split()
            problemFeatures = extract_features(problemInstance)
            result = trainedNBClassifier.classify(problemFeatures)
            results.append(result)

        session['tweets'] = list(zip(tweets, results))
        session['results'] = results
        session['text'] = text
        return redirect(url_for('json'))

# secret_key for sessions exposed as no sensitive data stored on sessions
if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()
