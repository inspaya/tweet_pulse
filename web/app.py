from os import path as os_path
from sys import path as sys_path
from flask import Flask, request, render_template

sys_path.append(os_path.abspath('..'))
from google_nlp import google_sentiment_analysis as google_sa
from stanford_corenlp import stanford_sentiment_analysis as corenlp_sa
from __init__ import get_user_tweets_from_timeline

app = Flask(__name__)

nlp_libraries = {
    'google_nlp': google_sa.analyze_text,
    'stanford_nlp': corenlp_sa.analyze
}

@app.route("/", methods=['GET', 'POST'])
def extract_sentiment():
    if request.method == 'POST':
        nlp_library = request.form["nlp_library_option"]
        input_text = request.form["one_or_more_sentences"]
        annotations = nlp_libraries[nlp_library](input_text)
        return render_template('results.html', annotations=annotations)
    return render_template('index.html')


@app.route("/twitter_user", methods=['POST'])
def get_twitter_timeline():
    if request.method == 'POST':
        twitter_user = request.form["twitter_user_handle"]
        tweets = get_user_tweets_from_timeline(twitter_user)
        if type(tweets) == list:
            annotations = google_sa.analyze_batch(tweets)
        else:
            annotations = google_sa.analyze(tweets)
        return render_template('results.html', annotations=annotations)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
