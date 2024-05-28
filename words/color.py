"""Random colors."""

import json
from pathlib import Path
from random import choices

from words import bp, WordsError  # noqa
from words.object import Object

ROOT_DIR = Path(__file__).parent.parent


class Color(Object):
    """A color name and hex code."""

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
        """Get hex code."""
        return self._code and ("#" + self._code.lstrip("#")) or self._code

    @code.setter
    def code(self, value):
        """Set hex code."""
        self._code = value


class Colors(dict):
    """Mapping of color names -> Color objects."""

    DATADIR = ROOT_DIR / "assets" / "colors"

    data = {}
    _maxlen = 0

    def __init__(self, num=1, *args, **kwargs):
        """Create the object."""
        self.num = num

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
        if not self:
            return []
        return choices(list(self.values()), k=self.num)
