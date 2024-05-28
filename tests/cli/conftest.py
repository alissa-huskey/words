import os

import pytest

from words import WordsError, bp  # noqa


@pytest.fixture(autouse=True)
def setup():
    os.environ["WORDS_PAGER"] = "NOPAGER"
    yield
