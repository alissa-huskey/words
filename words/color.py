"""Printing colors."""

import json
from pathlib import Path
from random import choices

from rich.columns import Columns
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.style import Style
from rich.text import Text

from words import WordsError
from words.object import Object

bp = breakpoint
ROOT_DIR = Path(__file__).parent.parent


class Color(Object):
    """A color."""

    _name = None
    _code = None

    def __init__(self, name=None, code=None):
        """Create the object."""
        self.name = name
        self.code = code

    @property
    def name(self):
        """Get name."""
        return self._name and self._name.title() or self.name

    @name.setter
    def name(self, value):
        """Set name."""
        self._name = value

    @property
    def code(self):
        """Get code."""
        return self._code and ("#" + self._code.lstrip("#")) or self._code

    @code.setter
    def code(self, value):
        """Set code."""
        self._code = value


class Colors(dict):
    """Mapping of color names -> Color objects."""

    DATADIR = ROOT_DIR / "assets" / "colors"

    data = {}
    _maxlen = 0

    def __init__(self, output_format=None, num=1, *args, **kwargs):
        """Create the object."""
        self.num = num
        self.output_format = output_format

        if not args:
            return

        super().__init__(*args, **kwargs)

    @property
    def path(self):
        """Path to the colors json."""
        return self.DATADIR / "simple-colors.json"

    def load(self):
        """Load the data from the json file."""
        with self.path.open() as fp:
            data = json.load(fp)
            mapping = {k: Color(k, v) for k, v in data.items()}
            self.update(mapping)

    @property
    def maxlen(self):
        """Return the length of the longest name."""
        if self._maxlen:
            return self._maxlen

        if not self:
            return 0

        return max(map(len, self))

    def choose(self):
        """Return one or more random colors."""
        return choices(list(self.values()), k=self.num)

    def render(self):
        """."""
        self.load()
        if self.output_format == "verbose":
            obj = self.render_verbose()
        elif self.output_format == "simple":
            obj = self.render_simple()
        else:
            raise WordsError(f"No such output format: {self.output_format}")
        return obj

    def render_verbose(self):
        """Return a renderable to print."""
        columns = Columns(padding=(2, 2))

        for color in self.choose():
            swatch = Text("  ", Style(bgcolor=color.code))
            code = Text(color.code)
            code.align("center", self.maxlen)
            group = Group(swatch, code)
            panel = Panel(group, title=color.name, width=self.maxlen + 4)
            columns.add_renderable(panel)

        return Padding(columns, (1, 5))

    def render_simple(self):
        """Return a renderable to print."""
        colors = self.choose()
        names = "\n".join([c.name for c in colors])
        panel = Panel(names, expand=False, title="Colors")
        return panel
