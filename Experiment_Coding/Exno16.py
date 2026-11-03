import heapq
graph = {'A':[('B',4),('C',2)], 'B':[('A',4),('C',1),('D',5)],
         'C':[('A',2),('B',1),('D',8)], 'D':[('B',5),('C',8),('E',2)],
         'E':[('D',2)]}
def dijkstra(start, goal):
    pq, dist, parent = [(0,start)], {start:0}, {start:None}
    while pq:
        d, u = heapq.heappop(pq)
        if u == goal:
            break
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v], parent[v] = nd, u
                heapq.heappush(pq, (nd,v))
    if goal not in dist:
        print("No path found")
        return
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    print("Shortest Path:", path[::-1])
    print("Total Distance:", dist[goal])
dijkstra('A', 'E')
