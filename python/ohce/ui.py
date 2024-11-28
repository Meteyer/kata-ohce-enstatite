from ohce import reverse


class ConsoleInteractor:
    def read_input(self):
        return input()

    def print_message(self, message):
        print(message)


class UI:
    def __init__(self, interactor=None):
        if interactor is None:
            interactor = ConsoleInteractor
        self.interactor = interactor

    def main_loop(self):
        while True:
            input = self.interactor.read_input()
            if input == "quit":
                break
            reversed = reverse(input)
            self.interactor.print_message(reversed)
            if reversed == input:
                self.interactor.print_message("That was a palindrome!")
