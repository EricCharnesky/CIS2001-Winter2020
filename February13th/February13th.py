class Node:

    def __init__(self, item, next=None, previous=None):
        self.item = item
        self.next = next
        self.previous = previous


class DoublyLinkedList:

    def __init__(self):
        self._head = Node()
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
            for current_index in range(self._number_of_items-1, index):
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
            for current_index in range(self._number_of_items-1, index):
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
        if self._front is None:
            raise IndexError

        current_node = self._head.next
        while current_node != self._head:
            if current_node.item == item:
                current_node.next.previous = current_node.previous
                current_node.previous.next = current_node.next
                current_node.item = None
                self._number_of_items -= 1
                return
        raise ValueError("item not found in list!")

