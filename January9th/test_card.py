from unittest import TestCase
from January9th import Suit, Face, Card

class TestCard(TestCase):
    def test_str(self):

        # AAA

        # Arrange
        expected_string = "Ace of Spades"
        card = Card(Suit.Spades, Face.Ace)

        # act
        actual_string = str(card)

        # assert
        self.assertEqual(expected_string, actual_string)