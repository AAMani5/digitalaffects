import nltk
import random
from nltk.corpus import twitter_samples
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression

from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import re
import pdb


pos_tweets = twitter_samples.strings('positive_tweets.json')
neg_tweets = twitter_samples.strings('negative_tweets.json')

split_pos_tweets = [words for tweets in pos_tweets for words in tweets.split()]
filtered_pos_tweetwords = [ word for word in split_pos_tweets if not word.startswith('@') ]
clean_pos_tweetwords = [ word for word in filtered_pos_tweetwords if not word.startswith('http') ]

split_neg_tweets = [words for tweets in neg_tweets for words in tweets.split()]
filtered_neg_tweets = [ word for word in split_neg_tweets if not word.startswith('@') ]
clean_neg_tweetwords = [ word for word in filtered_neg_tweets if not word.startswith('http') ]
