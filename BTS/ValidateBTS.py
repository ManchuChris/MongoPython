# Write a Python program to check whether a given a binary tree is a valid binary search tree (BST) or not. Go to the editor
#
# Let a binary search tree (BST) is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.

INT_MAX = 4294967296
INT_MIN = -4294967296
class VliadateBTS(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def balancedTreeTodo(list):
    if not list :
        return None
    midNumPosition = len(list) // 2
    balancedNodes = VliadateBTS(list[midNumPosition])
    balancedNodes.left = balancedTreeTodo(list[:midNumPosition])
    balancedNodes.right = balancedTreeTodo(list[midNumPosition + 1:])
    return balancedNodes


def printNode(balancedNodes):
    if not balancedNodes:
        return
    print(balancedNodes.value)
    printNode(balancedNodes.left)
    printNode(balancedNodes.right)


def validateBinarySTree(list):
    return _validateBinarySTree(list, INT_MIN, INT_MAX)


def _validateBinarySTree(listTest, minNum, maxNum):
    if not listTest:
        return True
    if listTest.value < minNum or listTest.value > maxNum:
        return False
    return _validateBinarySTree(listTest.left, minNum, listTest.value-1) and _validateBinarySTree(listTest.right, listTest.value+1, maxNum)


result = balancedTreeTodo([1, 2, 3, 4, 5, 6, 7])
print(validateBinarySTree(result))
