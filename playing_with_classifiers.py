import nltk
import random
from nltk.corpus import twitter_samples
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

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

# short_pos = open("polaritydata/rt-polarity.pos", "r").read()

documents = []
# twitter:
for tweet in pos_tweets:
    documents.append( (tweet, "positive") )
for tweet in neg_tweets:
    documents.append( (tweet, "negative") )

# movie reviews:
# for r in short_pos.split("\n"):
#     documents.append( (r, "positive") )


# PART OF SPEECH(pos) tagging: Js are adjectives, Vs are verbs, Rs are adverbs
# allowed_word_types = ["JJ", "JJR", "JJS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
# part_of_speech_pos_words = nltk.pos_tag(short_pos_words)
# part_of_speech_neg_words = nltk.pos_tag(short_neg_words)

all_words = []
# tokenize twitter_samples:
short_pos_words = word_tokenize("\n".join(clean_pos_tweetwords))
short_neg_words = word_tokenize("\n".join(clean_neg_tweetwords))




# tokenize movie reviews:
# short_pos_words = word_tokenize(short_pos)
# short_neg_words = word_tokenize(short_neg)

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
refined_word_features = [word for word in word_features if word not in stop_words]


save_word_features = open("ref_word_features.pickle", "wb")
pickle.dump(refined_word_features, save_word_features)
save_word_features.close()
# saved_word_features = open("new_word_features.pickle", "rb")
# word_features = pickle.load(saved_word_features)
# saved_word_features.close()

def find_features(document):
    # words = document.split()
    words = word_tokenize(document)
    # words = set(document)
    features = {}
    for w in refined_word_features:
        features[w] = (w in words)
    return features

# pdb.set_trace()

random.shuffle(documents)
print(documents[0])
featuresets = [(find_features(tweet), category) for (tweet, category) in documents]
#random.shuffle(featuresets)

# training_set = featuresets[:9500]
testing_set = featuresets[:2500]

# TRAIN classifiers:
# classifier = nltk.NaiveBayesClassifier.train(training_set)
#
# MNB_classifier = SklearnClassifier(MultinomialNB())
# MNB_classifier.train(training_set)
#
# BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
# BernoulliNB_classifier.train(training_set)
#
# LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
# LogisticRegression_classifier.train(training_set)
#
# SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
# SGDClassifier_classifier.train(training_set)
#
# SVC_classifier = SklearnClassifier(SVC())
# SVC_classifier.train(training_set)
#
# LinearSVC_classifier = SklearnClassifier(LinearSVC())
# LinearSVC_classifier.train(training_set)
#
# NuSVC_classifier = SklearnClassifier(NuSVC())
# NuSVC_classifier.train(training_set)



# USE an already trained classifier:
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_MNB = open("MNB.pickle", "rb")
MNB_classifier = pickle.load(classifier_MNB)
classifier_MNB.close()

classifier_BernoulliNB = open("BernoulliNB.pickle", "rb")
BernoulliNB_classifier = pickle.load(classifier_BernoulliNB)
classifier_BernoulliNB.close()

classifier_LogisticRegression = open("LogisticRegression.pickle", "rb")
LogisticRegression_classifier = pickle.load(classifier_LogisticRegression)
classifier_LogisticRegression.close()

classifier_SGDClassifier = open("SGDClassifier.pickle", "rb")
SGDClassifier_classifier = pickle.load(classifier_SGDClassifier)
classifier_SGDClassifier.close()

classifier_SVC = open("SVC.pickle", "rb")
SVC_classifier = pickle.load(classifier_SVC)
classifier_SVC.close()

classifier_LinearSVC = open("LinearSVC.pickle", "rb")
LinearSVC_classifier = pickle.load(classifier_LinearSVC)
classifier_LinearSVC.close()

classifier_NuSVC = open("NuSVC.pickle", "rb")
NuSVC_classifier = pickle.load(classifier_NuSVC)
classifier_NuSVC.close()


# PRINT results:
print("Original Naive Bayes accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)
print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)


# SAVE trained classifiers:
# save_NuSVC_classifier = open("NuSVC.pickle", "wb")
# pickle.dump(NuSVC_classifier, save_NuSVC_classifier)
# save_NuSVC_classifier.close()
#
# save_LinearSVC_classifier = open("LinearSVC.pickle", "wb")
# pickle.dump(LinearSVC_classifier, save_LinearSVC_classifier)
# save_LinearSVC_classifier.close()
#
# save_SVCclassifier = open("SVC.pickle", "wb")
# pickle.dump(SVC_classifier, save_SVCclassifier)
# save_SVCclassifier.close()
#
# save_SGDClassifier= open("SGDClassifier.pickle", "wb")
# pickle.dump(SGDClassifier_classifier, save_SGDClassifier)
# save_SGDClassifier.close()
#
# save_LogisticRegression_classifier = open("LogisticRegression.pickle", "wb")
# pickle.dump(LogisticRegression_classifier, save_LogisticRegression_classifier)
# save_LogisticRegression_classifier.close()
#
# save_BernoulliNB_classifier = open("BernoulliNB.pickle", "wb")
# pickle.dump(BernoulliNB_classifier, save_BernoulliNB_classifier)
# save_BernoulliNB_classifier.close()
#
# save_MNBclassifier = open("MNB.pickle", "wb")
# pickle.dump(MNB_classifier, save_MNBclassifier)
# save_MNBclassifier.close()
#
# save_classifier = open("naivebayes.pickle", "wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()
