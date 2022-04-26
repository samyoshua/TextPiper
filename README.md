# TextPiper

This is a really simple base class to preprocess text. The built in processors are minimal and have no additional requirements. The built-in functions can be seen in `processors.py` and are set as a default pipeline. All expect a string as an input and output a string except tokenize (so tokenization should be left until the end of the pipeline if used).

The default pipeline is:
 - `casefold` (lowercase)
 - `remove_punctuation` (see `constants.ALLOWED_CHARS`)
 - `remove_stopwords` (see `constants.STOPWORDS`)
 - `trim_whitespace`
 - `tokenize` (just a simple `.split()`)

## Example

A minimal use case (casefolding) can be seen below
```python
from text_piper import TextPiper

texts = ["Hello World"]
for text in TextPiper(texts, pipeline=[lambda x: x.casefold()]):
    print(text)

>> "hello world"
```

## Testing

Unit tests can be found in the `tests` directory and can be run using `pytest`.

## TODO:

- Add multiprocessing
- Improve default pipeline
- Add ngram/shingling
