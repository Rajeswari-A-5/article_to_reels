import os

os.environ["NLTK_DATA"] = "/opt/render/nltk_data"

import nltk

nltk.download("punkt")

nltk.download("punkt_tab")

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.stemmers import Stemmer


def summarize_text(text, sentences=5):

    parser = PlaintextParser.from_string(
        text,
        Tokenizer("english")
    )

    stemmer = Stemmer("english")

    summarizer = LuhnSummarizer(stemmer)

    summary = summarizer(
        parser.document,
        sentences
    )

    return [str(sentence) for sentence in summary]