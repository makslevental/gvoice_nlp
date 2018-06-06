# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os, json

# Instantiates a client
client = language.LanguageServiceClient()
conversations = json.load(open('conversations.json'))
messages = json.load(open('messages.json'))
# The text to analyze

for convo in conversations[:20]:
    me = filter(lambda msg: msg['name'] == 'Me', convo)
    text = '. '.join(map(lambda msg: msg['body'], me))
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))