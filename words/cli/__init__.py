"""CLI module for words tool."""

from words import bp, WordsError  # noqa
from words.cli._ui import UI

__ALL__ = ["ui"]


ui = UI()
