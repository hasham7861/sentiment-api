from flask import Flask, jsonify
from sentifish import Sentiment

application = app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        "status": "Api is running",
        "suggestion": "/predict/<text> is the route to get sentiment analyze"
    })


@app.route('/predict/<text>')
def predict_sentiment(text):
    obj = Sentiment(text)
    polarity = obj.analyze()
    positive = obj.isPositive()
    resp = jsonify(
        {"input_text": text, "postive": positive, "polarity": polarity})

    return resp
