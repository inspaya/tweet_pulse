"""
Adapted from https://cloud.google.com/natural-language/docs/sentiment-tutorial

Demonstrates how to make a simple call to the Natural Language API.
"""

import csv
import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

"""
Interpretation of Sentiment Analysis as per guidance from
https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values

score		- the overall emotion of a document
magnitude	- how much emotional content is present within the document,
            and this value is often proportional to the length of the document

Examples:
1. A document with a score of 0.0 is clearly 'Neutral' if the magnitude is also low e.g. 0.x
2. A document with a score of 0.0 is considered 'Mixed' if the magnitude is high e.g. x.y
(where x is > 0) if the volume of Positive and Negative sentiments cancel each other out.
3. A document with score less than 0.0 is 'Negative'
4. A document with score greater than 0.0 is 'Positive'

For the purpose of this exercise, we will not dive into clearly Positive/Negative sentiments.
However, the suggested values from the docs are worth nothing:

Clearly Positive*	"score": 0.8, "magnitude": 3.0
Clearly Negative*	"score":-0.6, "magnitude": 4.0
Neutral			    "score": 0.1, "magnitude": 0.0
Mixed			    "score": 0.0, "magnitude": 4.0
"""
score = 0.0
magnitude = 0.0
sentence_sentiment_list = []


def assign_sentiment(score, magnitude):
    if score > 0.5 and magnitude >= 0.5:
        sentiment = 'Positive'
    elif score < 0.0:
        sentiment = 'Negative'
    elif score == 0.0 and magnitude < 1.0:
        sentiment = 'Neutral'
    elif score == 0.0 and magnitude > 2.0:
        sentiment = 'Mixed'
    else:
        sentiment = 'no detectable '

    return sentiment


def generate_sentiments(annotations):
    for index, sentence in enumerate(annotations.sentences):
        sentence_text = sentence.text.content
        sentence_sentiment = sentence.sentiment.score
        sentence_magnitude = sentence.sentiment.magnitude
        print('Sentence {} has score of {} and magnitude of {}'.format(
            sentence_text, sentence_sentiment, sentence_magnitude
        ))

        sentiment = assign_sentiment(sentence_sentiment, sentence_magnitude)
        sentence_sentiment_list.append((sentence.text.content, sentiment,))

    with open('buffer.csv', 'w+') as data_buffer: # TODO: replace with filename of subject in data/tweets/ dir
        csv_writer = csv.writer(data_buffer)
        csv_writer.writerows(sentence_sentiment_list)
    return sentence_sentiment_list


def analyze_text(text_string):
    return analyze(text_string)


def analyze_file(input_filename):
    with open(input_filename, 'r') as review_file:
        content = review_file.read()

    return analyze(content)


def analyze_batch(content_list):
    annotations_list = []
    for content in content_list:
        new_annotation = analyze(content)
        annotations_list.extend(new_annotation)

    return list(set(annotations_list))


def analyze(content):
    client = language.LanguageServiceClient()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    return generate_sentiments(annotations)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'input_filename',
        help='The filename of the movie review you\'d like to analyze'
    )
    args = parser.parse_args()

    analyze_file(args.input_filename)
