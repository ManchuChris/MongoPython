# Write a Python program to create a Balanced Binary Search Tree (BST)
# using an array (given) elements where array elements are sorted in ascending order.
# Balanced Tree


class balancedTree(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def balancedTreeTodo(list):
    if not list :
        return None
    midNumPosition = len(list) // 2
    balancedNodes = balancedTree(list[midNumPosition])
    balancedNodes.left = balancedTreeTodo(list[:midNumPosition])
    balancedNodes.right = balancedTreeTodo(list[midNumPosition + 1:])
    return balancedNodes


def printNode(balancedNodes):
    if not balancedNodes:
        return
    print(balancedNodes.value)
    printNode(balancedNodes.left)
    printNode(balancedNodes.right)


result = balancedTreeTodo([1, 2, 3, 4, 5, 6, 7])
printNode(result)
