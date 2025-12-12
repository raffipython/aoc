import networkx as nx
import matplotlib.pyplot as plt

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
#filename = "./23/test"


with open(filename, 'r') as fd:
    test_data = fd.read()


# Parse connections into a list of tuples
connections = [tuple(conn.split("-")) for conn in test_data.strip().split("\n")]

# Create an undirected graph using NetworkX
G = nx.Graph()
G.add_edges_from(connections)

# Find the largest clique (fully connected subgraph)
largest_clique = nx.algorithms.clique.find_cliques(G)
largest_clique = max(largest_clique, key=len)  # Get the largest clique by size

# Display the results
print(f"Largest Clique (Fully Connected Subgraph): {largest_clique}")
print(f"Number of Nodes in the Largest Clique: {len(largest_clique)}")

# Visualize the largest clique
clique_subgraph = G.subgraph(largest_clique)  # Create a subgraph of the largest clique

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(clique_subgraph)
nx.draw(clique_subgraph, pos, with_labels=True, node_size=500, node_color="lightgreen", font_weight="bold", font_size=10)
#plt.title("Largest Clique in the Graph (Undirected)")
#plt.show()
print(",".join(sorted(largest_clique)))
