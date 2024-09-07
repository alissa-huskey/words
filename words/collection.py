from more_itertools import always_iterable

from words import bp, WordsError  # noqa
from words.object import Object


class Collection(Object):
    """Collection of items looked up by a given key."""

    def __init__(self, key=None, *args):
        """Create object."""
        self.key = key
        self._mapping = {}
        self._items = []
        self.add(*args)


    def add(self, *values):
        """Add value to collection."""
        for v in values:
            self._items.append(v)
            keys = always_iterable(getattr(v, self.key))

            for key in keys:
                self._mapping[key] = v

    def __getattr__(self, name):
        """Forward all missing methods to self._mapping."""
        return getattr(self._mapping, name)

    def __iter__(self):
        """Iterate over ._mapping.items()."""
        return iter(self._mapping.items())
