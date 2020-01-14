import random


class RandomWrapperInterface:

    def randint(self, start, end):
        raise NotImplemented


class NotActuallyRandom(RandomWrapperInterface):

    def __init__(self, not_random_number):
        self.not_random_number = not_random_number

    def randint(self, start, end):
        return self.not_random_number


class RandomWrapper(RandomWrapperInterface):

    def randint(self, start, end):
        return random.randit(start, end)


class DadJokes:

    def __init__(self, randomWrapper):
        self._jokes = [
"""There are 2 kinds of people in the world
Those who can extrapolate from incomplete data""",
"""I once bought a wooden car. Wooden engine, wooden doors,...
What do you know, it wooden start!"""
]
        self._randomWrapper = randomWrapper

    def hey_python_tell_me_a_joke(self):
        return self._jokes[ self._randomWrapper.randint(0, len(self._jokes) - 1)]