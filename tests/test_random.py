from pathlib import Path

import pytest

from words import bp, WordsError  # noqa
from words.random import Random, RandomBooks, RandomParagraph, RandomProse

from . import fixture_path


@pytest.fixture
def text():
    """Return a block of text."""

    text = """
        He walked nearer than a hundred paces to it, and yet he did not become
        fixed as before, but found that he could go quite close up to the door.
        Jorindel was very glad indeed to see this. Then he touched the door with
        the flower, and it sprang open; so that he went in through the court,
        and listened when he heard so many birds singing. At last he came to the
        chamber where the fairy sat, with the seven hundred birds singing in
        the seven hundred cages. When she saw Jorindel she was very angry, and
        screamed with rage; but she could not come within two yards of him, for
        the flower he held in his hand was his safeguard. He looked around at
        the birds, but alas! there were many, many nightingales, and how then
        should he find out which was his Jorinda? While he was thinking what to
        do, he saw the fairy had taken down one of the cages, and was making the
        best of her way off through the door. He ran or flew after her, touched
        the cage with the flower, and Jorinda stood before him, and threw her
        arms round his neck looking as beautiful as ever, as beautiful as when
        they walked together in the wood.
    """

    return text


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


def test_random_books():
    """
    WHEN: a RandomBooks() object is created
    THEN: it should work
    """

    books = RandomBooks()
    assert books


def test_random_books_files():
    """
    GIVEN: a RandomBooks() object
    WHEN: .files is accessed
    THEN: it should return a list of files
    """

    books = RandomBooks()
    files = books.files

    assert files


def test_random_books_get():
    """
    GIVEN: a RandomBooks() object
    WHEN: .get is accessed
    THEN: it should return a list of files
    AND: it should be the same size as count
    """

    books = RandomBooks()
    files = books.get(2)

    assert files
    assert len(files) == 2


def test_random_prose():
    """
    WHEN: a RandomProse object is created.
    THEN: it should work
    """
    prose = RandomProse()
    assert prose


def test_random_prose_file():
    """
    WHEN: a RandomProse object is created with a path.
    THEN: it should work
    """
    root = Path(__file__).parent.parent / "assets" / "prose"
    file = root / "dracula.txt"

    prose = RandomProse(file)

    assert prose.file == file


def test_random_prose_title():
    """
    GIVEN: a RandomProse with a file
    WHEN: .title is accessed
    THEN: it should return a title based on the filename
    """
    root = Path(__file__).parent.parent / "assets" / "prose"
    file = root / "a-christmas-carol.txt"

    prose = RandomProse(file)

    assert prose.title == "A Christmas Carol"


def test_random_prose_text():
    """
    GIVEN: a RandomProse with a file
    WHEN: .text is accessed
    THEN: it should return the contents of the file
    """
    root = Path(__file__).parent.parent / "assets" / "prose"
    file = root / "winnie-the-pooh.txt"

    prose = RandomProse(file)
    text = prose.text

    assert len(text) == 119749
    assert text.startswith("Here is Edward Bear, coming downstairs")


def test_random_prose_paragraphs():
    """
    GIVEN: a RandomProse with a file
    WHEN: .paragraphs is accessed
    THEN: it should return a list of paragraphs
    """
    root = Path(__file__).parent.parent / "assets" / "prose"
    file = root / "winnie-the-pooh.txt"

    prose = RandomProse(file)
    paras = prose.paragraphs

    assert len(paras) == 1054
    assert len(paras[0]) == 421
    assert paras[0].startswith("Here is Edward Bear, coming downstairs")


def test_random_prose_get():
    """
    GIVEN: a RandomProse with a file
    WHEN: .get() is called
    THEN: it should return a list of randomly chosen paragraphs
    """
    root = Path(__file__).parent.parent / "assets" / "prose"
    file = root / "winnie-the-pooh.txt"

    prose = RandomProse(file)
    paras = prose.get(5)

    assert len(paras) == 5


def test_random_paragraph():
    """
    WHEN: a RandomParagraph object is created
    THEN: it should work
    """
    p = RandomParagraph()
    assert p


def test_random_paragraph_text(text):
    """
    WHEN: a RandomParagraph object is created with text
    THEN: .text should contain the text
    AND: the excess mid-text whitespace should be stripped
    """
    p = RandomParagraph(text)
    t = p.text

    assert t
    assert len(t.splitlines()) == 1
    assert "become fixed" in t
    assert t.startswith("He walked nearer")
    assert t.endswith("together in the wood.")


def test_random_paragraph_sentences(text):
    """
    GIVEN: a RandomParagraph object is created with text
    WHEN: .sentences is accessed
    THEN: a list of sentences should be returned
    """
    p = RandomParagraph(text)
    sents = p.sentences

    assert sents


def test_random_paragraph_get(text):
    """
    GIVEN: a RandomParagraph object is created with text
    WHEN: .get() is called
    THEN: a randomly selected list of sentences should be returned
    """
    p = RandomParagraph(text)
    sents = p.get(2)

    assert sents
    assert len(sents) == 2


def test_random_():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
