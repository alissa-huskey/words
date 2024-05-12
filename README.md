Words
=====

CLI tool to look up words using the [datamuse][datamuse] and [dict.org][dict] APIs.

[datamuse]: https://www.datamuse.com/api/
[dict]: http://dict.org

Usage
-----

```text
words -- Command line thesaurus, dictionary and more.

COMMANDS:
  def   Get the definition of a word.
  dict  Dict.org API commands.
  dm    Datamuse word search.
  rand  Print one or more random things.
```

For more detailed usage `words [COMMAND] --help`.

Examples
--------

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
╭─────────────────────── WordNet (r) 3.0 (2006) ────────────────────────╮
│ homophone                                                             │
│     n 1: two words are homophones if they are pronounced the same     │
│          way but differ in meaning or spelling or both (e.g. bare     │
│          and bear)                                                    │
╰───────────────────────────────────────────────────────────────────────╯
```

Status
------

**Pre-Alpha**

Unsuited for not-me users.

Install
-------

You really shouldn't. But if you insist.

```bash
git clone https://github.com/alissa-huskey/words.git && cd words
pip install dist/*.whl
command -v asdf > /dev/null && asdf reshim python
command -v pyenv > /dev/null && pyenv rehash
```

Credits
------------

* jams2/py-dict-client -- `dict://` client
* gmarmstrong/python-datamuse -- datamuse client

Alternatives
------------

* [datamuse-cli](https://pypi.org/project/datamuse-cli/) -- A very nice CLI to
  datamuse. If I had seen this earlier I wouldn't have written this.
