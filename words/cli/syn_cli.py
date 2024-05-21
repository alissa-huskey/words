"""CLI for words rand command group."""

import click
from rich.table import Table

from words.cli import console
from words.datamuse_api import DatamuseAPI
from words.definition_request import DefinitionRequest
from words.word import Word
from words.word_presenter import WordPresenter

bp = breakpoint


@click.command("syn")
@click.argument("word")
@click.option("--max", type=int, default=10, help="Max results.")
@click.option("--json", is_flag=True, help="Export as raw JSON.")
@click.option("--long", is_flag=True, help="Print word list in long format.")
def syn_cmd(word: str, max: int, json: bool, long: bool):
    """Synonyms."""
    synonyms = []

    # get synonyms from datamuse
    requests = [
        DatamuseAPI(ml=word, max=max, md="p"),
        DatamuseAPI(rel_syn=word, max=max, md="p"),
    ]

    for r in requests:
        r.get()
        synonyms += (r.words)

    # get synonyms from moby thesaurus
    rsp = DefinitionRequest(word, db="moby-thesaurus")
    rsp.lookup()
    if rsp.definitions:
        entry = rsp.definitions[0]
        _, _, text = entry.partition("\n")
        synonyms += ([Word(word=w.strip()) for w in text.split(",")])

    #  bp()

    done = []
    #  if long:
    table = Table(*WordPresenter.headers())
    for w in synonyms:
        if w.word in done:
            continue
        word = WordPresenter(w)
        table.add_row(*word.columns)
        done.append(w.word)

    with console.pager():
        console.print(table)
    #  else:
    #      for word in api.words:
    #          print(word)
