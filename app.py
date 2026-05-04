from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['sentence']
        sentiment_score, sentiment_label = analyze_sentiment(user_input)
        return render_template('result.html', user_input=user_input, sentiment_score=sentiment_score, sentiment_label=sentiment_label)
    return render_template('index.html')


def analyze_sentiment(input_text):
    analysis = TextBlob(input_text)
    sentiment_score = analysis.sentiment.polarity  # Sentiment score between -1 and 1
    if sentiment_score > 0:
        sentiment_label = "Positive"
    elif sentiment_score < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    print("Input Text:", input_text)
    print("Sentiment Score:", sentiment_score)
    print("Sentiment Label:", sentiment_label)

    return sentiment_score, sentiment_label

if __name__ == '__main__':
    app.run(debug=True)

