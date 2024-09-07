from collections import namedtuple

from words import bp, WordsError  # noqa
from words.collection import Collection

Thing = namedtuple("Thing", ("name", "value"))



def test_collection():
    """
    GIVEN: ...
    WHEN: ...
    THEN: ...
    """
    c = Collection()
    assert c


def test_collection_mapping():
    things = (Thing("a", 1), Thing("b", 2), Thing("c", 3))
    c = Collection("name", *things)
    assert list(c._mapping.values()) == list(things)


def test_collection_add():
    """
    GIVEN: a Collection object.
    WHEN: .add() is called.
    THEN: the item is added to the list of items.
    """
    a = Thing("a", 1)
    c = Collection("name")
    c.add(a)

    assert "a" in c._mapping
    assert c._mapping["a"] == a


def test_collection_add_multiple_keys():
    """
    GIVEN: a Collection object.
    AND: an item where the key contains multiple values.
    WHEN: .add() is called.
    THEN: the item is added to the list of items associated with all values.
    """
    a = Thing(("a", "b", "c"), 1)
    c = Collection("name")
    c.add(a)

    assert "a" in c._mapping
    assert "b" in c._mapping
    assert "c" in c._mapping
    assert c._mapping["a"] == a
    assert c._mapping["b"] == a
    assert c._mapping["c"] == a


def test_collection_get():
    """
    GIVEN: a Collection object.
    WHEN: .get() is called with a key.
    THEN: the item associated with that key is returned.
    """
    things = ((a := Thing("a", 1)), (b := Thing("b", 2)), (c := Thing("c", 3)))
    c = Collection("name", *things)
    assert c.get("b") == b


def test_collection_iter():
    """
    GIVEN: a Collection object with items.
    WHEN: it is iterated over.
    THEN: ._mapping.items() is iterated over.
    """
    c = Collection()
    c._mapping = {"a": 1, "b": 2, "c": 3}
    assert list(c) == [('a', 1), ('b', 2), ('c', 3)]
