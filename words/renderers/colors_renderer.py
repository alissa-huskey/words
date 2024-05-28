"""Render colors."""

from pathlib import Path

from rich.columns import Columns
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.style import Style
from rich.text import Text

from words import WordsError, bp  # noqa

ROOT_DIR = Path(__file__).parent.parent


class ColorsRenderer():
    """Render a list of colors."""

    def __init__(self, colors):
        """Create the object."""
        self.colors = colors

    def render(self, output_format):
        """."""
        self.colors.load()
        """Return a rendearable to print."""
        if output_format == "verbose":
            obj = self.render_verbose()
        elif output_format == "simple":
            obj = self.render_simple()
        else:
            raise WordsError(f"No such output format: {output_format}")
        return obj

    def render_verbose(self):
        """Return a renderable to print verbosely."""
        columns = Columns(padding=(2, 2))

        for color in self.colors.choose():
            swatch = Text("  ", Style(bgcolor=color.code))
            code = Text(color.code)
            code.align("center", self.colors.maxlen)
            group = Group(swatch, code)
            panel = Panel(group, title=color.name, width=self.colors.maxlen + 4)
            columns.add_renderable(panel)

        return Padding(columns, (1, 5))

    def render_simple(self):
        """Return a renderable to print simply."""
        colors = self.colors.choose()
        names = "\n".join([c.name for c in colors])
        panel = Panel(names, expand=False, title="Colors")
        return panel
