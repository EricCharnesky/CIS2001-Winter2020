import enum
import math


class Alignment(enum.Enum):
    Us = 1
    Them = 2
    Chaotic = 3


class Ship:

    def __init__(self, name, x, y, alignment, max_health, range, attack_power, x_move = 0, y_move = 0):
        self._name = name
        self._x_location = x
        self._y_location = y
        self._alignment = alignment
        self._max_health = max_health
        self._range = range
        self._attack_power = attack_power
        self._current_health = max_health
        self._x_move = x_move
        self._y_move = y_move

    def get_current_health(self):
        return self._current_health

    def get_type(self):
        return "Ship"

    def get_x(self):
        return self._x_location

    def get_y(self):
        return self._y_location

    def get_alignment(self):
        return self._alignment

    def _is_within_range(self, target):
        return math.hypot(self._x_location - target.get_x(), self._y_location - target.get_y() ) <= self._range

    def _is_enemy(self, target):
        return self._alignment == Alignment.Chaotic or \
            self._alignment != target.get_alignment()

    def attack(self, target):
        if self._is_within_range(target) and self._is_enemy(target):
            target.assess_damage(self._attack_power)

    def status(self):
        return "{}\n".format(self._name) \
            + "type: {}\n".format(self.get_type()) \
            + "health:{}\n".format(self._current_health) \
            + "location:({}, {})".format(self.get_x(), self.get_y())

    def assess_damage(self, damage):
        self._current_health -= damage
        if self._current_health < 0:
            self._current_health = 0
        elif self._current_health > self._max_health:
            self._current_health = self._max_health

    def move(self):
        self._x_location += self._x_move
        self._y_location += self._y_move
        self.assess_damage(-1)

    def change_alignment(self):
        if self._alignment == Alignment.Us:
            self._alignment = Alignment.Them
        elif self._alignment == Alignment.Them:
            self._alignment = Alignment.Us


class Battle(Ship):

    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment, 100, 10, 10, -1, -1)
        self._torpedos = 10

    def get_type(self):
        return "Battleship"

    def attack(self, target):

        if self._torpedos > 0:
            self._attack_power += 10

        super().attack(target)

        if self._torpedos > 0:
            self._attack_power -= 10
            self._torpedos -= 1

    def status(self):
        return super().status() + "\nTorpedos: {}".format(self._torpedos)


class Cruiser(Ship):

    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment, 50, 50, 5, 1, 2)

    def get_type(self):
        return "Cruiser"


class Repair(Cruiser):

    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment)
        self._max_health = 20
        self._current_health = 20
        self._range = 25

    def get_type(self):
        return "Repair"

    def attack(self, target):
        if self._is_within_range(target) and self._alignment == target.get_alignment:
            target.assess_damage(target._max_health)


class Corvette(Ship):

    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment, 25, 20, 0, 5, 5)

    def get_type(self):
        return "Corvette"

    def attack(self, target):
        if self._is_within_range(target) and self._is_enemy(target):
            target.change_alignment()