# #There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# this is list of list to graph
#  graph = {prerequisites[0][0]: [prerequisites[0][1]]}
#             for l in prerequisites[1:]:
#                if l[0] in graph.keys():
#                   graph[l[0]].append(l[1])
#                else:
#                   graph[l[0]] = [l[1]]
# class Solution:
#     def cycle_exists(self, dependencies, index, target):
#         if (len(dependencies[index]) == 0):
#             return False
#         elif (target in dependencies[index]):
#             return True
#         else:
#             for course in dependencies[index]:
#                 if (self.cycle_exists(dependencies, course, target)):
#                     return True
#
#             return False
#
#     def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
#         dependencies = [set() for _ in range(n)]
#
#         for pair in prerequisites:
#             dependencies[pair[0]].add(pair[1])
#
#             if (self.cycle_exists(dependencies, pair[1], pair[0])):
#                 return False
#
#         return True

a = [set() for _ in range(5)]
a[0].add(1)
a[0].add(2)
a[1].add(2)
print(a)

b = {i: [] for i in range(5)}
b[0].append(1)
b[0].append(2)
b[1].append(1)
print(b)