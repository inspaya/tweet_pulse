from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.abspath('..'))

from flask import Flask, request, render_template
app = Flask(__name__)

from google_nlp import sentiment_analysis as sa

@app.route("/", methods=['GET','POST'])
def extract_sentiment():
    if request.method == 'POST':
        return "Extracting Sentiment from {}".format(request.form["one_line_sentence"])
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
