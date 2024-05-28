"""Individual matches received from a DICT database."""

from collections import namedtuple

from words import bp, WordsError  # noqa


class DictionaryEntry(namedtuple('DictionaryEntry',
                                 ("word", "db", "definition", "dbname"))):
    """Class representing a single match received from a dictionary request response."""
