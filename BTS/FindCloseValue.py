

class balancedTree(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def balancedTreeTodo(list):
    if not list:
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


def closest_value(root, target):
    a = root.value
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = closest_value(kid, target)
    return min((a, b), key=lambda x: abs(target - x))


result1 = balancedTreeTodo([10, 20, 30, 40, 50, 60, 70])
printNode(result1)
a = closest_value(result1, 31)
print("The cloest num: ", a)
