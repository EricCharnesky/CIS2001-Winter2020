class DynamicArray:

    def __init__(self):
        self._storage = [None] * 4
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    def __getitem__(self, index):
        self._is_index_valid(index)
        return self._storage[index]

    #???
    #def __setitem__(self, key, value):

    def _is_index_valid(self, index):
        if not 0 <= index < self._number_of_items:
            raise IndexError()

    def insert(self, index, item):
        self._is_index_valid(index)
        self._check_capacity()
        for new_index in range(self._number_of_items, index, -1):
            self._storage[new_index] = self._storage[new_index-1]
        self._insert_item(index, item)

    def _insert_item(self, index, item):
        self._storage[index] = item
        self._number_of_items += 1

    def _resize(self):
        new_storage = [None] * ( 2 * len(self._storage) )
        for index in range(len(self._storage)):
            new_storage[index] = self._storage[index]
        self._storage = new_storage

    def remove(self, item):
        for index in range(self._number_of_items):
            if self._storage[index] == item:
                for new_index in range(index, self._number_of_items-1):
                    self._storage[new_index] = self._storage[new_index+1]

                self._number_of_items -= 1
                self._storage[self._number_of_items] = None
                return
        raise ValueError("value not found")

    def append(self, item):
        self._check_capacity()
        self._insert_item(self._number_of_items, item)

    def _check_capacity(self):
        if self._number_of_items >= len(self._storage):
            self._resize()



def selection_sort(some_array):
    for insert_into_index in range(len(some_array)-1):
        smallest_index = insert_into_index
        for comparison_index in range(insert_into_index + 1, (len(some_array))):
            if some_array[comparison_index] < some_array[smallest_index]:
                smallest_index = comparison_index
        temp = some_array[insert_into_index]
        some_array[insert_into_index] = some_array[smallest_index]
        some_array[smallest_index] = temp

def insertion_sort(some_array):
    for index in range(1, len(some_array)):
        current = some_array[index]
        previous = current
        while previous > 0 and some_array[previous - 1] > current:
            some_array[previous] = some_array[previous - 1]
            previous -= 1
        some_array[previous] = current

dynamic_array = []
dynamic_array.append(7)
dynamic_array.append(28)
dynamic_array.append(2)
dynamic_array.append(42)

insertion_sort(dynamic_array)

for item in dynamic_array:
    print(item)