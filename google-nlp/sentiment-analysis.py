"""
Adapted from https://cloud.google.com/natural-language/docs/sentiment-tutorial

Demonstrates how to make a simple call to the Natural Language API.
"""

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has score of {}'.format(
            index, sentence_sentiment
        ))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude
    ))
    return 0


def analyze(input_filename):
    client = language.LanguageServiceClient()

    with open(input_filename, 'r') as review_file:
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    print_result(annotations)


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

    analyze(args.input_filename)
