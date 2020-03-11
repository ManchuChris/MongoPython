# _function is private function.
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class binary_search_tree(object):

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, currentNode):
        if value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = Node(value)
                currentNode.parent = currentNode
            else:
                self._insert(value, currentNode.left)
        elif value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = Node(value)
                currentNode.parent = currentNode
            else:
                self._insert(value, currentNode.right )
        else:
            print("The value is already in the tree.")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, currentNode):
        if currentNode is not None:
            self._print_tree(currentNode.left)
            print("node:" + str(currentNode.value))
            self._print_tree(currentNode.right)


tree = binary_search_tree()
tree.insert(10)
tree.insert(12)
tree.insert(5)
tree.insert(4)
tree.insert(20)
tree.insert(8)
tree.insert(7)
tree.insert(15)
tree.insert(13)
tree.print_tree()
