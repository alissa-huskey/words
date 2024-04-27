"""Word module.

Initially written for syllable comparison.
"""

from syllabifier import syllabifyARPA as syllabify

from peripherals.arpabet_dictionary import DICTIONARY
from peripherals.syllable import Syllable


class Word():
    """A word object."""

    def __init__(self, word=None, client=None):
        """Make the object."""
        self.word = word
        self.client = client

    def __str__(self):
        """str."""
        return self.word or ""

    def __repr__(self):
        """repr."""
        word = self.word or ""
        return f"Word({word!r})"

    def __eq__(self, other):
        """Return True if both prouns are equal."""
        return self.prouns == other.prouns

    @property
    def prouns(self):
        """Get the pronounciation in ARPA notation."""
        if not self.word:
            raise Exception("Can't get the prounciation if there's no word.")
        return DICTIONARY.get(self.word, "")

    @property
    def syllables(self):
        """Get a list of syllabls."""
        return [Syllable(s) for s in syllabify(self.prouns)]

    def difference(self, other):
        """Return the number of syllable differences."""
        mine, theirs = self.syllables, other.syllables

        if mine == theirs:
            return []

        if len(mine) != len(theirs):
            return [True] * (max(len(mine), len(theirs)))

        diffs = [mine[i].difference(theirs[i]) for i in range(len(mine))]
        return [len(x) for x in diffs]

    def diffs(self):
        """."""
        return {m.word: self.difference(m) for m in self.matches}

    @property
    def results(self):
        """Get consonant matches."""
        return self.client.words(rel_cns=self.word, max=100)

    @property
    def matches(self):
        """Get consonant matches."""
        if not self.results:
            return []
        return [Word(w["word"]) for w in self.results if " " not in w["word"]]
