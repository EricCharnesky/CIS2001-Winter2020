#      10
#     /  \
#    8    15
#   / \   / \
#  4   9 12  20

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


class BinarySearchTreeMap:

    class BinaryTreeNode:

        def __init__(self, data, parent=None, left=None, right=None):
            self._data = data
            self._parent = parent
            self._left = left
            self._right = right

    class BinaryTreePosition:

        def __init__(self, container, node):
            self._node = node
            self._container = container

        def element(self):
            return self._node._data

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _make_position(self, node):
        if node is None:
            return None
        return self.BinaryTreePosition(self, node)

    def _validate(self, position):
        if not isinstance(position, self.BinaryTreePosition):
            raise TypeError

        if position._container is not self:
            raise ValueError

        if position._node._parent is position._node:
            raise ValueError

        return position._node

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _add_root(self, item):
        self._root = self.BinaryTreeNode(item)

    def _parent(self, position):
        node = self._validate(position)
        return self._make_position(node._parent)

    def _left(self, position):
        node = self._validate(position)
        return self._make_position(node._left)

    def _right(self, position):
        node = self._validate(position)
        return self._make_position(node._right)

    def _add_right(self, position, item):

        if self._right(position) is not None:
            if item < self._right(position).element():
                return self._add_left(self._right(position), item)
            else:
                return self._add_right(self._right(position), item)
        else:
            node = self._validate(position)
            node._right = self.BinaryTreeNode(item, parent=node)
            self._size += 1
            return self._make_position(node._right)

    def _add_left(self, position, item):
        if self._left(position) is not None:
            if item < self._left(position).element():
                return self._add_left(self._left(position), item)
            else:
                return self._add_right(self._left(position), item)
        else:
            node = self._validate(position)
            node._left = self.BinaryTreeNode(item, parent=node)
            self._size += 1
            return self._make_position(node._left)

    def _subtree_search(self, position, key):
        if key == position.element()._key:
            return position
        elif key < position.element()._key:
            if self._left(position) is not None:
                return self._subtree_search(self._left(position), key)
        else:
            if self._right(position) is not None:
                return self._subtree_search(self._right(position), key)

    def __setitem__(self, key, value):
        if self.is_empty():
            self._add_root(Item(key, value))
            self._size += 1
            return self._make_position(self._root)
        else:
            position = self._subtree_search(self._make_position(self._root), key)
            if position is not None:
                previous_value = position.element()._value
                position.element()._value = value
                return previous_value
            else:
                root = self._make_position(self._root)
                if key < root.element()._key:
                    return self._add_left(root, Item(key, value))
                else:
                    return self._add_right(root, Item(key, value))

    def __getitem__(self, key):
        if self.is_empty():
            raise KeyError
        position = self._subtree_search(self._make_position(self._root), key)
        if position is None:
            raise KeyError
        return position.element()._value

    def first(self):
        if self.is_empty():
            return None
        return self._subtree_first_position(self._make_position(self._root))

    def _subtree_first_position(self, postition):
        current_position = postition
        while self._left(current_position):
            current_position = self._left(current_position)
        return current_position

    def _subtree_last_position(self, position):
        current_position = position
        while self._right(current_position):
            current_position = self._right(current_position)
        return current_position

    def last(self):
        if self.is_empty():
            return None
        return self._subtree_last_position(self._make_position(self._root))

    def before(self, position):
        if self._left(position):
            return self._subtree_last_position(self._left(position))
        current_position = position
        parent = self._parent(position)
        # find parent that is a right child
        while parent is not None and current_position == self._left(parent):
            current_position = parent
            parent = self._parent(parent)
        return parent

    def after(self, position):
        if self._right(position):
            return self._subtree_first_position(self._right(position))
        current_position = position
        parent = self._parent(position)
        # find parent that is a left child
        while parent is not None and current_position == self._right(parent):
            current_position = parent
            parent = self._parent(parent)
        return parent

    def __iter__(self):
        position = self.first()
        while position is not None:
            yield position.element()._key
            position = self.after(position)

    def delete(self, position):
        if self._left(position) is not None and self._right(position) is not None:
            replacement = self._subtree_last_position(self._left(position))
            replacement_parent = self._parent(replacement)
            replacement_left_child = self._left(replacement)
            if replacement_left_child is not None:
                replacement_parent._node._right = replacement_left_child._node
                replacement_left_child._node._parent = replacement_parent._node
            else:
                replacement_parent._node._right = None

            position._node._data = replacement._node._data
        else:
            if self._left(position) is not None:
                child = self._left(position)
            else:
                child = self._right(position)
            parent = self._parent(position)
            if child is not None:
                if parent is None:
                    self._root = child._node
                    child._node._parent = None
                else:
                    child._node._parent = parent._node
                    if self._left(parent) == position:
                        parent._node._left = child._node
                    else:
                        parent._node._right = child._node
            else:
                if parent is None:
                    self._root = None
                elif self._left(parent) == position:
                    parent._node._left = None
                else:
                    parent._node._right = None

        self._size -= 1


    def __delitem__(self, key):
        if self.is_empty():
            raise KeyError
        position = self._subtree_search(self._make_position(self._root), key)
        if position is None:
            raise KeyError
        self.delete(position)

my_binary_search_tree = BinarySearchTreeMap()
my_binary_search_tree[10] = 10
my_binary_search_tree[5] = 5
my_binary_search_tree[3] = 3
my_binary_search_tree[9] = 9
my_binary_search_tree[15] = 15
my_binary_search_tree[12] = 12
my_binary_search_tree[20] = 20


print("Forwards")
for key in my_binary_search_tree:
    print(key)

print()
print("Backwards")

current = my_binary_search_tree.last()
while current is not None:
    print(current.element()._key)
    current = my_binary_search_tree.before(current)


del my_binary_search_tree[10]

while not my_binary_search_tree.is_empty():
    print("Forwards")
    for key in my_binary_search_tree:
        print(key)
    my_binary_search_tree.delete(my_binary_search_tree.last())










