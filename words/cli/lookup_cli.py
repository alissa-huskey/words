"""CLI for words lookup command."""


from subprocess import run

import click
from more_itertools import always_iterable
from rich import box
from rich import print as rprint
from rich.table import Table

from words import bp, WordsError  # noqa
from words.web_references import REFERENCES


@click.command("lookup")
@click.option(
    "-l", "--list",
    is_flag=True,
    help="List web reference or resources of a reference with --ref.",
)
@click.option(
    "-w", "--ref",
    help="Web reference to search.",
)
@click.option(
    "-r", "--res", "resource",
    help="Resource to search.",
)
@click.argument("word")
def lookup_cmd(**kwargs):
    """Look up a word using a web resource."""

    name = kwargs.get("ref")
    ref = REFERENCES.get(name)

    if kwargs.get("list"):

        table = Table(box=box.SIMPLE, show_header=False)

        # list the reference resources
        if ref:
            table.title = f"{ref.name} Resources"
            for r in ref.resources._items:
                table.add_row(r.option, r.name)
                ...

        # list references
        else:
            for ref in REFERENCES._items:
                keys = always_iterable(getattr(ref, REFERENCES.key))
                table.add_row(", ".join(keys), ref.name)

        rprint(table)
        return

    s = kwargs.get("resource")
    if not s:
        raise Exception("You must pass a resource.")
    word = kwargs.get("wordesource")
    if not s:
        raise Exception("You must pass a word.")

    resource = ref.resources.get(s)
    url = resource.url(kwargs.get("word"))
    print(url)
    run(["open", url])
