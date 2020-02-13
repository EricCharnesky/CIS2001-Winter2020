class Node:

    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedStack:

    def __init__(self):
        self.first = None

    def push(self,item):
        if self.first is None:
            self.first = Node(item)
        else:
            self.first = Node(item, self.first)

    def pop(self):
        if self.first is None:
            raise IndexError
        item = self.first.item
        self.first = self.first.next
        return item

    def top(self):
        if self.first is None:
            raise IndexError
        return self.first.item


class LinkedQueue:

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, item):
        if self.front is None:
            self.front = Node(item)
            self.back = self.front
        else:
            self.back.next = Node(item)
            self.back = self.back.next

    def dequeue(self):
        if self.front is None:
            raise IndexError

        item = self.front.item
        if self.front == self.back:
            self.back = None
        self.front = self.front.next
        return item

    def front(self):
        if self.front is None:
            raise IndexError
        return self.front.item


class LinkedList:

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
            self._back.next = Node(item)
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
            current_node.next = Node(item, current_node.next)

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
        else:
            current_node = self._front
            for next_node in range(index-1):
                current_node = current_node.next

            if current_node.next == self._back:
                self._back = current_node

            item = current_node.next.item
            current_node.next = current_node.next.next

        self._number_of_items -= 1
        return item

    def remove(self, item):
        if self._front is None:
            raise IndexError

        if self._front.item == item:
            if self._front == self._back:
                self._back = None
            self._front = self._front.next
            self._number_of_items -= 1
            return

        else:
            current_node = self._front
            while current_node.next is not None:
                if current_node.next.item == item:
                    current_node.next = current_node.next.next
                    if current_node.next is None:
                        self._back = current_node
                    self._number_of_items -= 1
                    return
            raise ValueError("item not found in list!")


