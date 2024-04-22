Dict.org
========

* [Dict.org](https://dict.org/bin/Dict)
* [RFC 2229 Spec > A Dictionary Server Protocol](https://datatracker.ietf.org/doc/html/rfc2229)
* [Wikipedia > DICT](https://en.wikipedia.org/wiki/DICT)
* [Wayback Machine > Dict.org > Resources](https://web.archive.org/web/20200830164200/http://www.dict.org/links.html)
* [Dict.org Testing Server](dict://test.dict.org)
* [T-Shaped Journey > Search Dictionary From Command Line (Part 1)][tshaped-journey]
* [Struchu's blog > Enhance your writing with cURL](https://blog.strus.guru/2021/12/enhance-your-writing-with-curl/)

[tshaped-journey]: https://csonuryilmaz.github.io/curl/dict/2018/03/25/search-dictionary-from-command-line-(part1).html

Protocol
--------

### tl;dr

Query the `dict.org` using the following URL format using your browser or preferred network interface.

```
dict://dict.org/d:<word>
```

For example, here's a CLI request using curl.

```
curl -s dict://dict.org/d:pattern
```

You'll get a response back that looks something like this:

```
220 dict.dict.org dictd 1.12.1/rf on Linux 4.19.0-10-amd64 <auth.mime> <298169199.29919.1713730985@dict.dict.org>
250 ok
150 2 definitions retrieved
151 "Pattern" gcide "The Collaborative International Dictionary of English v.0.48"
Pattern \Pat"tern\, n. [OE. patron, F. patron, a patron, also, a
   pattern. See {Patron}.]
   1. Anything proposed for imitation; an archetype; an
      exemplar; that which is to be, or is worthy to be, copied
      or imitated; as, a pattern of a machine.
      [1913 Webster]

            I will be the pattern of all patience. --Shak.
      [1913 Webster]

   2. A part showing the figure or quality of the whole; a
      specimen; a sample; an example; an instance.
      [1913 Webster]

            He compares the pattern with the whole piece.
                                                  --Swift.
      [1913 Webster]

   3. Stuff sufficient for a garment; as, a dress pattern.
      [1913 Webster]

   4. Figure or style of decoration; design; as, wall paper of a
      beautiful pattern.
      [1913 Webster]

   5. Something made after a model; a copy. --Shak.
      [1913 Webster]

            The patterns of things in the heavens. --Heb. ix.
                                                  23.
      [1913 Webster]

   6. Anything cut or formed to serve as a guide to cutting or
      forming objects; as, a dressmaker's pattern.
      [1913 Webster]

   7. (Founding) A full-sized model around which a mold of sand
      is made, to receive the melted metal. It is usually made
      of wood and in several parts, so as to be removed from the
      mold without injuring it.
      [1913 Webster]

   8. a recognizable characteristic relationship or set of
      relationships between the members of any set of objects or
      actions, or the properties of the members; also, the set
      having a definable relationship between its members.
      [PJC]

   Note: Various collections of objects or markings are spoken
         of as a pattern. Thus: the distribution of bomb or
         shell impacts on a target area, or of bullet holes in a
         target; a set of traits or actions that appear to be
         consistent throughout the members of a group or over
         time within a group, as behavioral pattern, traffic
         pattern, dress pattern; the wave pattern for a spoken
         word; the pattern of intensities in a spectrum; a
         grammatical pattern.
         [PJC]

   9. (Gun.) A diagram showing the distribution of the pellets
      of a shotgun on a vertical target perpendicular to the
      plane of fire.
      [Webster 1913 Suppl.]

   10. the recommended flight path for an airplane to follow as
       it approaches an airport for a landing. Same as {landing
       pattern}.
       [PJC]

   11. an image or diagram containing lines, usually horizontal,
       vertical, and diagonal, sometimes of varying widths, used
       to test the resolution of an optical instrument or the
       accuracy of reproduction of image copying or transmission
       equipment. Same as {test pattern}.
       [PJC]

   {pattern box}, {pattern chain}, or {pattern cylinder} (Figure
      Weaving), devices, in a loom, for presenting several
      shuttles to the picker in the proper succession for
      forming the figure.

   {Pattern card}.
       (a) A set of samples on a card.
       (b) (Weaving) One of the perforated cards in a Jacquard
           apparatus.

   {Pattern reader}, one who arranges textile patterns.

   {Pattern wheel} (Horology), a count-wheel.
      [1913 Webster]
.
151 "Pattern" gcide "The Collaborative International Dictionary of English v.0.48"
Pattern \Pat"tern\, v. t. [imp. & p. p. {Patterned}; p. pr. &
   vb. n. {Patterning}.]
   1. To make or design (anything) by, from, or after, something
      that serves as a pattern; to copy; to model; to imitate.
      --Milton.
      [1913 Webster]

            [A temple] patterned from that which Adam reared in
            Paradise.                             --Sir T.
                                                  Herbert.
      [1913 Webster]

   2. To serve as an example for; also, to parallel.
      [1913 Webster]

   {To pattern after}, to imitate; to follow.
      [1913 Webster]
.
250 ok [d/m/c = 2/0/18; 0.000r 0.000u 0.000s]
221 bye [d/m/c = 0/0/0; 0.000r 0.000u 0.000s]
```

The beginning of each line tells you what kind of information you'll be getting.

* `150`: Number of results
* `151`: Beginning of a definition
* `.`: End of a definition
* `250`: End of results


### Top Level

* Requests are sent to a DICT server over the network using a particular format.
* Each request includes a command, and depending on the command, parameters.
* The server responds with text made up of a series of codes and data.
* These codes indicate success or failure and deliver the data that was requested.

#### URL Specification

```
dict://<user>;<auth>@<host>:<port>/<c>:<word>:<database>:<strategy>:<n>
```

| `*` | Field      | Meaning                             | Default |
|-----|------------|-------------------------------------|---------|
|     | `user`     | host username                       |         |
|     | `auth`     | host password (hashed)              |         |
| `*` | `host`     | host                                |         |
|     | `port`     | connection port                     | `2628`  |
| `*` | `c`        | command                             |         |
|     | `word`     |                                     |         |
|     | `database` |                                     | `!`     |
|     | `strat`    |                                     |         |
|     | `n`        | `nth` definition or match of a word | `.`     |

* `*`: Required

#### Parameters

Some request parameters can accept vaules with special meanings which can
(seemingly) be used with all commands that accept that parameter. These are
listed here.

| Parameter  | Value Name        | Symbol | Meaning                                                            |
|------------|-------------------|--------|--------------------------------------------------------------------|
| `DATABASE` | exclamation point | `!`    | search all and return all matches from the first matching database |
| `DATABASE` | star              | `*`    | search all databases and return all matches                        |
| `STRATEGY` | period            | `.`    | use the server-dependent default strategy                          |

#### Responses

##### Common

All responses start with a three digit code. An exhaustive list can be found
below in the [All Codes][] section, but the most common use is the `DEFINE` and
`MATCH` commands.


| Code | Meaning                                                       |
|------|---------------------------------------------------------------|
| 150  | `n` definitions retrieved - definitions follow                |
| 151  | word database name - text follows                             |
| 152  | `n` matches found - text follows                              |
| 220  | message header of things like server info and mime-type       |
| 221  | indicates the end of message                                  |
| 250  | ok (optional timing information here)                         |
| 550  | Invalid database, use "`SHOW DB`" for list of databases       |
| 551  | Invalid strategy, use "`SHOW STRAT`" for a list of strategies |
| 552  | No match                                                      |

###### Shared

Every `DICT`/`MATCH` response follows the following format.

* Line 1: `220` Header message -- server info.
* Line 2: `250` Ok message -- indicates that the request was received.
* Any number of lines: message body -- one or more lines of: `<Code> <Text>`
                      that contains either an error message or the data that
                      was requested.
* Last Line: `221` End of message.

It will look something like this:

```
220 <header message from server>
250 ok
<body>
221 bye
```

###### Failures

When the `DICT`/`MATCH` request failed, the response follows the same format as
above, but with a specific `<body>` format.

* Line 1: `220` Header message -- server info.
* Line 2: `250` Ok message -- indicates that the request was received.
* Line 3: `<Error Code> <Error Message>` -- indicates why it didn't work.
* Line 4: `221` End of message.

```
220 <header message from server>
250 ok
<Error Status> <Error Message>
221 bye
```

###### Successes

When the `DICT`/`MATCH` request succeeds, the response follows the same format as
above, but with a specific `<body>` format.

* Line 1: `220` Header message -- server info.
* Line 2: `250` Ok message -- indicates that the request was received.
* Any number of lines: message body -- one or more lines of: `<Code> <Text>`
                      that contains either the data that was requested.
* 2nd to Last Line:: `250` Ok message -- indicates that the request was successful.
* Last Line: `221` End of message.

```
220 <header message from server>
250 ok
<body>
221 bye
```

##### Global Codes

Responses start with a three digit code, listed below as `xyz` for each respective digit.

* `x`: Status, ie Success, Failure, Progress
* `y`: Broad category, ie Syntax, Connection, DICT
* `z`: Nature of this specific request

Response codes (`xyz`) are listed below grouped by status (`x`).

|     |                                                               |
|-----|---------------------------------------------------------------|
| 1## | Successful preliminary response                               |
| 110 | `n` databases present - text follows                          |
| 111 | `n` strategies available - text follows                       |
| 112 | database information follows                                  |
| 113 | help text follows                                             |
| 114 | server information follows                                    |
| 130 | challenge follows                                             |
| 150 | `n` definitions retrieved - definitions follow                |
| 151 | word database name - text follows                             |
| 152 | `n` matches found - text follows                              |
| 2## | Successfully received request                                 |
| 210 | (optional timing and statistical information here)            |
| 220 | text msg-id                                                   |
| 221 | Closing Connection                                            |
| 230 | Authentication successful                                     |
| 250 | ok (optional timing information here)                         |
| 3## | successful Intermediate response                              |
| 330 | send response                                                 |
| 4## | Failure in processing request, temporary                      |
| 420 | Server temporarily unavailable                                |
| 421 | Server shutting down at operator request                      |
| 5## | Failure in processing request, permanent                      |
| 500 | Syntax error, command not recognized                          |
| 501 | Syntax error, illegal parameters                              |
| 502 | Command not implemented                                       |
| 503 | Command parameter not implemented                             |
| 530 | Access denied                                                 |
| 531 | Access denied, use "SHOW INFO" for server information         |
| 532 | Access denied, unknown mechanism                              |
| 550 | Invalid database, use "`SHOW DB`" for list of databases       |
| 551 | Invalid strategy, use "`SHOW STRAT`" for a list of strategies |
| 552 | No match                                                      |
| 554 | No databases present                                          |
| 555 | No strategies available                                       |

The middle response code digit (`y`) values are listed below.

|     |                     |
|-----|---------------------|
| #0# | Syntax              |
| #1# | Information         |
| #2# | Connection          |
| #3# | Authentication      |
| #4# | Unspecified as yet  |
| #5# | DICT data           |
| #8# | Nonstandard/Private |

### Commands

Typical users will most likely only care about the `DEFINE` and `MATCH` commands, so those are the only ones documented in detail.

#### Summary

| Command    | Subcommand   | Shorthand | Args                           | Description                                                            |
|------------|--------------|-----------|--------------------------------|------------------------------------------------------------------------|
| `DEFINE`   |              | `D`       | `WORD`                         | look up `WORD` in the specified database                               |
| `MATCH`    |              | `M`       | `DATABASE` `STRATEGY` `WORD`   | search an index for for `WORD` using `STRATEGY`                        |
| `SHOW`     | `DATABASES`  | `DB`      |                                | list of currently accessible databases                                 |
| `SHOW`     | `STRATEGIES` | `STRAT`   |                                | list of currently supported search strategies                          |
| `SHOW`     | `INFO`       |           | `DATABASE`                     | source, copyright, and licensing information about a database          |
| `SHOW`     | `SERVER`     |           |                                | server information as written by administrator                         |
| `STATUS`   |              |           |                                | server-specific timing or debugging information                        |
| `QUIT`     |              |           |                                | exit the server                                                        |
| `OPTION`   |              |           | `MIME`                         | requested media header for response (Similar to http `Accept` header.) |
| `AUTH`     |              |           | `USERNAME` `SECRET`            | authenticate a client                                                  |
| `SASLAUTH` |              |           | `mechanism` `initial-response` | reserved for Simple Authentication and Security Layer (SASL) auth      |
| `SASLRESP` |              |           | `response`                     | reserved for Simple Authentication and Security Layer (SASL) auth      |

#### Text

* numeric status response line, using a 1yz code, will be sent indicating text will follow
* MIME header
* 2yz response code
* A single line containing only a period (decimal code 46, ".") indicates the end of the text

In this section I only care about 

```
<CODE>

```

#### DEFINE

```
dict://<host>/d:<word>:[<database>]:[<n>]
```

> NOTE: The redundant global URL fields have been ommitted.

| `*` | Field      | Meaning                             | Default |
|-----|------------|-------------------------------------|---------|
| `*` | `host`     | host                                |         |
| `*` | `/d`       | `DEFINE` command                    |         |
| `*` | `word`     | word to define                      |         |
|     | `database` | database to pull from               | `!`     |
|     | `n`        | `nth` definition or match of a word | `.`     |

* `*`: Required

##### Examples

###### Requests

```
dict://dict.org/d:shortcake:
dict://dict.org/d:shortcake:*
dict://dict.org/d:shortcake:wordnet:
dict://dict.org/d:shortcake:wordnet:1
dict://dict.org/d:abcdefgh
dict://dict.org/d:hot%20dog
dict://dict.org/d:sun
dict://dict.org/d:sun::1
```

###### Response Text

* `150`: number of matches found
* `151`: Start of definition in the format of:
* `.`: End of definition

```
151 `<WORD>` `<DATABASE>` `<DATABASE-DESCRIPTION>`
```

```
C: DEFINE ! penguin

S: 150 1 definitions found: list follows
S: 151 "penguin" wn "WordNet 1.5" : definition text follows
S: penguin
S:   1. n: short-legged flightless birds of cold southern esp. Antarctic
S:      regions having webbed feet and wings modified as flippers
S: .
S: 250 Command complete
```

```
C: DEFINE ! penguin

S: 150 1 definitions found: list follows
S: 151 "penguin" wn "WordNet 1.5" : definition text follows
S: penguin
S:   1. n: short-legged flightless birds of cold southern esp. Antarctic
S:      regions having webbed feet and wings modified as flippers
S: .
S: 250 Command complete
```

#### MATCH

```
dict://<host>>/m:<word>:<database>:<strat>:<n>
```

> NOTE: The redundant global URL fields have been ommitted.

| `*` | Field      | Meaning                             | Default |
|-----|------------|-------------------------------------|---------|
| `*` | `host`     | host                                |         |
| `*` | `/c`       | command                             |         |
|     | `word`     |                                     |         |
|     | `database` | database to pull from               | `!`     |
|     | `strat`    | what kind of search to run          |         |
|     | `n`        | `nth` definition or match of a word | `.`     |

* `*`: Required

##### Examples

###### Requests

```
dict://dict.org/m:sun
dict://dict.org/m:sun::soundex
dict://dict.org/m:sun:wordnet::1
dict://dict.org/m:sun::soundex:1
dict://dict.org/m:sun:::
```

###### Response Text

```
C: MATCH foldoc regex "s.si"

S: 152 7 matches found: list follows
S: foldoc Fast SCSI
S: foldoc SCSI
S: foldoc SCSI-1
S: foldoc SCSI-2
S: foldoc SCSI-3
S: foldoc Ultra-SCSI
S: foldoc Wide SCSI
S: .
S: 250 Command complete


C: MATCH wn substring "abcdefgh"

S: 552 No match
```

Python Dict Client
------------------

* [Github > jams2/py-dict-client](https://github.com/jams2/py-dict-client)
* [PyPi > py-dict-client](https://pypi.org/project/py-dict-client/)

```python
from dictionary_client import DictionaryClient as DictClient
client = DictClient("dict://test.dict.org")
client.define("hello")
```
