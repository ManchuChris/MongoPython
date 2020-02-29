
def dfsCall(graph, start):
    stack = [start]
    seen = set()
    seen.add(start)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)
