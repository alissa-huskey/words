"""UI Module."""

from functools import cached_property
from sys import stderr

from rich import print as rprint
from rich.console import Console, PagerContext

from words import WordsError, bp  # noqa
from words.cli.pager import get_pager
from words.object import Object


class UI(Object):
    """UI Class."""

    enable_pager: bool = True
    enable_debug_mode: bool = False

    _pager = None

    def err(self, message):
        """Print an error message and exit."""
        rprint(f"[red]Error[/red] {message}", file=stderr)
        exit(1)

    def debug(self, *text, **kwargs):
        """Print an debug message."""
        if not self.enable_debug_mode:
            return

        for k, v in kwargs.items():
            rprint(f"[yellow]{k}[/yellow]: {v!r}", file=stderr)

        if text:
            rprint("[yellow]>[/yellow]", *text, file=stderr)

    def header(self, title):
        """Print a section header."""
        self.console.rule(f"[bold green]{title}")

    @cached_property
    def pager_func(self):
        """Return the pager function for the pager context manager."""
        pager = get_pager(self)
        self.debug(pager=pager)
        return pager

    @cached_property
    def pager(self):
        """Return a pager context manager."""
        return PagerContext(self.console, self.pager_func, styles=True)

    @cached_property
    def console(self):
        """Return a rich console object."""
        return Console(stderr=True)
