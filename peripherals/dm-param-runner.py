"""Generate words via the Datamuse API.

Script to run a set of words through the Datamuse API using all
flag/parameters.
"""

from sys import argv, exit

from datamuse import Datamuse
from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty
from rich.style import Style

PARAMS = (
    "ml",
    "sl",
    "sp",
    "rel_jja",
    "rel_jjb",
    "rel_syn",
    "rel_ant",
    "rel_trg",
    "rel_spc",
    "rel_gen",
    "rel_com",
    "rel_par",
    "rel_bga",
    "rel_bgb",
    "rel_hom",
    "rel_cns",
)

console = Console()


def main(*words):
    """Do the thing."""
    client = Datamuse()
    for word in words:
        for flag in PARAMS:
            kwargs = {"max": 20, flag: word}
            res = client.words(**kwargs)
            #  breakpoint()
            console.rule(f"[cyan]{word}", style=Style(color="cyan"))
            panel = Panel(Pretty(res), title=flag)
            console.print(panel)
            reply = input()
            if reply.strip().lower() == "q":
                exit()


if __name__ == "__main__":
    args = argv[1:]
    if not args:
        args = "wreak sample".split()
    main(*args)
