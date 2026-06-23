from collections import Counter


def extract_keywords(text):

    words = text.lower().split()

    stop_words = {

        "the",

        "a",

        "an",

        "is",

        "are",

        "of",

        "to",

        "and",

        "in",

        "for",

        "with"

    }

    words = [

        word

        for word in words

        if word not in stop_words

        and len(word) > 3

    ]

    common = Counter(words)

    return common.most_common(5)