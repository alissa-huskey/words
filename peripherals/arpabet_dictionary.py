"""ARPABET Pronunciation dictionary."""

import pickle
from collections import namedtuple
from pathlib import Path

Line = namedtuple("Line", ("num", "line"))


def make_pron_dict():
    """Create pronunciation dictionary dict.

    Make a Python dictionary from the CMU Pronouncing Dictionary file in the
    form of:

        WORD -> ARPABET Pronunciation
    """
    cache_path = Path(__file__).parent / "pronunciation.cache"
    dictionary = Path(__file__).parent / "cmudict-0.7b"

    if cache_path.is_file() and cache_path.stat().st_size:
        with cache_path.open("rb") as fp:
            return pickle.load(fp)

    first, last = Line(126, b'A  AH0'), Line(-5, b'ZYWICKI  Z IH0 W IH1 K IY0')

    lines = dictionary.read_bytes().splitlines()
    lines[:first.num] = []
    lines[last.num:] = []

    assert lines[0] == first.line, f"The first line should not be: {lines[0]}"
    assert lines[-1] == last.line, f"The last line should not be: {lines[-1]}"

    pron = [line.decode("latin").partition(" ") for line in lines]
    words = {(line[0].lower()): line[2].strip() for line in pron}

    with cache_path.open("wb") as fp:
        pickle.dump(words, fp)
    return words


DICTIONARY = make_pron_dict()
