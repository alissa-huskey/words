"""Words CLI tool."""

import click
from rich.traceback import install as rich_tracebacks

from words import bp, WordsError  # noqa
from words.cli import ui
from words.cli.def_cli import def_cmd
from words.cli.dict_cli import dict_group
from words.cli.dm_cli import dm_cmd
from words.cli.lookup_cli import lookup_group
from words.cli.rand_cli import rand_group
from words.cli.syn_cli import syn_cmd
from words.cli.wordnik_cli import wordnik_group
from words.compat import BdbQuit

rich_tracebacks(show_locals=True, suppress=[click])


SETTINGS = dict(
    help_option_names=['-h', '--help'],
    show_default=True,
)


@click.group(context_settings=SETTINGS)
@click.option(
    "-D", "--debug", "enable_debug_mode",
    type=bool, is_flag=True, default=False,
    help="Print debug messages.",
)
@click.option(
    "-p/-P", "--pager/--no-pager", "enable_pager", show_default="True",
    type=bool, is_flag=True, default=None,
    help="Enable pager.",
)
def run(enable_debug_mode: bool, enable_pager: bool):
    """Command line thesaurus, dictionary and more."""
    ui.enable_debug_mode = enable_debug_mode
    ui.enable_pager = enable_pager


run.add_command(def_cmd)
run.add_command(dict_group)
run.add_command(dm_cmd)
run.add_command(lookup_group)
run.add_command(rand_group)
run.add_command(syn_cmd)
run.add_command(wordnik_group)


def main():
    """CLI entrypoint."""
    try:
        run(auto_envvar_prefix="WORDS")
    except (SystemExit, BdbQuit):
        ...
    except WordsError as e:
        ui.err(e)
