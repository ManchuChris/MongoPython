# Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.
# For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.
# We can use sort algorithm

# Bubble sort

class kLargestElement:
    # def __init__(self, list):
    #     self.inputList = list
    #
    def bubbleSort(self, list, k):
        for i in range(0, len(list) - 1):
            for j in range(0, (len(list) - 1 - i)):
                temp = None
                if list[j] > list[j + 1]:
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp
        tmpList = list[(len(list) - k):]
        print(tmpList[::-1])  # reverse list


    def quickSort(self, list, low, high):
        if low < high:
            pi = self.partitionList(list, low, high)
            self.quickSort(list, low, pi - 1)
            self.quickSort(list, pi + 1, high)
        print(list)

    def partitionList(self, list, low, high):
        pivot = list[high-1]
        i = low - 1
        for j in range(low, high - 2):
            if list[j] < pivot:
                i = i + 1
                tmp = list[i]
                list[i] = list[j]
                list[j] = tmp
        tmp = list[i + 1]
        list[i + 1] = list[high-1]
        list[high-1] = tmp
        return i + 1


listInput = [4, 6, 3, 5, 2]
k = kLargestElement()
# k.bubbleSort(listInput, 3)
k.quickSort(listInput, 0, 5)
