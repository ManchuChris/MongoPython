
def bfsCall(graph, start):
    queue = [start]
    seen = set()
    seen.add(start)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)


