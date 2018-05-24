from os import path as os_path
from sys import path as sys_path
from flask import Flask, request, render_template

sys_path.append(os_path.abspath('..'))
from google_nlp import sentiment_analysis as sa

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def extract_sentiment():
    if request.method == 'POST':
        input_text = request.form["one_or_more_sentences"]
        annotations = sa.analyze_text(input_text)
        return render_template('results.html', annotations=annotations)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
