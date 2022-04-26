from inspect import isgeneratorfunction

from .processors import (
    casefold,
    remove_punctuation,
    remove_stopwords,
    tokenize,
    trim_whitespace,
)

DEFAULT_PIPELINE = [
    casefold,
    remove_punctuation,
    remove_stopwords,
    trim_whitespace,
    tokenize,
]


class TextPiper:
    """
    A simple object to iterate over a corpus with a preprocessing pipeline.

    :param corpus, iter - an iterable of unprocessed texts
    :param pipeline, list(,optional) - a list of preprocessing functions
        each with input str and output str (so tokenize should be final step)

    Can then be iterated over returning either strings (or lists of tokens).
    """

    def __init__(self, corpus: iter, pipeline=DEFAULT_PIPELINE) -> None:
        self.corpus = corpus
        self.is_generator = isgeneratorfunction(self.corpus)
        self.pipeline = pipeline

    def __iter__(self):
        items = self.corpus() if self.is_generator else self.corpus
        for item in items:
            for pipe in self.pipeline:
                item = pipe(item)
            yield item

    def __len__(self) -> int:
        return None if self.is_generator else len(self.corpus)
