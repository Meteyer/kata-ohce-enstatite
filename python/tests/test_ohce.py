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
    greeter = Greeter(clock=clock_mock)
    for i in range(24):
        clock_mock.current_hour.return_value = i
        assert greeter.greet() is not None


class MainSetupOhce:
    def __init__(self):
        self.input_words = ["hello", "oto", "quit"]
        self.expected_outputs = ["olleh", "oto", "That was a palindrome!"]
        self.generated_outputs = []

    def handle_output(self, message):
        self.generated_outputs.append(message)


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
    interactor_mock = Mock()
    ohce_main = OhceMain()

    interactor_mock.read_input.side_effect = ohce_main.input_words
    interactor_mock.print_message.side_effect = ohce_main.handle_output

    ui = UI(interactor=interactor_mock)
    ui.main_loop()

    assert len(ohce_main.generated_outputs) == len(ohce_main.expected_outputs)
    assert ohce_main.generated_outputs == ohce_main.expected_outputs
