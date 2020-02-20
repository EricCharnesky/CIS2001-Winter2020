class TransportMethod:

    def __init__(self, time_for_one_way_trip_from_dock, capacity):
        self.capacity = capacity
        self.current_number_of_items = 0
        self.time_for_one_way_trip_from_dock = time_for_one_way_trip_from_dock
        self.time_until_fully_loaded = 0

    def load_item(self, time_worker_left_the_dock):
        self.current_number_of_items += 1
        if self.current_number_of_items == self.capacity:
            self.time_until_fully_loaded = time_worker_left_the_dock + self.time_for_one_way_trip_from_dock

        # returning the time the worker should get back
        return time_worker_left_the_dock + 2 * self.time_for_one_way_trip_from_dock


class Dock:

    def __init__(self, train_capacity_list, plane_capacity_list, train_item_list, plane_item_list):
        self.trains = []
        for index, train_capacity in enumerate(train_capacity_list):
            self.trains.append(TransportMethod(index+1, train_capacity))

        self.planes = []
        for index, plane_capacity in enumerate(plane_capacity_list):
            self.planes.append(TransportMethod((index+1) * 5, plane_capacity))

        self.train_items_queue_of_stacks = []
        self._stage_train_items(train_item_list)

        self.plane_items_queue = []
        for item in plane_item_list:
            self.plane_items_queue.append(item)

        self._load_trains()
        self._load_planes()

    def _load_trains(self):
        current_time = 0
        while len(self.train_items_queue_of_stacks) != 0:
            current_stack = self.train_items_queue_of_stacks.pop(0)
            while len(current_stack) != 0:
                item = current_stack.pop()
                current_time = self.trains[item-1].load_item(current_time)

    def _load_planes(self):
        current_time = 0
        while len(self.plane_items_queue) != 0:
            item = self.plane_items_queue.pop(0)
            current_time = self.planes[item - 1].load_item(current_time)

    def _stage_train_items(self, train_item_list):

        stack_of_items = []
        for item in train_item_list:
            if len(stack_of_items) == 5:
                self.train_items_queue_of_stacks.append(stack_of_items)
                stack_of_items = []
            stack_of_items.append(item)

        # add last stack to the queue
        self.train_items_queue_of_stacks.append(stack_of_items)

    def output_calculated_load_times(self):
        print(" ".join(str(train.time_until_fully_loaded) for train in self.trains))
        print(" ".join(str(plane.time_until_fully_loaded) for plane in self.planes))


train_capacity_list = input()
train_capacity_list = [ int(item) for item in train_capacity_list.split() ]

plane_capacity_list = input()
plane_capacity_list = [ int(item) for item in plane_capacity_list.split() ]

train_item_list = input()
train_item_list = [ int(item) for item in train_item_list.split() ]

plane_item_list = input()
plane_item_list = [ int(item) for item in plane_item_list.split() ]

dock = Dock(train_capacity_list, plane_capacity_list, train_item_list, plane_item_list)
dock.output_calculated_load_times()
