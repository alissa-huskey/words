"""Generate random sentences from text files."""

from pathlib import Path
from random import choice, choices

from nltk import sent_tokenize
from rich import box
from rich.console import Console
from rich.panel import Panel

from words import bp  # noqa

FORMAT = "pretty"
COUNT = 5
WIDTH = 80

TYPE = "paragraph"


def main():
    """Random sentences."""
    rootdir = Path("assets/prose")
    books = choices(list(rootdir.iterdir()), k=COUNT)
    console = Console()

    for book in books:
        title = book.name[:-4].replace("-", " ").title()
        text = book.read_text()
        paragraphs = text.split("\n\n")
        p = choice(paragraphs)

        if TYPE == "sentence":
            sentences = sent_tokenize(p)
            chosen = choice(sentences).replace("\n", " ")
        else:
            chosen = p

        if FORMAT == "pretty":
            panel = Panel(
                chosen, padding=(1, 3),
                width=WIDTH,
                subtitle=f"-- {title}",
                subtitle_align="right",
                box=box.MINIMAL,
            )

            console.print(panel)
        else:
            print(chosen)

    console.line()


main()
