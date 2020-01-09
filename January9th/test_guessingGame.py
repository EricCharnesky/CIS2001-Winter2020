from unittest import TestCase
from January9th import GuessingGame


class TestGuessingGame(TestCase):
    def test_guess_guess_correctly_in_one_guess(self):

        # AAA

        # arrange - set up all variables
        magic_number = 4
        expected_result = "You guessed it in 1 guesses!"
        max_number = 10

        test_game = GuessingGame(max_number)
        test_game._magic_number = magic_number

        # act - call the code we are testing
        actual_result = test_game.guess(magic_number)

        # assert - did we get what we expected
        self.assertEqual(expected_result, actual_result)

    def test_guess_guess_too_low(self):

        # AAA

        # arrange - set up all variables
        magic_number = 4
        expected_result = "Your guess was too low!"
        max_number = 10

        test_game = GuessingGame(max_number)
        test_game._magic_number = max_number

        # act - call the code we are testing
        actual_result = test_game.guess(magic_number)

        # assert - did we get what we expected
        self.assertEqual(expected_result, actual_result)

    def test_guess_guess_too_high(self):

        # AAA

        # arrange - set up all variables
        magic_number = 4
        expected_result = "Your guess was too high!"
        max_number = 10

        test_game = GuessingGame(max_number)
        test_game._magic_number = magic_number

        # act - call the code we are testing
        actual_result = test_game.guess(max_number)

        # assert - did we get what we expected
        self.assertEqual(expected_result, actual_result)
