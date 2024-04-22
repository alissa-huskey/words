"""Datamuse API Wrapper."""

from enum import Enum, EnumMeta

from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.traceback import install as rich_tracebacks
from typer import BadParameter, Option, Typer
from typing_extensions import Annotated

from words.compat import BdbQuit
from words.datamuse import Datamuse
from words.word_presenter import WordPresenter

cli = Typer()
console = Console(stderr=True)
rich_tracebacks(show_locals=True)


class EnumContains(EnumMeta):
    """Metaclass to allow membership checking."""

    def __contains__(cls, value):
        """Return True if value is a name or value of any enum object in class."""
        if value in cls.__members__:
            return True
        try:
            cls(value)
        except ValueError:
            return False
        return True


class MetadataFlags(str, Enum, metaclass=EnumContains):
    """Possible values for the Metadata (`--md`) parameter.

    Flags representing categories of extra lexical knowledge to include.
    """

    d = "d"    # "Definitions"
    p = "p"    # "Parts of Speech"
    s = "s"    # "Syllable count"
    r = "r"    # "Pronunciation"
    f = "f"    # "Word frequency"

    def __init__(self, title):
        """Use the name as the value for typer Option."""
        self.flag, self.title = self._name_, title
        self._value_ = self.flag


def check_metadata(value: str):
    """Validate all letters for metadata."""
    if not value:
        return
    for flag in iter(value):
        if flag not in MetadataFlags:
            raise BadParameter(f"Invalid metadata (--md) flag: {flag}")
    return value


@cli.command()
def words(
    ml: Annotated[str, Option(help="Meaning like.", metavar="WORD")] = "",
    md: Annotated[str, Option(
        metavar="FLAG",
        case_sensitive=False,
        help="Metadata to include.",
        callback=check_metadata,
        show_default=False,
    )] = None,
    max: Annotated[int, Option(help="Max results.", metavar="NUMBER")] = 30,
    ipa: Annotated[int, Option(
        help="Use International Phonetic Alphabet pronunciation format.",
    )] = 0,
    json: Annotated[bool, Option(
        "--json",
        help="Export as raw JSON",
        show_default=False,
    )] = False,
    long: Annotated[bool, Option(
        "--long", "-l",
        help="Print word list in long format.",
    )] = False,
):
    """Print results from the primary datamuse endpoint."""
    api = Datamuse(ml=ml, md=md, max=max, ipa=ipa)
    api.get()

    if json:
        rprint(api.data)
        return

    if long:
        table = Table(*WordPresenter.headers())
        for w in api.words:
            word = WordPresenter(w)
            table.add_row(*word.columns)
        console.print(table)
    else:
        for word in api.words:
            print(word)


def run():
    """Command line runner."""
    try:
        cli()
    except (SystemExit, BdbQuit):
        ...
    #  except BaseException as e:
    #      rprint("[red]Error[/red]", e)
    #      exit(1)


if __name__ == "__main__":
    run()
