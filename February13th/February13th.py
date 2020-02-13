class Node:

    def __init__(self, item, next=None, previous=None):
        self.item = item
        self.next = next
        self.previous = previous


class DoublyLinkedList:

    def __init__(self):
        self._front = None
        self._back = None
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    def append(self, item):
        if self._front is None:
            self._front = Node(item)
            self._back = self._front
        else:
            self._back.next = Node(item, previous=self._back)
            self._back = self._back.next
        self._number_of_items += 1

    def get(self, index):
        if index < 0 or index >= self._number_of_items:
            raise IndexError

        current_node = self._front
        for current_index in range(index):
            current_node = current_node.next
        return current_node.item

    def insert(self, item, index):
        if index < 0 or index >= self._number_of_items:
            raise IndexError

        if index == 0:
            self._front = Node(item, self._front)
        else:
            current_node = self._front
            for next_node in range(index-1):
                current_node = current_node.next
            current_node.next = Node(item, current_node.next, current_node)

        self._number_of_items += 1

    def pop(self, index=None):
        if index is None:
            index = self._number_of_items - 1
        if index < 0 or index >= self._number_of_items:
            raise IndexError

        if index == 0:
            if self._front == self._back:
                self._back = None
            item = self._front.item
            self._front = self._front.next
            if self._front:
                self._front.previous = None
        else:
            current_node = self._front
            for next_node in range(index-1):
                current_node = current_node.next

            if current_node.next == self._back:
                self._back = current_node

            item = current_node.next.item
            current_node.next = current_node.next.next
            if current_node.next:
                current_node.next.previous = current_node

        self._number_of_items -= 1
        return item

    def remove(self, item):
        if self._front is None:
            raise IndexError

        if self._front.item == item:
            if self._front == self._back:
                self._back = None
            self._front = self._front.next
            if self._front:
                self._front.previous = None
            self._number_of_items -= 1
            return

        else:
            current_node = self._front
            while current_node.next is not None:
                if current_node.next.item == item:
                    current_node.next = current_node.next.next
                    if current_node.next:
                        current_node.next.previous = current_node
                    else:
                        self._back = current_node
                    self._number_of_items -= 1
                    return
            raise ValueError("item not found in list!")

