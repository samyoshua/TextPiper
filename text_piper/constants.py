import string

ALLOWED_CHARS = set(string.ascii_letters + string.digits).union(["#", "+", "'", "."])


STOPWORDS = {
    "yourself",
    "least",
    "an",
    "am",
    "behind",
    "ever",
    "every",
    "if",
    "upon",
    "though",
    "therefore",
    "thereupon",
    "nevertheless",
    "bottom",
    "see",
    "whom",
    "several",
    "only",
    "everyone",
    "forty",
    "nowhere",
    "either",
    "former",
    "in",
    "mostly",
    "’ve",
    "take",
    "above",
    "i",
    "alone",
    "beforehand",
    "hundred",
    "via",
    "thereby",
    "whereafter",
    "around",
    "’s",
    "out",
    "serious",
    "same",
    "say",
    "why",
    "give",
    "just",
    "has",
    "and",
    "enough",
    "once",
    "eleven",
    "its",
    "also",
    "indeed",
    "when",
    "both",
    "across",
    "'s",
    "get",
    "less",
    "always",
    "neither",
    "whoever",
    "ours",
    "everywhere",
    "otherwise",
    "does",
    "after",
    "seeming",
    "yet",
    "your",
    "might",
    "‘m",
    "sometimes",
    "elsewhere",
    "who",
    "whole",
    "whereby",
    "as",
    "onto",
    "become",
    "the",
    "so",
    "’ll",
    "have",
    "which",
    "five",
    "‘ve",
    "him",
    "under",
    "six",
    "used",
    "therein",
    "any",
    "anything",
    "do",
    "done",
    "his",
    "was",
    "due",
    "never",
    "hereafter",
    "during",
    "third",
    "doing",
    "full",
    "others",
    "last",
    "fifty",
    "'d",
    "been",
    "by",
    "against",
    "herein",
    "however",
    "should",
    "thru",
    "until",
    "else",
    "many",
    "top",
    "without",
    "'ve",
    "down",
    "put",
    "how",
    "part",
    "their",
    "using",
    "were",
    "whose",
    "somewhere",
    "along",
    "front",
    "meanwhile",
    "thereafter",
    "ten",
    "nothing",
    "whereupon",
    "yourselves",
    "regarding",
    "per",
    "but",
    "something",
    "two",
    "even",
    "are",
    "me",
    "somehow",
    "‘ll",
    "nobody",
    "could",
    "four",
    "often",
    "besides",
    "unless",
    "anyhow",
    "sixty",
    "various",
    "cannot",
    "sometime",
    "amongst",
    "our",
    "three",
    "all",
    "seems",
    "had",
    "themselves",
    "twelve",
    "very",
    "’d",
    "still",
    "into",
    "since",
    "before",
    "few",
    "well",
    "can",
    "he",
    "of",
    "then",
    "seem",
    "hers",
    "about",
    "except",
    "made",
    "not",
    "whenever",
    "much",
    "becomes",
    "ca",
    "show",
    "quite",
    "anyone",
    "ourselves",
    "everything",
    "eight",
    "whatever",
    "wherever",
    "hence",
    "yours",
    "these",
    "himself",
    "noone",
    "no",
    "did",
    "almost",
    "than",
    "latterly",
    "on",
    "already",
    "or",
    "whereas",
    "be",
    "n‘t",
    "through",
    "throughout",
    "'ll",
    "them",
    "moreover",
    "n’t",
    "’m",
    "move",
    "will",
    "n't",
    "latter",
    "‘re",
    "please",
    "more",
    "nine",
    "that",
    "such",
    "with",
    "make",
    "beyond",
    "a",
    "my",
    "hereupon",
    "twenty",
    "myself",
    "anyway",
    "go",
    "afterwards",
    "she",
    "nor",
    "over",
    "name",
    "for",
    "one",
    "further",
    "up",
    "mine",
    "where",
    "herself",
    "keep",
    "side",
    "first",
    "‘d",
    "toward",
    "‘s",
    "formerly",
    "amount",
    "her",
    "re",
    "next",
    "none",
    "became",
    "you",
    "together",
    "because",
    "some",
    "rather",
    "they",
    "seemed",
    "thus",
    "anywhere",
    "'re",
    "beside",
    "again",
    "to",
    "whether",
    "own",
    "perhaps",
    "may",
    "whence",
    "thence",
    "call",
    "too",
    "those",
    "between",
    "us",
    "while",
    "empty",
    "someone",
    "this",
    "back",
    "although",
    "must",
    "itself",
    "below",
    "most",
    "'m",
    "fifteen",
    "wherein",
    "whither",
    "now",
    "there",
    "within",
    "hereby",
    "what",
    "namely",
    "here",
    "off",
    "each",
    "would",
    "at",
    "other",
    "is",
    "being",
    "becoming",
    "’re",
    "it",
    "from",
    "really",
    "we",
    "another",
    "among",
    "towards",
}