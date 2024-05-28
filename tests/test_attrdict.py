from words import bp, WordsError  # noqa
from words.attrdict import AttrDict


def test_attrdict():
    assert AttrDict()


def test_attrdict_init_attrs():
    obj = AttrDict(a=1)

    assert obj.a == 1
    assert obj["a"] == 1


def test_attrdict_set_attrs():
    obj = AttrDict()
    obj.a = 1

    assert obj["a"] == 1


def test_attrdict_set_subscript():
    obj = AttrDict()
    obj["a"] = 1

    assert obj.a == 1
