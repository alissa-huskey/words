"""Custom click ParamTypes."""

from click import ParamType

from words import bp, WordsError  # noqa
from words.cli import ui  # noqa


class RangeType(ParamType):
    """Custom click parameter type."""

    name = "[MIN]-[MAX]"

    def convert(self, value, param=None, ctx=None):
        """Convert from str to tuple(int, int) or None."""
        # for valid default values, pass straight through
        if isinstance(value, type(None)):
            return value
        elif (
            isinstance(value, tuple) and len(value) == 2 and
            all(map(lambda x: isinstance(x, int), value))
        ):
            return value

        try:
            if not isinstance(value, str):
                raise ValueError("non-default values must be type str")

            # split on dash and convert to int
            values = [x.strip() and int(x.strip()) or 0 for x in value.split("-")]

            if not value:
                raise ValueError("value cannot be an empty string")
            elif len(values) == 2:
                min_range, max_range = values
            elif len(values) == 1:
                min_range, max_range = 0, values[0]
            else:
                raise ValueError(
                    "when value is split on dash, "
                    "the result must have a length of 1 or 2"
                )

            if max_range and min_range > max_range:
                self.fail("MIN cannot be greater than MAX", param, ctx)

            return (min_range, max_range)

        except ValueError:
            message = (
                f"{value!r} is not valid. Valid formats are "
                f"MAX_INT, MIN_INT-, -MAX_INT or MIN_INT-MAX_INT"
            )
            self.fail(message, param, ctx)
