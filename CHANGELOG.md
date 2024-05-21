Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

[Unreleased]
------------

### Added

...

### Changed

#### Docs

- `README.md`: Update usage, add examples.
- Change project description in all relevant files.

#### CLI

- Better help command descriptions.
- `words syn`: Paginate output.

### Removed

...

[v0.3.0] - 2024-05-19
---------------------

> Features: `syn`, `dict define` and `rand word`.

### Added

#### CLI

- New command: `words syn` with options:
    - `--max`
    - `--json`
    - `--long`
    - `WORD`
- New subcommand: `words dict define` with options:
    - `--num`
    - `--db`
    - `WORD`
- New subcommand: `words rand word` with options:
    - `--num`
    - `--len`

#### Docs

- `resources.md`: add word lists links

#### Housekeeping

- Add names and colors lists to build files.
- Move extra build files to `assets/`.

### Changed

- Fix datamuse parts of speech parsing.

### Removed

- `words def` remove `--db` option, in favor of using default dbs.


[v0.2.0] - 2024-05-13
----------------------

> Features: `def`, `dict dbs`, `dict strageties`, `rand name`, `rand color`.

### Added

#### CLI

- New command: `words def` with options:
    - `--db`
    - `WORD`
- New command: `words dict`
  - New subcommand: `words dict dbs` with options:
    - `--search PHRASE`
    - `--default`
  - New subcommand: `words dict strageties`
- New options for command: `words dm`
    - `--sl`
    - `--sp`
    - `--rel-jja`
    - `--rel-jjb`
    - `--rel-syn`
    - `--rel-ant`
    - `--rel-trg`
    - `--rel-spc`
    - `--rel-gen`
    - `--rel-com`
    - `--rel-par`
    - `--rel-bga`
    - `--rel-bgb`
    - `--rel-hom`
    - `--rel-cns`
    - `--rel-cns`
    - `--ipa`
- New command: `words rand`
    - New subcommand: `words names` with options:
        - `-b, --male`
        - `-g, --girl`
        - `-l, --last`
        - `-f, --full`
        - `-n, --num`
        - `-m, --max`
    - New subcommand: `words rand color with options:`
        - `-s, --simple`
        - `-v, --verbose`
        - `-n, --num`
#### Docs

- Add `api.json` to keep track of the CLI api that I'm considering
- Add `api.md` for my CLI api brainstorming
- Add `dict.md` for notes about the dict.org API
- Add `pronunciation.md` for notes about pronunciation (for making sense of some of the Datamuse options.)
- Add `resources.md` for information about sources backing Datamuse and Dict.org, other APIs that could be useful, and other word-related tools.

#### Housekeeping

- Store build files in `dist/`.

### Changed

- `words` command moved to `dm` subcommand.


[v0.1.0] - 2024-04-21
----------------------

> Initial commit.

### Added

- `words` CLI tool -- Datamuse API wrapper.
    - `--ml` option
    - `--max` option
- docs: Copy of datamuse docs.

[v0.3.0]: https://github.com/alissa-huskey/words/compare/v0.2.0...v0.3.0
[v0.2.0]: https://github.com/alissa-huskey/words/compare/v0.1.0...v0.2.0
[v0.1.0]: https://github.com/alissa-huskey/words/tree/v0.1.0
[unreleased]: https://github.com/alissa-huskey/words/compare/v0.3.0...HEAD
