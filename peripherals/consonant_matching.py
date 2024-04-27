"""Consonant matching.

Just trying to figure out what the hell "Consonant match" means.
"""

from re import compile as re_compile

from rich import print as rprint
from rich.table import Table

from peripherals.word import Word

VOWEL_PHENOMES = [
    "AA",
    "AE",
    "AH",
    "AO",
    "AW",
    "AX",
    "AXR",
    "AY",
    "EH",
    "ER",
    "EY",
    "IH",
    "IX",
    "IY",
    "OW",
    "OY",
    "UH",
    "UW",
    "UX",
]

PHENOME_STR = "|".join(VOWEL_PHENOMES)
PHEONME_FINDER = re_compile(rf'\b(({PHENOME_STR})\d?)\b')


class MyWord(Word):
    """."""

    @property
    def cons_pr(self):
        """Return pronunciation without vowels phenomes."""
        return PHEONME_FINDER.sub("-", self.prouns)


def hr():
    """Print a horizontal rule."""
    print("=" * 100)


examples = {
    "sample": ["simple"],
    "awake": ["awoke"],
    "beach": ["batch", "birch", "beech", "botch", "bouche"],
    "cow": ["key", "coy", "coo", "qi", "chi", "caw"],
    "slack": ["sleek", "slick", "slake", "slock"],
    "dessert": ["desert"],
    "sandy": ["sunday", "cindy", "sunder", "sander"],
    "late": ["lot", "let", "lit", "loot"],
    "car": ["care", "core", "coar", "khor"],
    "trunk": ["trank", "trink"],
}

table = Table("Word", "Pronunciation", "Only Consonants", "Size")
for w, matches in examples.items():
    word = MyWord(w)
    matches = {m: MyWord(m) for m in matches}
    matches = {m: w for m, w in matches.items() if w.prouns}
    cons = {w.cons_pr for w in matches.values()}
    cons.add(word.cons_pr)

    if len(cons) > 1:
        res = {m: MyWord(m).cons_pr for m in matches}
        breakpoint()

    row = [
        word.word,
        word.prouns,
        word.cons_pr,
        str(len(cons)),
    ]
    table.add_row(*row)

#  rprint(table)


examples = {
    "sample": ["simple"],
    "cow": ["key", "coo"],
    "late": ["lit", "loot"],
}

table = Table("Word", "Pronunciation", "Only Consonants")
for w, matches in examples.items():
    word = MyWord(w)

    table.add_row(
        word.word,
        word.prouns,
        word.cons_pr,
    )

    for m in matches:
        match = MyWord(m)
        table.add_row(match.word, match.prouns, match.cons_pr)

rprint(table)
