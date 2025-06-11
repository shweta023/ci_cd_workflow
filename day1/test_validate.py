# tests/test_validate.py

import re
import io
import sys
from loginValidator import validate
import pytest
 # adjust import to match your project structure

# Capture stdout helper
class CapturePrints:
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        return self
    def __exit__(self, *args):
        self.output = self._stringio.getvalue()
        sys.stdout = self._stdout

@pytest.mark.parametrize("username,should_be_valid", [
    ("AliceA", True),      # 6 letters
    ("abcde", True),       # exactly 5 letters
    ("abcdefghij", True),  # exactly 10 letters
    ("abcd", False),       # too short
    ("abcdefghijk", False),# too long
    ("User1", False),      # contains digit
    ("user_name", False),  # contains underscore
])
def test_username_validation(username, should_be_valid):
    with CapturePrints() as cap:
        validate(userName=username)
    if should_be_valid:
        assert f"UserName{username} is valid" in cap.output
    else:
        assert cap.output == ""

@pytest.mark.parametrize("password,should_be_valid", [
    ("Password1", True),       # uppercase + digit, length ≥8
    ("ABCdef12", True),        # mixed-case + digits
    ("short1A", False),        # too short
    ("nouppercase1", False),   # no uppercase letter
    ("NOLOWERCASE1", False),   # no lowercase letter
    ("NoDigitsHere", False),   # no digit
    ("P4ssw rd", False),       # contains space
])
def test_password_validation(password, should_be_valid):
    with CapturePrints() as cap:
        validate(password=password)
    if should_be_valid:
        assert f"Password{password} is valid" in cap.output
    else:
        assert cap.output == ""

def test_both_fields_together(capsys):
    # Valid username and valid password together
    validate(userName="TesterX", password="X1password")
    captured = capsys.readouterr().out
    assert "UserNameTesterX is valid" in captured
    assert "PasswordX1password is valid" in captured

def test_no_fields_prints_nothing(capsys):
    # Calling validate with neither key produces no output
    validate()
    assert capsys.readouterr().out == ""
