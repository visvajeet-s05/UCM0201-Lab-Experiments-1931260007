V = ['A', 'B', 'C', 'D', 'E']
edges = [(1,'A','B'), (3,'A','C'), (2,'B','C'),
         (4,'B','D'), (5,'C','D'), (6,'C','E'), (7,'D','E')]
parent = {v:v for v in V}
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]
def union(a, b):
    x, y = find(a), find(b)
    if x != y:
        parent[y] = x
        return True
    return False
mst, total = [], 0
for w, u, v in sorted(edges):
    if union(u, v):
        mst.append((u, v, w))
        total += w
print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(u, "-", v, ":", w)
print("Total Installation Cost:", total)