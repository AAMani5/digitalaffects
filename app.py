from flask import Flask, render_template, request, jsonify, session, redirect, url_for
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
            result = naiveBayesSentimentCalculator(tweet)
            results.append(result)

        session['tweets'] = tweets
        session['results'] = results
        session['text'] = text
        return redirect(url_for('json'))

# secret_key for sessions exposed as no sensitive data stored on sessions
if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()
