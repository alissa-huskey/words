"""Generate random sentences from text files."""

from pathlib import Path
from re import compile as re_compile

from nltk import sent_tokenize
from rich.console import Console
from rich.table import Table

from words import bp  # noqa

abbr_matcher = re_compile(r'^([A-Z][.])+$')

abbrevs = Table(show_lines=True)


def starts_lower(text):
    """Return True if the text starts with a lowercase letter."""
    return text[0].islower()


def starts_i(text):
    """Return True if the text starts with "I "."""
    return text[0:2] == "I "


def ends_quoted(text):
    """Return True if the text ends in double or single quotes."""
    return text[-1] in ('"', "'")


def ends_interruptable(text):
    """Return True if the text ends in certain punctuation."""
    return text[-1] in ("!", "?", ")", )


def ends_abbrev(text):
    """Return True if the sentence ends in an abbreviation.

    E.S.E.
    S.

    Example:
        >>> is_quoted(
            "In the meantime Mrs.",
            "Darling had put the children to bed for supper."
        )
        True
    """
    abbrs = ("Mr.", "Mrs.", "Ms.", "etc.", "Etc.", "lat.", "lbs.", "deg.", "ft.")
    word = text.rsplit(maxsplit=1)[-1]
    if word in abbrs:
        abbrevs.add_row(word, text)
        return True


def is_quoted(start, end):
    """Return True if the sentences should go together because of a quote.

    Example:
        >>> is_quoted('"That is nice,"', 'he said')
        True
    """
    return (ends_quoted(start) and (starts_lower(end) or starts_i(end)))


def is_interrupted(start, end):
    """Return True if the sentences should be joined due to punctuation.

    Example:
        >>> is_interrupted("Sing Ho!", "for the life of a Bear!")
        True
    """
    return ends_interruptable(start) and starts_lower(end)


def main():
    """Random sentences."""
    rootdir = Path("assets/prose")
    books = list(rootdir.iterdir())
    console = Console()
    table = Table("Book", "Sentence")
    #  table = Table("Book", "Sentence")

    new = None
    for book in books:
        title = book.name.replace("-", " ").title()
        text = book.read_text()
        paragraphs = text.split("\n\n")

        console.rule(title)

        fixed = Table("Fixed", show_lines=True)
        leftover = Table("Prev", "This", show_lines=True)

        for ii, p in enumerate(paragraphs):
            p = p.replace("\n", " ")
            sentences = sent_tokenize(p)
            #  revised = []
            revised = Table()

            mx = len(sentences)
            i = 0
            while i < mx:
                s = sentences[i]

                x = 1
                new = s

                while True:
                    idx = i + x

                    if idx >= mx:
                        break

                    nxt = sentences[idx]

                    if not (
                        is_quoted(new, nxt) or
                        is_interrupted(new, nxt) or
                        ends_abbrev(new)
                    ):
                        break

                    new = " ".join((new, nxt)).replace("\n", " ")
                    x += 1

                revised.add_row(new)
                i += x

                if x > 1:
                    fixed.add_row(new)

                if nxt[0].islower():
                    leftover.add_row(new, nxt)

                table.add_row(book.name, s)

        #  console.print(abbrevs)
        console.print(revised)


main()
