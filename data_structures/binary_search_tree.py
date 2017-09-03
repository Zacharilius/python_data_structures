class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @property
    def has_left(self):
        return self.left is not None

    @property
    def has_right(self):
        return self.right is not None

    def __str__(self):
          return str(self.data)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current_node, new_node):
        if new_node.data <= current_node.data:
            if not current_node.has_left:
                current_node.left = new_node
            else:
                self._insert(current_node.left, new_node)
        else:
            if not current_node.has_right:
                current_node.right = new_node
            else:
                self._insert(current_node.right, new_node)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            return max(self._height(node.left), self._height(node.right)) + 1

    def inorder(self):
        output = []
        self._inorder(self.root, output)
        return output

    def _inorder(self, current_node, output):
        if current_node.has_left:
            self._inorder(current_node.left, output)
        output.append(current_node.data)
        if current_node.has_right:
            self._inorder(current_node.right, output)

    def preorder(self):
        output = []
        self._preorder(self.root, output)
        return output

    def _preorder(self, current_node, output):
        output.append(current_node.data)
        if current_node.has_left:
            self._preorder(current_node.left, output)
        if current_node.has_right:
            self._preorder(current_node.right, output)

    def postorder(self):
        output = []
        self._postorder(self.root, output)
        return output

    def _postorder(self, current_node, output):
        if current_node.has_left:
            self._postorder(current_node.left, output)
        if current_node.has_right:
            self._postorder(current_node.right, output)
        output.append(current_node.data)
