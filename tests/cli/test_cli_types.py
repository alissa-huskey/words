import pytest
from click import BadParameter

from words import bp, WordsError  # noqa
from words.cli.param_types import RangeType


@pytest.mark.parametrize(["input_value", "expected", "input_msg", "output_msg"], [
    ("10", (0, 10), "INT", "0,MAX_INT"),
    ("-10", (0, 10), "-INT", "0,MAX_INT"),
    ("10-", (10, 0), "-INT", "MAX_INT,0"),
    ("5-10", (5, 10), "INT-INT", "MAX_INT,MIN_INT"),
    (None, None, None, None),
    ((0, 10), (0, 10), "tuple(INT, INT)", "MIN_INT,MAX_INT"),
])
def test_cli_types_range(input_value, expected, input_msg, output_msg):
    """
    GIVEN: a RangeType
    WHEN: .convert() is called with a valid input value
    THEN: the correct output value should be returned
    """
    output_value = RangeType().convert(input_value)

    assert output_value == expected, \
        f"When input value is {input_msg!r} output value should be {output_msg!r}."

    assert isinstance(output_value, type(expected)), (
        f"When input value is {input_msg!r} output value "
        f"should be type {type(output_value)}."
    )


@pytest.mark.parametrize(["input_value"], [
    [""], ["xxx"], ["xxx-1"], ["1-xxx"], ["1-2-3"], ["10-5"],
    [(1, 2, 3)], [("1", 2)], [{}], [10],
])
def test_cli_types_range_invalid(input_value):



    """
    GIVEN: a RangeType
    WHEN: .convert() is called with an invalid input value
    THEN: the correct output value should be returned
    """

    with pytest.raises(BadParameter):
        RangeType().convert(input_value)
