class MyStack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        if len(self._data) == 0:
            raise IndexError
        return self._data[-1]

    def __len__(self):
        return len(self._data)


class MyQueue:

    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    # this is slow! O(n)
    def dequeue(self):
        return self._data.pop(0)

    def front(self):
        if len(self._data) == 0:
            raise IndexError
        return self._data[0]

    def __len__(self):
        return len(self._data)

# not as memory efficient
class MyFasterQueue:

    def __init__(self):
        self._data = []
        self._now_serving = 0

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        item = self._data[self._now_serving]
        self._data[self._now_serving] = None
        self._now_serving += 1
        if self._now_serving > len(self._data) / 2:
            self._shrink()
        return item

    def front(self):
        if len(self._data) == 0:
            raise IndexError
        return self._data[0]

    def __len__(self):
        return len(self._data)

    def _shrink(self):
        new_data = []
        for index in range(self._now_serving, len(self._data)):
            new_data.append(self._data[index])
        self._now_serving = 0



class CircularQueue:

    DEFAULT_CAPACITY = 20

    def __init__(self, initial_size = DEFAULT_CAPACITY):
        self._data = [None] * initial_size
        self._front = 0
        self._back = 0
        self._number_of_items = 0

    def enqueue(self, item):
        self._check_capacity()
        self._data[self._back] = item
        self._back += 1
        if self._back == len(self._data):
            self._back = 0
        self._number_of_items += 1

    def dequeue(self):
        if self._number_of_items == 0:
            raise IndexError
        item = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        if self._front == len(self._data):
            self._front = 0
        self._number_of_items -= 1
        return item

    def front(self):
        if self._number_of_items == 0:
            raise IndexError
        return self._data[self._front]

    def __len__(self):
        return self._number_of_items

    def _check_capacity(self):
        if self._number_of_items >= len(self._data):
            new_data = [None] * len(self._data) * 2
            new_data_index = 0
            for index in range(self._front, len(self._data)):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
            for index in range(0, self._back):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
            self._data = new_data
            self._front = 0
            self._back = self._number_of_items





def non_recursive_binary_search(some_list, item_to_find):
    first_index = 0
    last_index = len(some_list) - 1

    while(first_index <= last_index):
        middle_index =(last_index - first_index)//2+first_index
        if some_list[middle_index] == item_to_find:
            return True
        if item_to_find < some_list[middle_index]:
            last_index = middle_index - 1
        else:
            first_index = middle_index + 1


numbers = [ 1,2,3,4,5,6,7,8]

non_recursive_binary_search(numbers, 8)



myStack = MyStack()
for number in range(1,10):
    myStack.push(number)

while len(myStack) != 0:
    print(myStack.pop())


circularQueue = CircularQueue()
for number in range(1,30):
    circularQueue.enqueue(number)
    if number % 2:
        circularQueue.dequeue()