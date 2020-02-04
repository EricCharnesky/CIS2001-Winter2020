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