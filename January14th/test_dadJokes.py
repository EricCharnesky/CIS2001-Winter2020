from unittest import TestCase
import January14th

class TestDadJokes(TestCase):
    def test_hey_python_tell_me_a_joke(self):
        # arrange
        not_actually_random = January14th.NotActuallyRandom(0)
        dad_jokes = January14th.DadJokes(not_actually_random)
        expected_joke = """There are 2 kinds of people in the world
Those who can extrapolate from incomplete data"""

        # act
        actual_joke = dad_jokes.hey_python_tell_me_a_joke()

        # assert
        self.assertEqual(expected_joke, actual_joke)


