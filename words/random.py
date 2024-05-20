"""Get a random line from a file."""

from pathlib import Path
from random import choices

from words import WordsError

bp = breakpoint


class Random():
    """Get a random line from a file."""

    ROOT = Path(__file__).parent.parent / "assets"

    def __init__(self, file=None, max=0, length_range=None):
        """Create an object."""
        self.file = file and Path(file)
        self.max = max or None
        self.length_range = length_range

    @property
    def lines(self):
        """Return the lines in the file."""
        if not self.file:
            raise WordsError("No lines without file.")
        if not self.file.is_file():
            raise WordsError(f"No such file: {self.file}")
        lines = self.file.read_text().splitlines()

        if self.length_range:
            min_length, max_length = self.length_range
            if max_length:
                pred = lambda word: len(word) >= min_length and len(word) <= max_length
            else:
                pred = lambda word: len(word) >= min_length
            lines = [line for line in lines if pred(line)]

        return lines[:self.max]

    def get(self, count=1):
        """Get random lines from the file."""
        return choices(self.lines, k=count)


class RandomName(Random):
    """Get a random name."""

    def __init__(self, name, **kwargs):
        """Create the object."""
        path = self.ROOT / "names" / f"{name}-names.txt"
        return super().__init__(file=path, **kwargs)


class RandomWord(Random):
    """Get a random word."""

    def __init__(self, **kwargs):
        """Create the object."""
        path = self.ROOT / "wordlists" / "dictionary.txt"
        return super().__init__(file=path, **kwargs)
