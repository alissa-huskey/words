import os

import pytest

from words import bp, WordsError  # noqa


@pytest.fixture(autouse=True)
def setup():
    os.environ["WORDS_PAGER"] = "NOPAGER"
    yield
