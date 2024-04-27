"""Syllable-level phoneme comparison.

Compares the phoneme of each syllable of two words. This turned out to be
fairly useless, since I thought at the time that it had something to do with
consonant matching.
"""

from pprint import pprint

from datamuse import Datamuse

from peripherals.word import Word


def main():
    """Do the stuff."""
    client = Datamuse()

    strings = (
        "sample",
        "awake",
        "beach",
        "cow",
        "slack",
        "dessert",
        "sandy",
        "late",
        "car",
    )
    words = [Word(w, client) for w in strings]

    diffs = {w.word: w.diffs() for w in words}
    pprint(diffs)


if __name__ == "__main__":
    main()
