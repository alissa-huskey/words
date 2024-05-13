"""Get a random line from a file."""

from pathlib import Path
from random import choices

from words import WordsError


class Random():
    """Get a random line from a file."""

    ROOT = Path(__file__).parent.parent / "peripherals"

    def __init__(self, file=None, max=0):
        """Create an object."""
        self.file = file and Path(file)
        self.max = max or None

    @property
    def lines(self):
        """Return the lines in the file."""
        if not self.file:
            raise WordsError("No lines without file.")
        if not self.file.is_file():
            raise WordsError(f"No such file: {self.file}")
        lines = self.file.read_text().splitlines()

        return lines[:self.max]

    def get(self, count=1):
        """Get random lines from the file."""
        return choices(self.lines, k=count)


class RandomName(Random):
    """Get a random name."""

    def __init__(self, name, **kwargs):
        """Create the object."""
        path = self.ROOT / f"{name}-names.txt"
        return super().__init__(file=path, **kwargs)
