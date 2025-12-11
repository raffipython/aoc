import os
import networkx as nx
import matplotlib.pyplot as plt

# 428

i = 'input'
#i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
#print(lines)

def count_paths(graph, start, end):
    def dfs(node, visited):
        if node == end:
            return 1

        total = 0
        for nxt in graph.get(node, []):
            if nxt not in visited:  # avoid cycles
                total += dfs(nxt, visited | {nxt})

        return total

    return dfs(start, {start})

graph = {}

for line in lines:
    print(line)
    name = line.split(":")[0]
    edges = line.split(":")[1].split()

    graph.update({name: edges})

G = nx.DiGraph()

for node, targets in graph.items():
    for t in targets:
        G.add_edge(node, t)

plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True, node_color="lightgreen")

print(count_paths(graph, "you", "out"))
plt.show()

