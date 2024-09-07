"""CLI for words lookup command."""


from subprocess import run

import click
from more_itertools import always_iterable
from rich import box
from rich import print as rprint
from rich.table import Table

from words import bp, WordsError  # noqa
from words.web_references import REFERENCES


def validate_reference(ctx, param, value):
    """Validate web reference."""
    if value and value not in REFERENCES.keys():
        raise click.BadParameter("Invalid web reference. Try --list.")
    return value


def list_references():
    """Return a table listing all references."""
    table = Table(box=box.SIMPLE, show_header=False)
    for ref in REFERENCES._items:
        keys = always_iterable(getattr(ref, REFERENCES.key))
        table.add_row(*keys, ref.name)
    return table


def list_resources(ref):
    """Return a table listing all resources for a given reference."""
    table = Table(box=box.SIMPLE, show_header=False, title=f"{ref.name} Resources")
    for r in ref.resources._items:
        table.add_row(r.option, r.name)
    return table


@click.command("lookup")
@click.option(
    "-l", "--list",
    is_flag=True,
    help="List web reference or resources of a reference with --ref.",
)
@click.option(
    "-w", "--ref", "reference",
    callback=validate_reference,
    help="Web reference to search.",
)
@click.option(
    "-r", "--res", "resource",
    help="Resource to search.",
)
@click.argument("word", required=False)
def lookup_cmd(**kwargs):
    """Look up a word using a web resource."""
    name = kwargs.get("reference")
    ref = REFERENCES.get(name)

    if kwargs.get("list"):
        if ref:
            table = list_resources(ref)

        else:
            table = list_references()

        rprint(table)
        return

    word = kwargs.get("word")
    if not word:
        raise click.BadParameter("Missing argument: 'WORD'.")

    if not ref:
        raise click.BadParameter("Web reference (-w/--ref) required to look up a word.")

    s = kwargs.get("resource")

    if not s:
        raise click.BadParameter("Missing option: -r/--resource.")

    resource = ref.resources.get(s)
    url = resource.url(word)
    print(url)
    run(["open", url])
