# Given two numbers represented by two linked lists, write a function that returns the sum list.
# The sum list is linked list representation of the addition of two input numbers. It is not allowed to modify the lists.
# Also, not allowed to use explicit extra space (Hint: Use Recursion)

class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node

    def addTwoLists(self, firstList, secondList):
        Prev = None
        temp = None
        carry = 0
        while firstList is not None or secondList is not None:
            firstValue = 0 if firstList is None else firstList.value
            secondValue = 0 if secondList is None else secondList.value
            Sum = carry + firstValue + secondValue
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            temp = node(Sum)
            if self.head is None:
                self.head = temp
            else:
                Prev.next = temp

            Prev = temp
            if firstList is not None:
                firstList = firstList.next
            if secondList is not None:
                secondList = secondList.next
        if carry > 0:
            temp.next = node(carry)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value),
            temp = temp.next


first = linkedList()
second = linkedList()

first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
print("First List is "),
first.printList()

second.push(4)
second.push(8)
print("\nSecond List is "),
second.printList()

finalList = linkedList()
finalList.addTwoLists(first.head, second.head)
print("\nsum List is "),
finalList.printList()
