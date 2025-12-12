# Input data
test_data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

filename = "./23/input"
filename = "./23/test"


with open(filename, 'r') as fd:
    test_data = fd.read()

# Parse connections into a list of tuples
connections = [tuple(conn.split("-")) for conn in test_data.strip().split("\n")]

# Extract all unique computers
all_computers = set()
for conn in connections:
    all_computers.update(conn)

# Create an adjacency list to represent the graph
adjacency = {computer: set() for computer in all_computers}
for conn in connections:
    a, b = conn
    adjacency[a].add(b)
    adjacency[b].add(a)

# Find sets of three interconnected computers
sets_of_three = set()

for a in all_computers:
    for b in adjacency[a]:
        for c in adjacency[b]:
            # Check if `c` connects back to `a` and is not the same as `a` or `b`
            if c in adjacency[a] and a != b != c != a:
                # Sort to ensure uniqueness
                sets_of_three.add(tuple(sorted([a, b, c])))

# Print the results
print(f"CONNECTIONS: {len(connections)}")
print(f"COMPUTERS: {all_computers}")
print(f"NUMBER OF COMPUTERS: {len(all_computers)}")
print(f"SETS OF THREE:")
for s in sorted(sets_of_three):
    print(",".join(s))
print(f"NUMBER OF SETS OF THREE: {len(sets_of_three)}")
count = 0
for i in sets_of_three:
    if "t" == i[0][0] or "t" == i[1][0] or "t" == i[2][0]:
        print(i)
        count += 1
print(count)

import networkx as nx
import matplotlib.pyplot as plt








# Parse connections into a list of tuples
connections = [tuple(conn.split("-")) for conn in test_data.strip().split("\n")]

# Create a graph using NetworkX
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(connections)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)  # Use spring layout for better visualization
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

# Add title
plt.title("Social Graph Visualization", fontsize=16)
plt.show()
