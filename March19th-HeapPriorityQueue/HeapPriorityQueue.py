class HeapPriorityQueue:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def _parent(self, index):
        if index % 2 == 0:
            index -= 1
        return index // 2

    def _left(self, index):
        return index * 2 + 1

    def _right(self, index):
        return index * 2 + 2

    def min(self):
        return self._data[0]

    def add(self, item):
        self._data.append(item)
        self._upheap(len(self._data) - 1 )

    def remove_min(self):
        value = self._data[0]
        if len(self._data) != 1:
            self._data[0] = self._data.pop()
            self._downheap(0)
        else:
            self._data.pop()
        return value

    def _swap(self, index, other_index):
        temp = self._data[index]
        self._data[index] = self._data[other_index]
        self._data[other_index] = temp

    def _upheap(self, index):
        if index == 0:
            return
        parent_index = self._parent(index)
        if self._data[index] < self._data[parent_index]:
            self._swap(index, parent_index)
            self._upheap(parent_index)

    def _downheap(self, index):
        left = self._left(index)
        if left >= len(self._data):
            return

        smallest_child_index = left

        right = self._right(index)
        if right < len(self._data):
            if self._data[right] < self._data[smallest_child_index]:
                smallest_child_index = right

        if self._data[index] > self._data[smallest_child_index]:
            self._swap(index, smallest_child_index)
            self._downheap(smallest_child_index)


