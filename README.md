Words
=====

> Command line thesaurus, dictionary and more.

Uses the [datamuse][datamuse] and [dict.org][dict] APIs.

[datamuse]: https://www.datamuse.com/api/
[dict]: http://dict.org

Status
------

**Pre-Alpha**

A personal project with limited QA and questionable stability.

Not-me users, beware.

Usage
-----

    Usage: words [OPTIONS] COMMAND [ARGS]...

      Command line thesaurus, dictionary and more.

    Options:
      --help  Show this message and exit.

    Commands:
      def   Definition lookup.
      dict  Dict.org API wrapper.
      dm    Datamuse API wrapper.
      rand  Random data.
      syn   Synonyms.

For more detailed usage `words [COMMAND] --help`.

Examples
--------

### Definition

``` text
$ words def homophone
╭──── The Collaborative International Dictionary of English v.0.48 ─────╮
│ Homophone \Hom"o*phone\, n. [Cf. F. homophone. See                    │
│    {Homophonous}.]                                                    │
│    1. A letter or character which expresses a like sound with         │
│       another. --Gliddon.                                             │
│       [1913 Webster]                                                  │
│                                                                       │
│    2. A word having the same sound as another, but differing          │
│       from it in meaning and usually in spelling; as, all and         │
│       awl; bare and bear; rite, write, right, and wright.             │
│       Homophonic                                                      │
╰───────────────────────────────────────────────────────────────────────╯
```

### Synonyms

``` text
$ words syn undergrad
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Parts   ┃ Word           ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ adj, n  │ undergraduate  │
│ n       │ postgrad       │
│ n       │ grad           │
│ n       │ college        │
│ n       │ profs          │
│ n       │ university     │
│ n       │ prof           │
│ n       │ undergraduates │
│ n, prop │ biochem        │
│ adj     │ premed         │
└─────────┴────────────────┘
```

### Random Data

``` bash
$ words rand name --girl --num 5
╭─ Girl Names ─╮
│ Vivien       │
│ Ileen        │
│ Ashton       │
│ Kellie       │
│ Fe           │
╰──────────────╯
```

``` bash
$ words rand word --num 5 --len 5-8
╭─ words ─╮
│ graph   │
│ bound   │
│ labor   │
│ flying  │
│ incline │
╰─────────╯
```

``` bash
$ words rand color --num 4 --verbose

  ╭─ Goldenrod ──╮  ╭─── Blush ────╮
  │              │  │              │
  │   #FCD667    │  │   #B44668    │
  ╰──────────────╯  ╰──────────────╯


  ╭─ Blackberry ─╮  ╭─── Copper ───╮
  │              │  │              │
  │   #4D0135    │  │   #B87333    │
  ╰──────────────╯  ╰──────────────╯
```

### Datamuse API Wrapper

``` bash
$ words dm --ml homage --max 5
court
honor
honoured
respect
appreciation
```

``` bash
$ words dm --rel-hom night
knight
nite
```

### Dict.org API Wrapper

```text
$ words dict define --db elements silver
╭─────────────────────── The Elements (07Nov00) ────────────────────────╮
│ silver                                                                │
│ Symbol: Ag                                                            │
│ Atomic number: 47                                                     │
│ Atomic weight: 107.870                                                │
│ White lustrous soft metallic transition element. Found in both its    │
│ elemental form and in minerals. Used in jewelry, tableware and so on. │
│ Less reactive than silver, chemically.                                │
│                                                                       │
╰───────────────────────────────────────────────────────────────────────╯
```

Install
-------

You probably shouldn't. But if you insist.

```bash
git clone https://github.com/alissa-huskey/words.git && cd words
pip install dist/*.whl
command -v asdf > /dev/null && asdf reshim python
command -v pyenv > /dev/null && pyenv rehash
```

Credits
-------

* jams2/py-dict-client -- `dict://` client
* gmarmstrong/python-datamuse -- datamuse client

Alternatives
------------

* [datamuse-cli](https://pypi.org/project/datamuse-cli/) -- A very nice CLI to
  datamuse. If I had seen this earlier I wouldn't have written this.
