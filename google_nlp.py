# -*- coding: utf-8 -*-
"""google_nlp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YOf-ScaaDi0FQ6Pm68x0eMsb9yneiLIe
"""

!export GOOGLE_APPLICATION_CREDENTIALS="/content/tidy-arcade-290903-a589145de641.json"

!gcloud auth activate-service-account --key-file="/content/tidy-arcade-290903-a589145de641.json"

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/content/tidy-arcade-290903-a589145de641.json"

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('My Project 30963-4186ddea0f9c.json')

from google.cloud import language
from google.cloud.language import enums, types


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = [
        ('text', text),
        ('score', sentiment.score),
        ('magnitude', sentiment.magnitude),
    ]
    for k, v in results:
        print('{:10}: {}'.format(k, v))

text1 = 'I am sad today because I have a lot of homework!'
analyze_text_sentiment(text1)

text2 = 'I want to go to the beach'
analyze_text_sentiment(text2)

text3 = 'The moon is beautiful'
analyze_text_sentiment(text3)

text4 = 'When do you want to eat'
analyze_text_sentiment(text4)

text5 = 'I have a job offer'
analyze_text_sentiment(text5)

text6 = 'I want to cook steak for dinner'
analyze_text_sentiment(text6)