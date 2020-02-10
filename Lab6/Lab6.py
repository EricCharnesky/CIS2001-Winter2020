import random


class Order:
    def __init__(self):
        self.burgers_ordered = random.randint(1, 5)
        self.fries_ordered = random.randint(1, 5)
        self.burgers_received = 0
        self.fries_received = 0


class Car:
    def __init__(self, time_arrived):
        self.time_arrived = time_arrived
        self.order = Order()

    def order_or_drive_off(self, current_time):
        if current_time >= self.time_arrived + 5:
            return
        return self.order


class DriveThru:

    def __init__(self):
        self.queue_of_cars = []
        self.money_earned = 0.0
        self.queue_of_burgers = []
        self.stack_of_fries = []
        self.grill = []
        self.deep_fryer = []


class Item:

    def __init__(self, name, cooked_at_time, profit):
        self.name = name
        self.cooked_at_time = cooked_at_time
        self.expires_at_time = cooked_at_time + 5
        self.profit = profit




