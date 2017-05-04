from flask import Flask, render_template, request
from flask_navigation import Navigation
import requests
import json
import pickle
from model.twitterAPI import getTweets
from model.NBclassifier import naiveBayesSentimentCalculator

app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
])

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/results", methods=['GET'])
def results():
    if request.method == 'GET':
        text = request.args.get('userinput')
        tweets = getTweets(text)
        results = []

        for tweet in tweets:
            result = naiveBayesSentimentCalculator(tweet)
            results.append(result)
        values = [results.count('positive'), results.count('negative')]
        return render_template('results.html', values=values, text=text, tweets=tweets)


if __name__ == '__main__':
    app.debug = True
    app.run()
