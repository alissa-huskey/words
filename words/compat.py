"""Compatability."""

from words import bp, WordsError  # noqa

try:
    from bdb import BdbQuit
except ModuleNotFoundError:
    class BdbQuit(BaseException): ...   # noqa
