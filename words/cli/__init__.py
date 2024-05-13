"""CLI module for words tool."""

from rich import print as rprint
from rich.console import Console

console = Console(stderr=True)


def err(message):
    """Print an error message and exit."""
    rprint(f"[red]Error[/red] {message}")
    exit(1)


def header(title):
    """Print a section header."""
    console.rule(f"[bold green]{title}")
