"""Get a random line from a file."""

from collections import namedtuple
from functools import cached_property
from pathlib import Path
from random import choices
from re import sub as re_sub

from nltk import sent_tokenize

from words import bp, WordsError  # noqa
from words.object import Object


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


class Sentence(namedtuple("Sentence", ["text", "source"])):
    """Sentence class."""

    @property
    def title(self):
        """Return the source title."""
        return self.source.title


class RandomParagraph():
    """Randomly selected sentences from a paragraph of text."""

    _text: str = None

    def __init__(self, text: str = None, source=None):
        """Create the object."""
        self.text = text
        self.source = source

    @property
    def text(self):
        """Get text."""
        return self._text

    @text.setter
    def text(self, value):
        """Set text."""
        if not value:
            return

        self._text = re_sub(r"\s+", " ", value.strip())

    @property
    def sentences(self) -> list[str]:
        """Return a list of sentences."""
        if not self.text:
            return []

        return sent_tokenize(self.text)

    def get(self, count: int = 1) -> list[str]:
        """Return a randomly selected list of sentences."""
        return [Sentence(x, self) for x in choices(self.sentences, k=count)]

    @property
    def title(self):
        """Return the source title."""
        if not self.source:
            return ""
        return self.source.title


class RandomProse():
    """Randomly selected paragraphs from a prose file."""

    def __init__(self, file: Path = None):
        """Create the object."""
        self.file = file

    @property
    def title(self) -> str:
        """Return the title of the file."""
        name = self.file.name
        return name[:-4].replace("-", " ").title()

    @cached_property
    def text(self) -> str:
        """Return the contents of the file."""
        return self.file.read_text()

    @cached_property
    def paragraphs(self) -> list[str]:
        """Return a list of paragraphs in the file."""
        return self.text.split("\n\n")

    def get(self, count: int = 1) -> list[str]:
        """Get a randomly selected list of paragrpahs."""
        return [RandomParagraph(x, self) for x in choices(self.paragraphs, k=count)]


class RandomBooks(Object):
    """Random selection of book files."""

    ROOT = Path(__file__).parent.parent / "assets" / "prose"

    _selection = []

    @cached_property
    def files(self) -> list[Path]:
        """Return a list of text files that contain books."""
        return list(self.ROOT.iterdir())

    def get(self, count: int = 1) -> list[Path]:
        """Return a list of randomly selected book files."""
        return [RandomProse(x) for x in choices(self.files, k=count)]
