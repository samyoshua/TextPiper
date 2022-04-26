from .constants import ALLOWED_CHARS, STOPWORDS


def casefold(text):
    return text.casefold()


def remove_punctuation(text):
    return "".join(x if x in ALLOWED_CHARS else " " for x in text)


def remove_stopwords(text):
    return " ".join(word for word in text.split() if word.lower() not in STOPWORDS)


def tokenize(text):
    return text.split()


def trim_whitespace(text):
    return " ".join(text.split())
