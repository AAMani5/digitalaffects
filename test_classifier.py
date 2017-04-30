import pytest
from NBclassifier import getVocabulary

def multiply(a, b):
    return a * b

def test_numbers_3_4():
    assert multiply(3,4) == 12
