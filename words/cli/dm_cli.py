"""CLI for words dm command group."""

import click
from rich import print as rprint
from rich.table import Table

from words.cli import console, err
from words.datamuse_api import DatamuseAPI
from words.datamuse_options import DatamuseOptions
from words.word_presenter import WordPresenter

bp = breakpoint


def _(**kwargs):
    """Datamuse API wrapper."""
    has_required = filter(None, map(kwargs.get, DatamuseOptions.cli_required))
    if not tuple(has_required):
        err("No search option provided.")
        return

    api = DatamuseAPI(**kwargs)
    api.get()

    if api.json:
        rprint(api.data)
        return

    if api.long:
        table = Table(*WordPresenter.headers())
        for w in api.words:
            word = WordPresenter(w)
            table.add_row(*word.columns)
        console.print(table)
    else:
        for word in api.words:
            print(word)


dm_cmd = click.Command("dm", callback=_, help=_.__doc__, params=[
    *DatamuseOptions.cli_options,
    click.Option(["--json"], is_flag=True, help="Export as raw JSON."),
    click.Option(["--long"], is_flag=True, help="Print word list in long format."),
])
