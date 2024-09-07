"""CLI for words lookup command."""


from functools import partial
from subprocess import run

import click

from words import bp, WordsError  # noqa
from words.web_references import REFERENCES


@click.group("lookup")
def lookup_group(**kwargs):
    """Look up a word on a website."""


def cmd_maker(ref, **kwargs):
    """Look up a word using a web resource."""
    word = kwargs.get("word")
    if not word:
        raise click.BadParameter("Missing argument: 'WORD'.")

    if len(ref.resources._items) == 1:
        resource = ref.resources._items[0]
    else:
        search = kwargs.get("resource")
        resource = ref.resources.get(search)

    url = resource.url(word)
    print(url)
    run(["open", url])


for ref in REFERENCES._items:
    params = dict(
        callback=partial(cmd_maker, ref),
        short_help=f"{ref.options[0]} {ref.name}",
        help=ref.name,
        params=(
            [
                click.Option(
                    [f"--{r.option}", "resource"],
                    flag_value=r.option,
                    help=r.name
                )
                for r in ref.resources._items
                if len(ref.resources._items) > 1
            ] +
            [click.Argument(["word"])]
        )
    )

    lookup_group.add_command(click.Command(
        ref.options[1],
        **params
    ))

    lookup_group.add_command(click.Command(ref.options[0], hidden=True, **params))
