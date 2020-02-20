import random

class Node:

    def __init__(self, item, next=None, previous=None):
        self.item = item
        self.next = next
        self.previous = previous

class Position:

    def __init__(self, container, node):
        self._container = container
        self._node = node

    def item(self):
        return self._node.item

    def __eq__(self, other):
        return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
        return not (self == other)

class PositionalList:

    def __init__(self):
        self._head = Node(None)
        self._head.previous = self._head
        self._head.next = self._head
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    def append(self, item):
        new_node = Node(item, previous=self._head.previous, next=self._head)
        new_node.next.previous = new_node
        new_node.previous.next = new_node
        self._number_of_items += 1

    def get(self, index):
        if index < 0 or index >= self._number_of_items:
            raise IndexError

        if index <= self._number_of_items // 2:
            current_node = self._head.next
            for current_index in range(index):
                current_node = current_node.next
            return current_node.item
        else:
            current_node = self._head.previous
            for current_index in range(self._number_of_items - 1, index):
                current_node = current_node.previous
            return current_node.item

    def insert(self, item, index):
        if index < 0 or index >= self._number_of_items:
            raise IndexError

        if index <= self._number_of_items // 2:
            current_node = self._head
            for current_index in range(index):
                current_node = current_node.next
        else:
            current_node = self._head.previous
            for current_index in range(self._number_of_items - 1, index):
                current_node = current_node.previous

        new_node = Node(item, previous=current_node, next=current_node.next)
        new_node.next.previous = new_node
        new_node.previous.next = new_node

        self._number_of_items += 1

    def pop(self, index=None):
        if index is None:
            index = self._number_of_items - 1
        if index < 0 or index >= self._number_of_items:
            raise IndexError

        current_node = self._head.next
        for next_node in range(index):
            current_node = current_node.next

        item = current_node.item
        current_node.next.previous = current_node.previous
        current_node.previous.next = current_node.next
        current_node.item = None

        self._number_of_items -= 1
        return item

    def remove(self, item):

        current_node = self._head.next
        while current_node != self._head:
            if current_node.item == item:
                current_node.next.previous = current_node.previous
                current_node.previous.next = current_node.next
                current_node.item = None
                self._number_of_items -= 1
                return
        raise ValueError("item not found in list!")


    def _validate_position(self, position):
        if not isinstance(position, Position):
            raise TypeError
        if position._container is not self:
            raise ValueError
        if position._node.next is None:
            raise ValueError
        return position._node

    def _make_position(self, node):
        if node is self._head:
            return None
        return Position(self, node)

    def first(self):
        return self._make_position(self._head.next)

    def last(self):
        return self._make_position(self._head.previous)

    def before(self, position):
        node = self._validate_position(position)
        return self._make_position(node.previous)

    def insert_before(self, position, item):
        node = self._validate_position(position)
        return self._insert_between(item, previous=node.previous, next=node)

    def after(self, position):
        node = self._validate_position(position)
        return self._make_position(node.next)

    def insert_after(self, position, item):
        node = self._validate_position(position)
        return self._insert_between(item, previous=node, next=node.next)

    def _insert_between(self, item, previous, next):
        new_node = Node(item, previous=previous, next=next)
        new_node.next.previous = new_node
        new_node.previous.next = new_node
        self._number_of_items += 1
        return self._make_position(new_node)

    def add_first(self, item):
        return self._insert_between(item, previous=self._head, next=self._head.next)

    def add_last(self, item):
        return self._insert_between(item, previous=self._head.previous, next=self._head)

    def delete(self, position):
        node = self._validate_position(position)
        node.next.previous = node.previous
        node.previous.next = node.next
        item = node.item
        node.item = None
        return item

    def replace(self, position, new_item):
        node = self._validate_position(position)
        old_item = node.item
        node.item = new_item
        return old_item

    def __iter__(self):
        current_node = self._head.next
        while current_node != self._head:
            yield current_node.item
            current_node = current_node.next



def insertion_sort(positional_list):
    if len(positional_list) > 1:
        marker = positional_list.first()
        while marker != positional_list.last():
            pivot = positional_list.after(marker)
            item = pivot.item()
            if item > marker.item():
                marker = pivot
            else:
                current_position = marker
                while current_position != positional_list.first() and \
                    positional_list.before(current_position).item() > item:
                    current_position = positional_list.before(current_position)
                positional_list.insert_before(current_position, item)
                positional_list.delete(pivot)



my_positional_list = PositionalList()
for number in range(1, 11):
    my_positional_list.add_first(random.randint(1,100))

insertion_sort(my_positional_list)

for value in my_positional_list:
    print(value)









