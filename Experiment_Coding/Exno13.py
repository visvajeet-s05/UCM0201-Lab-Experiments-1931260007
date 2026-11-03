from collections import deque
graph = {'A':['B','C'], 'B':['A','D','E'], 'C':['A','E'],
         'D':['B','F'], 'E':['B','C','F'], 'F':['D','E']}
def bfs(start, goal):
    q, visited, parent, order = deque([start]), {start}, {start:None}, []
    while q:
        node = q.popleft()
        order.append(node)
        if node == goal:
            break
        for v in graph[node]:
            if v not in visited:
                visited.add(v)
                parent[v] = node
                q.append(v)
    if goal not in parent:
        print("No route found")
        return
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    print("Traversal Order:", order)
    print("Shortest Path:", path[::-1])
    print("Corridors:", len(path)-1)
bfs('A', 'F')