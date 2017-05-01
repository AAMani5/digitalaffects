import pytest
from digitalaffects.NBclassifier import getVocabulary, extract_features, getTrainingData, getTrainedNaiveBayesClassifier

def multiply(a, b):
    return a * b

def test_numbers_3_4():
    assert multiply(3,4)==12

def test_extract_features():
    assert set(extract_features("this is a test").values()) == set([False,True])

def test_getVocabulary():
    vocabulary = getVocabulary(["amazing", "great"],["terrible","worst"])
    test_vocabulary = ["great", "worst", "amazing", "terrible"]
    actual = set(vocabulary).intersection(test_vocabulary)
    expected = {"great", "worst", "amazing", "terrible"}
    assert actual == expected


def test_getTrainingData():
    assert getTrainingData(["amazing", "great"],["terrible","worst"]) == [(["terrible"],'negative'),(["worst"],'negative'),(['amazing'],'positive'),(['great'], 'positive')]
