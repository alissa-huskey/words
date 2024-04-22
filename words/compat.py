"""Compatability."""

try:
    from bdb import BdbQuit
except ModuleNotFoundError:
    class BdbQuit(BaseException): ...
