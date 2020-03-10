class Position:
    def __init__(self, item, container, parent, children):
        self.item = item
        self.container = container
        self.parent = parent
        self.children = children

    def get_item(self):
        return self.item

class GenericTree:

    def __init__(self, item, parent = None):
        self.item = item
        self.children = []
        self.parent = parent

    def is_root(self, position):
        return position.parent == None

    def parent(self, position):
        return position.parent

    def children(self, position):
        return position.children

    def is_leaf(self, position):
        return len(position.children) == 0

    def __len__(self):
        length = 1
        for child in self.children:
            length += len(child)
        return length

    def is_empty(self):
        return self.item == None

    def root(self):
        return Position(self.item, self, None, self.children)

    def depth(self, position):
        if self.is_root(position):
            return 0
        return 1 + self.depth(self.parent(position))

    def height(self):
        current_max = 0
        for child in self.children:
            child_height = 1 + child.height()
            if child_height > current_max:
                current_max = child_height
        return current_max

    def bad_height(self): # O(n^2) - touches ever position, and every leaf all the way back to root
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p) )

