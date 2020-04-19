from flask import Flask
from textblob import TextBlob

application = Flask(__name__)


@application.route('/')
def index():
    return "/predict/< text > is the route to get sentiment analyze"


@application.route('/predict/<text>')
def predict_sentiment(text):
    analysis = TextBlob(text)
    resp = analysis.sentiment.polarity
    print(resp)
    return '<h1>polarity: {}</h1>'.format(resp)


# run the app.
if __name__ == "__main__":
    application.run()
