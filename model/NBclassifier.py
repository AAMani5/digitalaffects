import nltk
import json
from nltk.corpus import twitter_samples
from nltk.corpus import punkt
import pickle
from nltk.tokenize import word_tokenize

positiveTweets = twitter_samples.strings('positive_tweets.json')
negativeTweets = twitter_samples.strings('negative_tweets.json')

testTrainingSplitIndex = 2500

testNegativetweets = negativeTweets[testTrainingSplitIndex+1:]
testPositivetweets = positiveTweets[testTrainingSplitIndex+1:]

trainingPositiveTweets = positiveTweets[:testTrainingSplitIndex]
trainingNegativeTweets = negativeTweets[:testTrainingSplitIndex]

def getVocabulary(trainingPositiveTweets, trainingNegativeTweets):
    positiveWordList = [word for line in trainingPositiveTweets for word in line.split()]
    negativeWordList = [word for line in trainingNegativeTweets for word in line.split()]
    allWordList = [item for sublist in [positiveWordList,negativeWordList] for item in sublist]
    allWordSet = list(set(allWordList))
    vocabulary = allWordSet
    return vocabulary

def extract_features(tweet):
    tweet_words= word_tokenize("\n".join(tweet))
    features={}
    for word in vocabulary:
        features[word]=(word in tweet_words)

    return features

def getTrainingData(trainingPositiveTweets, trainingNegativeTweets):
  negTaggedTrainingTweetList = [{'Tweet':oneTweet.split(),'label':'negative'} for oneTweet in trainingNegativeTweets]
  posTaggedTrainingTweetList = [{'Tweet':oneTweet.split(),'label':'positive'} for oneTweet in trainingPositiveTweets]
  fullTaggedTrainingData = [item for sublist in [negTaggedTrainingTweetList,posTaggedTrainingTweetList] for item in sublist]
  trainingData = [(Tweet['Tweet'],Tweet['label']) for Tweet in fullTaggedTrainingData]
  return trainingData

# vocabulary = getVocabulary(trainingPositiveTweets, trainingNegativeTweets)
with open('./pickledfiles/refined_vocabulary.pickle', 'rb') as f:
    vocabulary = pickle.load(f)

trainingData = getTrainingData(trainingPositiveTweets, trainingNegativeTweets)

def getTrainedNaiveBayesClassifier(extract_features = extract_features, trainingData = trainingData):
  trainingFeatures=nltk.classify.apply_features(extract_features, trainingData)
  trainedNBClassifier=nltk.NaiveBayesClassifier.train(trainingFeatures) # Train the Classifier
  return trainedNBClassifier

# trainedNBClassifier = getTrainedNaiveBayesClassifier(extract_features,trainingData)

## pickling classifier, vocabulary
# with open('../pickledfiles/twitter_classifier.pickle', 'wb') as f:
#     pickle.dump(trainedNBClassifier, f)
#
#
# with open('../pickledfiles/vocabulary.pickle', 'wb') as vocabulary_file:
#     pickle.dump(vocabulary, vocabulary_file)

## unpickling classifier
with open('./pickledfiles/BernoulliNB.pickle', 'rb') as f:
    trainedNBClassifier = pickle.load(f)

def naiveBayesSentimentCalculator(tweet):
  problemInstance = tweet.split()
  problemFeatures = extract_features(problemInstance)
  return trainedNBClassifier.classify(problemFeatures)

def getTesttweetSentiments(naiveBayesSentimentCalculator):
  testNegResults = [naiveBayesSentimentCalculator(tweet) for tweet in testNegativetweets]
  testPosResults = [naiveBayesSentimentCalculator(tweet) for tweet in testPositivetweets]
  labelToNum = {'positive':1,'negative':-1}
  numericNegResults = [labelToNum[x] for x in testNegResults]
  numericPosResults = [labelToNum[x] for x in testPosResults]
  return {'results-on-positive':numericPosResults, 'results-on-negative':numericNegResults}

#
def runDiagnostics(tweetResult):
  positiveTweetsResult = tweetResult['results-on-positive']
  negativeTweetsResult = tweetResult['results-on-negative']
  numTruePositive = sum(x > 0 for x in positiveTweetsResult)
  numTrueNegative = sum(x < 0 for x in negativeTweetsResult)
  pctTruePositive = float(numTruePositive)/len(positiveTweetsResult)
  pctTrueNegative = float(numTrueNegative)/len(negativeTweetsResult)
  totalAccurate = numTruePositive + numTrueNegative
  total = len(positiveTweetsResult) + len(negativeTweetsResult)
  print("Accuracy on positive tweets = " +"%.2f" % (pctTruePositive*100) + "%")
  print("Accuracy on negative tweets = " +"%.2f" % (pctTrueNegative*100) + "%")
  print("Overall accuracy = " + "%.2f" % (totalAccurate*100/total) + "%")

# reviewResult = getTesttweetSentiments(naiveBayesSentimentCalculator)
# runDiagnostics(reviewResult)
