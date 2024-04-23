"""The words test module."""

from pathlib import Path

DATADIR = Path(__file__).parent / "data"


class Stub():
    """Arbitrary stub class."""

    def __init__(self, **kwargs):
        """Make the object and set all kwargs as attrs."""
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        """Return a nice looking repr string."""
        attrs = ", ".join([f"{k}={v!r}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({attrs})"


def fixture_path(name) -> Path:
    """Return the path to a file in the tests/data directory."""
    return DATADIR / name


def read_file(path, mode="rb"):
    """Read a file and return its contents."""
    if isinstance(path, str):
        path = fixture_path(path)

    with path.open(mode) as fp:
        contents = fp.read()

    return contents
