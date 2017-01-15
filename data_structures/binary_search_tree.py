class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # === Getter Setter ===

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    # === Node navigation ===

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current_node, new_node):
        if new_node.get_data() <= current_node.get_data():
            if not current_node.has_left():
                current_node.set_left(new_node)
            else:
                self._insert(current_node.get_left(), new_node)
        else:
            if not current_node.has_right():
                current_node.set_right(new_node)
            else:
                self._insert(current_node.get_right(), new_node)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            return max(self._height(node.get_left()), self._height(node.get_right())) + 1

    def inorder(self):
        if self.root is None:
            return None
        else:
            self._inorder(self.root)

    def _inorder(self, current_node):
        if current_node.has_left():
            self._inorder(current_node.get_left())
        print(current_node.get_data())
        if current_node.has_right():
            self._inorder(current_node.get_right())

    def preorder(self):
        if self.root is None:
            return None
        else:
            self._preorder(self.root)

    def _preorder(self, current_node):
        print(current_node.get_data())
        if current_node.has_left():
            self._preorder(current_node.get_left())
        if current_node.has_right():
            self._preorder(current_node.get_right())

    def postorder(self):
        if self.root is None:
            return None
        else:
            self._postorder(self.root)

    def _postorder(self, current_node):
        if current_node.has_left():
            self._postorder(current_node.get_left())
        if current_node.has_right():
            self._postorder(current_node.get_right())
        print(current_node.get_data())


