from corenlp import CoreNLPClient


def generate_sentiments(annotation):
    pass


def analyze(content):
    with CoreNLPClient(annotators='sentiment'.split()) as client:
        annotation = client.annotate(content)

    return generate_sentiments(annotation)
