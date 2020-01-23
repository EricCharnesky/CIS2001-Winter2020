from unittest import TestCase
from project1 import Ship, Alignment, Battle

class TestShip(TestCase):
    def test_get_type(self):
        expected_type = "Ship"
        test_ship = Ship("Some Ship", 0, 0, Alignment.Us, 0, 0, 0)

        actual_type = test_ship.get_type()

        self.assertEqual(expected_type, actual_type)

    def test_attack_us_attacks_them(self):
        starting_health = 10
        attack_power = 5
        range = 10
        test_ship = Ship("Some Ship", 0, 0, Alignment.Us, starting_health, range, attack_power)
        test_target = Ship("Target Ship", 0, 0, Alignment.Them, starting_health, range, attack_power)
        expected_health = starting_health - attack_power

        test_ship.attack(test_target)
        actual_health = test_target.get_current_health()

        self.assertEqual(expected_health, actual_health)

    def test_attack_chaotic_attacks(self):
        starting_health = 10
        attack_power = 5
        range = 10
        test_ship = Ship("Some Ship", 0, 0, Alignment.Chaotic, starting_health, range, attack_power)
        test_target = Ship("Target Ship", 0, 0, Alignment.Chaotic, starting_health, range, attack_power)
        expected_health = starting_health - attack_power

        test_ship.attack(test_target)
        actual_health = test_target.get_current_health()

        self.assertEqual(expected_health, actual_health)

    def test_attack_not_in_range(self):
        starting_health = 10
        attack_power = 5
        range = 10
        test_ship = Ship("Some Ship", 0, 0, Alignment.Chaotic, starting_health, range, attack_power)
        test_target = Ship("Target Ship", 10, 10, Alignment.Chaotic, starting_health, range, attack_power)
        expected_health = starting_health

        test_ship.attack(test_target)
        actual_health = test_target.get_current_health()

        self.assertEqual(expected_health, actual_health)

    def test_status(self):
        test_ship = Ship("Some Ship", 0, 0, Alignment.Us, 10, 0, 0)
        expect_status = \
"""Some Ship
type: Ship
health:10
location:(0, 0)"""

        actual_status = test_ship.status()

        self.assertEqual(expect_status, actual_status)

    def test_assess_damage(self):
        max_health = 10
        damage = 2
        test_ship = Ship("Some Ship", 0, 0, Alignment.Us, max_health, 0, 0)
        test_ship.assess_damage(damage)

        actual_health = test_ship.get_current_health()

        self.assertEqual(max_health - damage, actual_health)

    def test_assess_damage_doesnt_go_below_zero(self):
        max_health = 10
        damage = 100
        test_ship = Ship("Some Ship", 0, 0, Alignment.Us, max_health, 0, 0)
        test_ship.assess_damage(damage)

        actual_health = test_ship.get_current_health()

        self.assertEqual(0, actual_health)

    def test_assess_damage_doesnt_go_above_max(self):
        max_health = 10
        damage = -10
        test_ship = Ship("Some Ship", 0, 0, Alignment.Us, max_health, 0, 0)
        test_ship.assess_damage(damage)

        actual_health = test_ship.get_current_health()

        self.assertEqual(max_health, actual_health)

    def test_move(self):
        start_x = 1
        start_y = 1
        x_move = 1
        y_move = 1
        expected_health = 9
        test_ship = Ship("Some Ship", start_x, start_y, Alignment.Us, 10, 0, 0, x_move, y_move)
        test_ship.assess_damage(2)

        test_ship.move()
        actual_x = test_ship.get_x()
        actual_y = test_ship.get_y()
        actual_health = test_ship.get_current_health()

        self.assertEqual(x_move + start_x, actual_x)
        self.assertEqual(y_move + start_y, actual_y)
        self.assertEqual(expected_health, actual_health)

    def test_change_alignment(self):
        expected_alignment = Alignment.Them
        test_ship = Ship("Some Ship", 0, 0, Alignment.Us, 0, 0, 0)

        test_ship.change_alignment()
        actual_alignment = test_ship.get_alignment()

        self.assertEqual(expected_alignment, actual_alignment)

    def test_battle_status(self):
        test_ship = Battle("Some Battleship", 0, 0, Alignment.Us)
        expect_status = \
"""Some Battleship
type: Battleship
health:100
location:(0, 0)
Torpedos: 10"""

        actual_status = test_ship.status()

        self.assertEqual(expect_status, actual_status)

    def test_battleship_attack_with_torpedos(self):
        test_ship = Battle("Some Ship", 0, 0, Alignment.Us)
        test_target = Battle("Target Ship", 0, 0, Alignment.Them)
        expected_health = 80

        test_ship.attack(test_target)
        actual_health = test_target.get_current_health()

        self.assertEqual(expected_health, actual_health)
