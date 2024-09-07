"""The web reference module."""

from words import bp, WordsError  # noqa
from words.collection import Collection
from words.object import Object


class WebReference(Object):
    """A website that can be used to look up words."""

    def __init__(self, **kwargs):
        """Create object."""
        self.resources = Collection("option", *kwargs.pop("resources", []))
        super().__init__(**kwargs)
