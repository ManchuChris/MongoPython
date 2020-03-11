# Giving an array, every element presents the height of a tree. You have to jump from one tree to another same height tree,
# How many paths can you make. EX: [6,4,3,4,6], There are 4 path, 6->6 4->4 and 6<-6 ,  4<-4
# EX: [3,8,3] There is not any path, since 8 is too tall. 3 can go over from top of 8


def checkPath(list):
    count = 0
    for a in range(0, len(list)):
        for b in range(a + 1, len(list)):
            if list[a] < list[b]:
                break
            if list[a] == list[b]:
                count = count + 1

    print(count*2)


list = [6, 4, 3, 4, 6, 4, 3, 6]

checkPath(list)
