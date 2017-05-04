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

documents = []

for tweet in pos_tweets:
    documents.append( (tweet, "positive") )
for tweet in neg_tweets:
    documents.append( (tweet, "negative") )

all_words = []

short_pos_words = word_tokenize("\n".join(clean_pos_tweetwords))
short_neg_words = word_tokenize("\n".join(clean_neg_tweetwords))

word_regex = r'^\w+$'

def is_word(sample):
    match = re.match(word_regex, sample)
    if match:
        return True
    else:
        return False

for word in short_pos_words:
    if is_word(word):
        all_words.append(word.lower())
for word in short_neg_words:
    if is_word(word):
        all_words.append(word.lower())

all_words = nltk.FreqDist(all_words)

common_words = all_words.most_common(20)
common_words_dictionary = dict(common_words)
stop_words = list(common_words_dictionary.keys())


word_features = list(all_words.keys())[:5000]
print(word_features)
print(stop_words)
refined_vocabulary = [word for word in word_features if word not in stop_words]

save_refined_vocabulary = open("refined_vocabulary.pickle", "wb")
pickle.dump(refined_vocabulary, save_refined_vocabulary)
save_refined_vocabulary.close()

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in refined_vocabulary:
        features[w] = (w in words)
    return features
