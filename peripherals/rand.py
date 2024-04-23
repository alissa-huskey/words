"""Get one or more random words from a local dictionary.

Usage: python rand.py [NUM_WORDS]
"""

from pathlib import Path
from random import choices
from sys import argv, exit

from rich import print


def main(count=1):
    """Return a random word."""
    count = int(count)
    filename = "/usr/share/dict/words"
    path = Path(filename)
    if not path.is_file():
        print(f"[red]Error:[/red] Could not open dictionary file {filename!r}.")
        exit(1)
    text = path.read_text()
    lines = text.strip().splitlines()
    words = choices(lines, k=count)
    return words


if __name__ == "__main__":
    words = main(*argv[1:2])
    for word in words:
        print(word)
