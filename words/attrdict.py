"""AttrDict module."""

from words.object import Object


class AttrDict(Object):
    """Object that equates subscription and attribute accessors."""

    def __repr__(self):
        """Return repr."""
        return repr(self.__dict__)

    def __getitem__(self, key):
        """Get an attribute via subscription."""
        return self.__dict__.__getitem__(key)

    def __setitem__(self, key, value):
        """Set an attribute via subscription."""
        return self.__dict__.__setitem__(key, value)
