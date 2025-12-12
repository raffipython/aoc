import os
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque   # ✅ for BFS queue

# 2 is wrong

i = 'input'
#i = 'input2'
#i = 'input3'

with open(i, 'r') as fd:
    f = fd.read().strip()
    lines = f.split('\n')

def count_paths_bfs(graph, start, end):
    global path
    path = []

    # queue items: (current_node, visited_set)
    queue = deque()
    queue.append((start, frozenset([start])))

    total = 0

    while queue:
        node, visited = queue.popleft()

        if node == end:
            # store a sorted list of nodes in this path (same as your DFS version)
            path.append(sorted(visited))
            total += 1
            continue

        for nxt in graph.get(node, []):
            if nxt not in visited:  # avoid cycles per-path
                queue.append((nxt, visited | {nxt}))

    return total


graph = {}

for line in lines:
    if not line.strip():
        continue
    name, rest = line.split(":")
    edges = rest.split()
    graph[name] = edges

#print(graph)

print(count_paths_bfs(graph, "svr", "out"))

counter = 0
for p in path:
    if "fft" in p and "dac" in p:
        print(p)
        counter += 1

print(counter)
