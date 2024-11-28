from unittest.mock import Mock
import pytest
from ohce.greeter import Greeter
from ohce.ui import UI


@pytest.fixture
def clock_mock():
    return Mock()


def test_nightly_greeting(clock_mock):
    """
    Assert that greeter says "Good night" at midnight
    (when current hour is 0)
    """
    clock_mock.current_hour.return_value = 0

    greeter = Greeter(clock=clock_mock)

    assert greeter.greet() == "Good night"


def test_greeting_never_returns_none(clock_mock):
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """
    pytest.fail("TODO")

def test_ohce_main_loop():
    """
    Given the following inputs:
    - hello
    - oto
    - quit

    Check that the following messages are printed:
    - olleh
    - oto
    - That was a palindrome!
    """
    pytest.fail("TODO")
