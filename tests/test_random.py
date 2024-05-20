import pytest

from words import WordsError
from words.random import Random

from . import fixture_path

bp = breakpoint


def test_random():
    file = Random()

    assert file


def test_random_path():
    path = fixture_path("data/names.txt")
    file = Random(path)

    assert file.file == path


def test_random_lines_no_file():
    """
    GIVEN: A Random object with no file attr.
    WHEN: .lines is accessed
    THEN: an exception should be raised.
    """
    file = Random()
    with pytest.raises(WordsError):
        file.lines


def test_random_lines_file_missing():
    """
    GIVEN: A Random object with a file that does not exist.
    WHEN: .lines is accessed
    THEN: an exception should be raised.
    """
    file = Random("xxx.txt")
    with pytest.raises(WordsError):
        file.lines


def test_random_lines():
    """
    GIVEN: A Random object with a file that does exist.
    WHEN: .lines is accessed
    THEN: a list of lines should be returned.
    """
    path = fixture_path("names.txt")
    file = Random(path)
    lines = file.lines

    assert lines
    assert len(lines) == 10
    assert lines[0].split()[0] == "Mary"


def test_random_max():
    """
    GIVEN: A Random object where the max attr has been set.
    WHEN: self.lines is called
    THEN: only the lines up to max should be returned.
    """
    path = fixture_path("names.txt")
    file = Random(path, max=2)
    lines = file.lines

    assert lines
    assert len(lines) == 2


def test_random_get():
    """
    GIVEN: A Random object where the file exists
    WHEN: self.get() is called
    THEN: a random line shoud be returned
    """
    path = fixture_path("names.txt")
    file = Random(path)

    choices = file.get()

    assert choices
    assert len(choices) == 1
    assert choices[0] in file.lines


@pytest.mark.parametrize(["length_range", "pred", "message"], [
    ((0, 5), lambda line: len(line) <= 5, "less than or equal to 5"),
    ((10, 0), lambda line: len(line) >= 10, "greater than or equal to 10"),
    ((5, 8), lambda line: len(line) >= 5 and len(line) <= 8, "between 5 and 8"),
    (None, lambda line: True, "any length"),
])
def test_random_length_range(length_range, pred, message):
    """
    GIVEN: A Random object where the length_range attr has been set.
    WHEN: self.lines is called
    THEN: the length of all lines should be constrained appropriately
    """
    path = fixture_path("words.txt")
    file = Random(path, length_range=length_range)

    assert all(map(pred, file.lines)), f"all lines should be f{message}"


def test_random_():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
