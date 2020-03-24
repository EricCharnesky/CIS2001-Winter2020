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


corona_stats = MyBasicMap()

corona_stats["New York"] = 25665
corona_stats["New Jersey"] = 3675
corona_stats["California"] = 2494
corona_stats["Washington"] = 2221
corona_stats["Michigan"] = 1791

for key in corona_stats:
    print(key, ":", corona_stats[key])
