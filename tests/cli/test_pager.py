import os

import pytest

from words import WordsError, bp  # noqa
from words.cli import pager as pager_module
from words.cli.pager import (ProgramPager, get_pager, pager_program,
                             should_enable_pager)

from .. import Stub


@pytest.fixture
def clear_pager_vars():
    for var in ("WORDS_PAGER", "PAGER", "MANPAGER"):
        pager_module.os.environ.pop(var, None)


class Params(Stub):
    """Parameterization class with defaults."""

    console = Stub(is_terminal=True)
    pager = ""


@pytest.mark.parametrize(("params",), [
    [Params(option=False, expected=False, desc="--no-pager is passed")],
    [Params(option=True, expected=True, desc="--pager is passed")],
    [Params(
        option=None, console=Stub(is_terminal=True), expected=True,
        desc="no pager option exists and output goes to a terminal"
    )],
    [Params(option="ov", expected=True, desc="--pager=PROGRAM is passed")],
    [Params(
        option=None, console=Stub(is_terminal=False), expected=False,
        desc="no pager option exists and output does not go to a terminal"
    )],
    [Params(
        pager="NOPAGER", option=None, expected=False,
        desc="no pager option exists and WORDS_PAGER is set to 'NOPAGER'"
    )]
])
def test_should_enable_pager(params):
    os.environ["WORDS_PAGER"] = params.pager
    assert should_enable_pager(params.option, params.console) == params.expected, \
        f"When {params.desc}, should_enable_pager() should return {params.expected}"


@pytest.mark.parametrize(("cmd", "installed", "expected"), [
    ("ov", ["less"], Stub(prog="ov", cmd="ov", installed=False)),
    ("ov -FX", ["ov"], Stub(prog="ov", cmd="ov -FX", installed=True)),
])
def test_pager_pager(monkeypatch, cmd, installed, expected):
    """
    WHEN: A ProgramPager object is created with a command string (like: "less -R")
    THEN: .prog should return the first word of the string
    AND: .cmd should return the whole string
    AND: .is_installed() should return True the program is installed
    """

    # tell which how to answer about what programs are installed
    monkeypatch.setattr(pager_module, "which", lambda x: x in installed)

    p = ProgramPager(cmd)
    assert p.prog == expected.prog
    assert p.cmd == expected.cmd
    assert p.is_installed() is expected.installed


@pytest.mark.parametrize(
    ("env", "defaults", "installed", "expected", "desc"),
    [
        (
            {}, ["less"], ["less"], "less",
            (
                "a program from the default pagers list is installed"
                "it should be returned"
            )
        ),
        (
            {"WORDS_PAGER": "less"}, ["less -R"], ["less"], "less",
            "the program from WORDS_PAGER env var is installed, it should be returned"
        ),
        (
            {"WORDS_PAGER": "ov", "PAGER": "less"}, [], ["less"], "less",
            (
                "the program from WORDS_PAGER is not installed "
                "and the program from PAGER is installed, "
                "the PAGER value should be returned"
            )
        ),
        (
            {"WORDS_PAGER": "ov", "PAGER": "less"}, [], ["ov", "less"], "ov",
            (
                "the programs from WORDS_PAGER and PAGER are installed "
                "the WORDS_PAGER value should be returned"
            )
        ),
        (
            {}, ["less -R"], ["less"], "less -R",
            (
                "the default pager is installed and includes options, "
                "it should be correctly returned"
            )
        ),
        (
            {"WORDS_PAGER": "less"}, ["less -R"], ["less"], "less",
            (
                "the default pager includes options "
                "and the environment variable has the same pager "
                "but with different (or no) options "
                "and they are both installed, "
                "the pager from the environment variable should be returned"
            )
        ),
        (
            {"PAGER": "bat"}, ["less"], ["bat", "less"], "less",
            (
                "the default pager is installed "
                "and so is one of the PAGER/MANPAGER values, "
                "the default pager should take precedence"
            )
        ),
        (
            {"PAGER": "less"}, ["bat"], ["less"], "less",
            (
                "the default pager is not installed "
                "and one of the PAGER/MANPAGER values is installed, "
                "the fallback env var value should be returned"
            )
        ),
    ]
)
def test_pager_program(
    monkeypatch, clear_pager_vars, env, defaults, installed, expected, desc
):
    """
    GIVEN: pagers.PAGERS is set to a list of pager commands
    AND: the environment variables WORDS_PAGER, PAGER and MAN_PAGER have various values
    AND: certain pagers are installed
    WHEN: pager_program() is called
    THEN: it should return the first command from the environment variables,
          then the list of default pager commands that is installed
    """

    # set the default list of pagers
    monkeypatch.setattr(pager_module, "PAGERS", defaults)

    # set the pager-related environment variables
    pager_module.os.environ.update(env)

    # tell which how to answer about what programs are installed
    monkeypatch.setattr(pager_module, "which", lambda x: x in installed)

    program = pager_program()

    assert program == expected, (
        f"When {desc}."
    )


class Params(Stub):
    """Parameterization data defaults."""

    enabled: bool = True
    program: str = None
    platform: str = "darwin"
    attrs: dict = {}


@pytest.mark.parametrize(["params"], [
    [Params(enabled=False, klass="NoPager")],
    [Params(program="", klass="TtyPager")],
    [Params(
        program="more",
        platform="win32",
        klass="TempfilePager",
        attrs=dict(cmd="more")
    )],
    [Params(program="ov -FX", klass="ProgramPager")]
])
def test_get_pager(monkeypatch, params):
    """
    GIVEN: should_enable_pager() returns True or False
    AND: pager_program() returns a string or None
    AND: sys.platform contains a string
    WHEN: get_pager() is called
    THEN: the correct pager object should be returned
    """

    monkeypatch.setattr(pager_module, "should_enable_pager", lambda *x: params.enabled)
    monkeypatch.setattr(pager_module, "pager_program", lambda: params.program)
    monkeypatch.setattr(pager_module.sys, "platform", params.platform)

    pager = get_pager(Stub(enable_pager=None, console=None))

    assert pager.__class__.__name__ == params.klass

    for attr, value in params.attrs.items():
        assert getattr(pager, attr) == value
