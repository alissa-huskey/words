"""CLI module for words tool."""

from pydoc import pipepager, plainpager
from shutil import which

from rich import print as rprint
from rich.console import Console, PagerContext
from rich.pager import SystemPager

__ALL__ = ["err", "header", "console", "pager"]

console = Console(stderr=True)


class PolitePager(SystemPager):
    """Return a well-behaved pager if possible."""

    def _pager(self, content: str):
        """Less based pager with sane options.

        -e, -E  --quit-at-eof  --QUIT-AT-EOF
        -F      --quit-if-one-screen
        -K      --quit-on-intr
        -r, -R  --raw-control-chars  --RAW-CONTROL-CHARS
        """
        try:
            if not console.is_terminal:
                return plainpager(content)
            if not which("less"):
                raise OSError("less command not found")
            pager = lambda text: pipepager(text, "less -EFKR")
            return pager(content)
        except (AttributeError, OSError):
            return super()._pager(content)


def err(message):
    """Print an error message and exit."""
    rprint(f"[red]Error[/red] {message}")
    exit(1)


def header(title):
    """Print a section header."""
    console.rule(f"[bold green]{title}")


pager = PagerContext(console, PolitePager(), styles=True)
