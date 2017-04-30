import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
from statistics import mode
# nltk.download('punkt')
from nltk.tokenize import word_tokenize

short_pos = open("polaritydata/rt-polarity.pos", "r").read()
short_neg = open("polaritydata/rt-polarity.neg", "r").read()

documents = []

for r in short_pos.split('\n'):
    documents.append( (r, "pos") )

for r in short_neg.split('\n'):
    documents.append( (r, "neg") )

all_words = []

short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
    all_words.append(w.lower())
for w in short_neg_words:
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

common_words = all_words.most_common(20)
common_words_dictionary = dict(common_words)
stop_words = list(common_words_dictionary.keys())

word_features = list(all_words.keys())[:3000]
refined_word_features = [x for x in word_features if x not in stop_words]


def find_features(document):
    words = word_tokenize(document)
    # words = set(document)
    features = {}
    for w in refined_word_features:
        features[w] = (w in words)

    return features
