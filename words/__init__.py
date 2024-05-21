"""Words package."""

import os
from pathlib import Path

__ALL__ = ["WordsError", "bp"]


class WordsError(BaseException):
    """Words Exception."""


os.environ["NLTK_DATA"] = str(Path(__file__).parent.parent / "assets" / "nltk_data")

bp = breakpoint
