import google_nlp
import os
import pytest


nlp = google_nlp.init()

def analyze(c):
    emotion = google_nlp.analyze_sentiment(nlp, c)
    return emotion

def test_negative_comment():
    Mycomments = ["awful day“]
    for c in comments:
        sentiment = analyze(c)
        assert emotion.score < 0

def test_positive_comment():  
    comments = ["good day!"]
    for c in comments:
        sentiment = analyze(c)
        assert emotion.score > 0

if __name__ == '__main__':
    pytest.main("test_google_nlp.py")
