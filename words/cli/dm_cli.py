"""CLI for words dm command group."""

import click
from rich import print as rprint
from rich.table import Table

from words import WordsError, bp  # noqa
from words.cli import ui  # noqa
from words.datamuse_api import DatamuseAPI
from words.datamuse_options import DatamuseOptions
from words.word_presenter import WordPresenter


def _(**kwargs):
    """Datamuse API wrapper.

    Query the Datamuse API.
    """
    has_required = filter(None, map(kwargs.get, DatamuseOptions.cli_required))
    if not tuple(has_required):
        ui.err("No search option provided.")
        return

    api = DatamuseAPI(**kwargs)
    api.get()

    if api.json:
        rprint(api.data)
        return

    with ui.pager:
        if api.long:
            table = Table(*WordPresenter.headers())
            for w in api.words:
                word = WordPresenter(w)
                table.add_row(*word.columns)
            ui.console.print(table)
        else:
            for word in api.words:
                ui.console.print(word)


dm_cmd = click.Command(
    "dm",
    callback=_, help=_.__doc__,
    epilog="Datamuse documentation: https://www.datamuse.com/api/",
    params=[
        *DatamuseOptions.cli_options,
        click.Option(["--json"], is_flag=True, help="Export as raw JSON."),
        click.Option(["--long"], is_flag=True, help="Print word list in long format."),
    ],
)
