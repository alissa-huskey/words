"""Words CLI tool."""

import click
from rich.traceback import install as rich_tracebacks

from words import WordsError
from words.cli import err
from words.cli.def_cli import def_cmd
from words.cli.dict_cli import dict_group
from words.cli.dm_cli import dm_cmd
from words.cli.rand_cli import rand_group
from words.cli.syn_cli import syn_cmd
from words.compat import BdbQuit

rich_tracebacks(show_locals=True, suppress=[click])
bp = breakpoint


@click.group()
def run():
    """Command line thesaurus, dictionary and more."""
    pass


run.add_command(rand_group)
run.add_command(def_cmd)
run.add_command(dict_group)
run.add_command(dm_cmd)
run.add_command(syn_cmd)


def main():
    """CLI entrypoint."""
    try:
        run()
    except (SystemExit, BdbQuit):
        ...
    except WordsError as e:
        err(e)
