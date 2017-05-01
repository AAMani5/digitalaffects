from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import requests
import json
import pickle
from model.twitterAPI import getTweets
from model.NBclassifier import naiveBayesSentimentCalculator

def create_app():
    app = Flask(__name__)

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

            session['tweets'] = list(zip(tweets, results))
            session['results'] = results
            session['text'] = text
            return redirect(url_for('json'))

    @app.route('/ping')
    def ping():
        return jsonify(ping='pong')

    return app
    return app

# secret_key for sessions exposed as no sensitive data stored on sessions
if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run()
