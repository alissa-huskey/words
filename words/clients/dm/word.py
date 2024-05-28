"""Datamuse word module."""

from words import WordsError, bp  # noqa
from words.object import Object


class Word(Object):
    """Word class."""

    PARTS_OF_SPEECH = ('a', 'adj', 'adv', 'n', 'prop', 'u', 'v')
    word: str = None

    def __init__(self, **kwargs):
        """Create the object."""
        self._tags = []
        self._parts = []

        super().__init__(**kwargs)

    def __gt__(self, other):
        """Sort Word by word."""
        return (self.word > other.word)

    def __str__(self):
        """Return word or repr."""
        if self.word:
            return self.word
        return repr(self)

    @property
    def tags(self):
        """Get tags."""
        return self._tags

    @tags.setter
    def tags(self, value):
        """Set tags, parts and other "key:value" formatted values based on tags."""
        for text in value:
            if text.lower() in self.PARTS_OF_SPEECH:
                self._parts.append(text)
                continue
            elif ":" in text:
                k, v = text.split(":")
                setattr(self, k, v)
            else:
                self._tags.append(text)

    @property
    def parts(self):
        """Get part of speech."""
        return self._parts
