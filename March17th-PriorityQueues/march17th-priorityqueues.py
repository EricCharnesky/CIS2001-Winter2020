class PriorityQueue:

    def __init__(self):
        self.storageTree = ArrayBasedBinaryTree()
        self.number_of_items = 0

    def add(self, item):
        pass
        # add to index of number_of_items in the internal heap/tree storage
        # next position to keep a 'complete' heap form
        # complete == every level is full and the leaf level is filling from the left
        # recursively up-heap with the parent node
        # if node is < parent, swap and recurse

    def min(self):
        if not self.is_empty():
            return self.storageTree[0]
        raise IndexError

    def remove_min(self):
        pass


class ArrayBasedBinaryTree:

    class Node:

        def __init__(self, data, index):
            self.data = data
            self.index = index

    class Position:

        def __init__(self, container, node):
            self.container = container
            self.node = node

    def __init__(self):
        self._storage = [None] * 16
        self._size = 0

    def root(self):
        return self._make_position(self._storage[0])

    def _make_position(self, node):
        if node is None:
            return None
        return self.Position(self, node)

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError

        if position._container is not self:
            raise ValueError

        if position._node.index == -1:
            raise ValueError

        return position._node

    def left(self, position):
        return self._make_position(self._storage[position.node.index * 2 + 1])

    def right(self, position):
        return self._make_position(self._storage[position.node.index * 2 + 2])

    def parent(self, position):
        if position.node.index == 0:
            return None

        if position.node.index % 2 == 0:
            parent_index = (position.node.index - 1) // 2
        else:
            parent_index = position.node.idex // 2

        return self._make_position(self._storage[parent_index])


class LinkedBinaryTree:

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

    def root(self):
        return self._make_position(self._root)

    def parent(self, position):
        node = self._validate(position)
        return self._make_position(node._parent)

    def left(self, position):
        node = self._validate(position)
        return self._make_position(node._left)

    def right(self, position):
        node = self._validate(position)
        return self._make_position(node._right)

    def sibling(self, position):
        parent = self.parent(position)
        if parent is None:
            return None
        if position == self.left(parent):
            return self.right(parent)
        return self.left(parent)

    def children(self, position):
        if self.left(position) is not None:
            yield self.left(position)
        if self.right(position) is not None:
            yield self.right(position)

    def num_children(self, position):
        node = self._validate(position)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def add_root(self, data):
        if self._root is not None:
            raise ValueError
        self._size += 1
        self._root = self.BinaryTreeNode(data)
        return self._make_position(self._root)

    def add_left(self, position, data):
        node = self._validate(position)
        if node._left is not None:
            raise ValueError
        self._size += 1
        node._left = self.BinaryTreeNode(data, node)
        return self._make_position(node._left)

    def add_right(self, position, data):
        node = self._validate(position)
        if node._right is not None:
            raise ValueError
        self._size += 1
        node._right = self.BinaryTreeNode(data, node)
        return self._make_position(node._right)

    def _replace(self, position, data):
        node = self._validate(position)
        previous_value = node._data
        node._data = data
        return previous_value

    def delete(self, position):
        node = self._validate(position)
        if self.num_children(position) == 2:
            raise ValueError
        if node._left is not None:
            child = node._left
        elif node._right is not None:
            child = node._right
        else:
            child = None

        if child is not None:
            child._parent = node._parent

        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._data

    def attach(self, position, left_tree, right_tree):
        node = self._validate(position)
        if self.num_children(position) != 0:
            raise ValueError
        if not type(self) is type(left_tree) is type(right_tree):
            raise TypeError
        self._size += len(left_tree) + len(right_tree)
        if not left_tree.is_empty():
            left_tree._root._parent = node
            node._left = left_tree._root
            left_tree._root = None
            left_tree._size = 0
        if not right_tree.is_empty():
            right_tree._root._parent = node
            node._right = right_tree._root
            right_tree._root = None
            right_tree._size = 0


first_tree = LinkedBinaryTree()
root = first_tree.add_root(10)
root_left = first_tree.add_left(root, 5)
root_right = first_tree.add_right(root, 15)

first_tree.add_right(root_left, 8)
first_tree.add_left(root_right, 12)