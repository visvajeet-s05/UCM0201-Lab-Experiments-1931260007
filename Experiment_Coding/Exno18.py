graph = {'A':['B','C'], 'B':['A','C'], 'C':['A','B','D','E'],
         'D':['C','E'], 'E':['C','D']}
print("Vertex Degrees:")
for v in graph:
    print(v, ":", len(graph[v]))
if any(len(graph[v]) % 2 for v in graph):
    print("Euler Circuit does not exist")
else:
    g = {v:list(e) for v,e in graph.items()}
    stack, circuit = ['A'], []
    while stack:
        u = stack[-1]
        if g[u]:
            v = g[u].pop()
            g[v].remove(u)
            stack.append(v)
        else:
            circuit.append(stack.pop())
    circuit.reverse()
    print("\nEuler Circuit:", " -> ".join(circuit))