import random
import enum

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


class Suit(enum.Enum):
    Spades = 1
    Hearts = 2
    Clubs = 3
    Diamonds = 4


class Face(enum.Enum):
    Ace = 14
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


class Card:

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def __str__(self):
        return "{} of {}".format(self.face.name, self.suit.name)


class Deck:

    def __init__(self):
        self.cards = []
        for suit in Suit:
            for face in Face:
                self.cards.append( Card(suit, face) )

    def print(self):
        for card in self.cards:
            print( card )

if __name__ == "__main__":
    new_deck = Deck()

    new_deck.print()

    Card(Suit.Spades, Face.Ace)
    Card(Suit.Spades, Face.King)

