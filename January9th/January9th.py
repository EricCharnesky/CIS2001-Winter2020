import random


class GuessingGame:

    def __init__(self, max_number):
        self._magic_number = random.randint(1, max_number)
        self._number_of_guesses = 0

    def guess(self, number):
        self._number_of_guesses += 1
        if number == self._magic_number:
            return "You guessed it in {} guesses!".format(self._number_of_guesses)
        if number < self._magic_number:
            return "Your guess was too low!"
        return "Your guess was too high!"


