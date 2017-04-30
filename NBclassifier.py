from nltk.corpus import twitter_samples

positiveTweets = twitter_samples.strings('positive_tweets.json')
negativeTweets = twitter_samples.strings('negative_tweets.json')

testTrainingSplitIndex = 2500

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
    tweet_words=set(tweet)
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

vocabulary = getVocabulary(trainingPositiveTweets, trainingNegativeTweets)
