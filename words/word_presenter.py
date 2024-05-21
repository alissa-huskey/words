"""Module for preparing a Word object for printing.

(Like a controller.)
"""

from words import WordsError, bp  # noqa
from words.object import Object
from words.word import Word


class WordPresenter(Object):
    """Prepare a word for printing."""

    HEADERS = ("Parts", "Word")
    """Default table header for long view."""

    word: Word = None
    """Word object."""

    _headers: None

    def __init__(self, word, **kwargs):
        """Create the object."""
        super().__init__(**kwargs)
        self.word = word

    def __str__(self):
        """Return the object string."""
        return str(self.word)

    @classmethod
    def headers(cls, *args):
        """Get headers."""
        return cls.HEADERS + args

    @property
    def parts(self):
        """Return a formatted list of word parts."""
        return ", ".join(self.word.parts)

    @property
    def columns(self):
        """Return a formatted list of word columns values."""
        return (fr"{self.parts}", str(self))
