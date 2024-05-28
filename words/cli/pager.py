"""Custom rich pager class."""

import os
import sys
from pydoc import pipepager, tempfilepager, ttypager
from shutil import which

from more_itertools import first
from rich.pager import SystemPager

from words import WordsError, bp  # noqa

__ALL__ = ["PAGERS", "get_pager"]


PAGERS = [
    "less -EFKR --exit-follow-on-close",
    "most",
    "more",
]


class RichPager(SystemPager):
    """Custom rich pager base class."""

    def __repr__(self):
        """Return repr string."""
        return f"{self.__class__.__name__}()"


class ProgramPager(RichPager):
    """Pager for a particular program.

    Use pydoc.pipepager() to run a particular program.

    Includes additional information attributes.
    """

    _cmd: str = None
    _prog: str = None

    def __init__(self, cmd):
        """Initialize the object.

        Args:
            cmd (str): pager command to run
        """
        self.cmd = cmd

    def __repr__(self):
        """Return repr string."""
        return f"Pager({self.cmd!r})"

    @property
    def cmd(self):
        """Get cmd."""
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        """Set cmd."""
        if not isinstance(value, str):
            raise TypeError(f"Pager() expects str not {type(value)}")
        self._cmd = value

    @property
    def prog(self):
        """Get prog."""
        if self._cmd and not self._prog:
            self._prog = self._cmd.split()[0]
        return self._prog

    def is_installed(self):
        """Return True if the pager program is installed."""
        return bool(which(self.prog))

    def _pager(self, text):
        """Page through text by feeding it to another program."""
        return pipepager(text, self.cmd)


class TtyPager(RichPager):
    """Pager based on pydoc.ttypager."""

    def _pager(self, text):
        """Manually page through text on a terminal."""
        return ttypager(text)


class TempfilePager(ProgramPager):
    """Pager based on pydoc.tempfilepager."""

    def _pager(self, text):
        """Page through text by invoking a program on a temporary file."""
        return tempfilepager(text, f"{self.cmd} <")


class NoPager(RichPager):
    """Pager that doesn't paginate."""

    def _pager(self, content):
        """Print text to stdout."""
        print(content, end="")


def pager_program() -> str:
    """Return the pager program to use including any CLI options.

    Searches for pagers in the PAGERS global variable plus the
    environment varialbes:

        - WORDS_PAGER
        - PAGER
        - MANPAGER

    Precedence order is: WORDS_PAGER, *PAGERS, PAGER, MANPAGER
    """
    # pagers set in environment variables
    pagers = [os.environ.get(v) for v in ("WORDS_PAGER", 'PAGER', 'MANPAGER')]
    pagers[1:1] = PAGERS.copy()

    prog = first(
        [ProgramPager(x) for x in pagers if x and ProgramPager(x).is_installed()],
        None
    )

    return (prog and prog.cmd or None)


def should_enable_pager(option, console) -> bool:
    """Return True if output should be viewed using a pager program."""
    # --no-pager
    env_pager = os.environ.get("WORDS_PAGER")
    if (option is False) or (env_pager == "NOPAGER"):
        return False

    # True: --pager or --pager=PROGRAM or in a terminal
    # False: --pager=None and not in a terminal
    return bool(option or console.is_terminal)


def get_pager(ui) -> RichPager:
    """Return a PagerContext object."""
    if not should_enable_pager(ui.enable_pager, ui.console):
        return NoPager()

    program = pager_program()

    if not program:
        return TtyPager()

    # pipes broken on windows apparently
    if sys.platform == 'win32':
        pager = TempfilePager(program)
    else:
        pager = ProgramPager(program)

    return pager
