from text_piper.processors import (
    casefold,
    remove_punctuation,
    remove_stopwords,
    tokenize,
    trim_whitespace,
)


def test_casefold():
    assert casefold("Fluß") == "fluss"


def test_remove_punctuation():
    assert remove_punctuation("hello!") == "hello "


def test_remove_stopwords():
    assert remove_stopwords("I am a test") == "test"


def test_tokenize():
    assert tokenize("hello world") == ["hello", "world"]


def test_trim_whitespace():
    assert trim_whitespace("  hello     world   ") == "hello world"
