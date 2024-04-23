import pytest

from words.response_status import ResponseStatus


def test_response_status():
    assert ResponseStatus()


def test_response_status_args():
    status = ResponseStatus(200, "ok")
    assert status.code == 200
    assert status.message == "ok"


def test_response_status_str_code():
    status = ResponseStatus("200")
    assert status.code == 200


@pytest.mark.parametrize(("code",), [("batty",), ("1234",)])
def test_response_status_bad_code(code):
    """
    WHEN: an invalid code is assigned to status.code
    THEN: status.code should be None
    """
    status = ResponseStatus()
    with pytest.raises(ValueError):
        status.code = code


def test_response_status_strip_message():
    status = ResponseStatus("200", "ok ")
    assert status.message == "ok"


@pytest.mark.parametrize(("line", "code", "message"), [
    ("550 invalid database, use SHOW DB for list",
     550, "invalid database, use SHOW DB for list"),
    ("   maan, OS. & OHG. m[=a]no, G. mond, Icel. m[=a]ni, Dan. maane,",
     None, None),
    (r"Moon \Moon\, v. i.", None, None),
    (r"250 ok [d/m/c = 6/0/148; 0.000r 0.000u 0.000s]", 250, "ok"),
])
def test_response_status_parse(line, code, message):
    """
    WHEN: a response line is parsed via status.parse()
    THEN: it should assign status.code and status.message correctly
    """
    status = ResponseStatus()
    status.parse(line)
    assert status.code == code
    assert status.message == message


@pytest.mark.parametrize(("line", "code", "message"), [
    ("550 invalid database, use SHOW DB for list",
     550, "invalid database, use SHOW DB for list"),
])
def test_response_status_parse_line(line, code, message):
    status = ResponseStatus(line)
    assert status.code == code
    assert status.message == message
