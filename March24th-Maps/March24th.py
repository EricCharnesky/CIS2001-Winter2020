# Map - Key -> Value

class Item:

    def __init__(self, key, value=None):
        self._key = key
        self._value = value

    def __eq__(self, other):
        return self._key == other._key

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self._key < other._key


class MyHashMap:

    class BucketNode:

        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self, initial_size=11):
        self._data = [None] * initial_size
        self._number_of_items = 0

    def _resize(self):
        # don't actually just double in real life - find the smart math that makes these prime
        self._number_of_items = 0
        new_data = [None] * len(self._data) * 2
        for key in self:
            self._add_to_internal_storage(key, self[key], new_data)
        self._data = new_data

    def _add_to_internal_storage(self, key, value, storage):
        hash_value = hash(key)
        expected_index = hash_value % len(storage)
        if storage[expected_index] is None:
            self._number_of_items += 1
            node = self.BucketNode(Item(key, value))
            storage[expected_index] = node

        else:
            current_node = storage[expected_index]
            while current_node is not None:
                if key == current_node.item._key:
                    previous_value = current_node.item._value
                    current_node.item._value = value
                    return previous_value
                current_node = current_node.next
            new_node = self.BucketNode(Item(key, value))
            new_node.next = storage[expected_index]
            storage[expected_index] = new_node
            self._number_of_items += 1
            return

    def __getitem__(self, key):
        hash_value = hash(key)
        expected_index = hash_value % len(self._data)
        if self._data[expected_index] is not None:
            current_node = self._data[expected_index]
            while current_node is not None:
                if key == current_node.item._key:
                    return current_node.item._value
                current_node = current_node.next
        raise KeyError

    def __setitem__(self, key, value):
        if self._number_of_items / len(self._data) > .6:
            self._resize()
        return self._add_to_internal_storage(key, value, self._data)

    def __delitem__(self, key):
        hash_value = hash(key)
        expected_index = hash_value % len(self._data)
        if self._data[expected_index] is not None:
            current_node = self._data[expected_index]
            if current_node.item._key == key:
                previous_value = current_node.item._value
                self._data[expected_index] = current_node.next
                return previous_value

            while current_node.next is not None:
                if key == current_node.next.item._key:
                    previous_value = current_node.next.item._value
                    current_node.next = current_node.next.next
                    return previous_value
                current_node = current_node.next
            raise KeyError
        raise KeyError

    def __len__(self):
        return self._number_of_items

    def __iter__(self):
        for item in self._data:
            if item is not None:
                current_node = item
                while current_node is not None:
                    yield current_node.item._key
                    current_node = current_node.next



class MyBasicMap:

    def __init__(self):
        self._data = []

    def __getitem__(self, key):
        for item in self._data:
            if item._key == key:
                return item._value
        raise KeyError

    def __setitem__(self, key, value):
        for item in self._data:
            if item._key == key:
                item._value = value
                return
        self._data.append(Item(key, value))

    def __delitem__(self, key):
        for index in range(len(self._data)):
            if self._data[index]._key == key:
                self._data.pop(index)
                return
        raise KeyError

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item._key


class CoronaStats:

    def __init__(self, area_name, number_of_cases):
        self._area_name = area_name
        self._number_of_cases = number_of_cases

    def __eq__(self, other):
        if type(other) != CoronaStats:
            return False
        return self._area_name == other._area_name and self._number_of_cases == other._number_of_cases

    def __hash__(self):
        return hash(self._area_name)


new_york = CoronaStats('New York', 37258)
new_jersey = CoronaStats('New Jersey', 6876)
california = CoronaStats('California', 3243)
michigan = CoronaStats('Michigan', 2856)
washington = CoronaStats('Washington', 2588)
new_york_2 = CoronaStats('New York', 37258)


print(hash('Eric') + hash('John'))
print(hash('Eric' + 'John'))

#corona_stats = MyBasicMap()
corona_stats = MyHashMap()
corona_stats[new_york] = 385

corona_stats[new_jersey] = 81
corona_stats[new_york_2] = 385


corona_stats["New York"] = 25665
corona_stats["New Jersey"] = 3675
corona_stats["California"] = 2494
corona_stats["Washington"] = 2221
corona_stats["Michigan"] = 1791

for key in corona_stats:
    print(key, ":", corona_stats[key])


test_hash_map = MyHashMap()

for number in range(100):
    test_hash_map[number] = number

for key in test_hash_map:
    print(key, ":", test_hash_map[key])