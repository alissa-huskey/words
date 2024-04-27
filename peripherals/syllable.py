"""Syllable module."""

from itertools import filterfalse


class Syllable():
    """A Syllable."""

    def __init__(self, syl):
        """Make the object."""
        self.syl = syl

    def __repr__(self):
        """repr."""
        return f"Syllable({self.syl!r})"

    def __eq__(self, other):
        """Return True if the syllable strings are equal."""
        return self.syl == other.syl

    def __hash__(self):
        """Use syl string for hashing."""
        return hash(self.syl)

    @property
    def phonemes(self):
        """Get the phonemes."""
        return self.syl.split()

    def difference(self, other):
        """Return the difference between this and another sylable.

        Return a tuple that contains the index number for each of the
        respective phonemes that differ.
        """
        # no need to check, there's no difference
        if self == other:
            return tuple()

        mine, theirs = self.phonemes, other.phonemes

        # unreasonable to check if the number of phonemes isn't the same
        # this is sloppy, but I haven't thought of a better way
        if len(mine) != len(theirs):
            return [True] * len(mine)

        # use this predicate checker to get the index numbers of differing
        # phonemes in a generator
        checker = lambda i: mine[i] == theirs[i]        # noqa: E731
        diff = filterfalse(checker, range(len(mine)))

        # return it as a tuple
        return tuple(diff)
