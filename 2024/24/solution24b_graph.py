import networkx as nx
import plotly.graph_objects as go

def create_circuit_graph(initial_values, gate_definitions):
    """
    Create a directed graph to represent the circuit.
    Automatically assigns layers based on dependencies.
    """
    G = nx.DiGraph()

    # Add initial values as nodes
    for wire, value in initial_values.items():
        G.add_node(wire, label=f"{wire}\n{value}", color="lightblue", layer=0)

    # Add gates and connections
    for gate in gate_definitions:
        input1 = gate["input1"]
        input2 = gate["input2"]
        gate_type = gate["gate"]
        output = gate["output"]

        # Check if inputs exist; initialize if missing
        if input1 not in G.nodes:
            G.add_node(input1, label=f"{input1}\n?", color="red", layer=0)
        if input2 not in G.nodes:
            G.add_node(input2, label=f"{input2}\n?", color="red", layer=0)

        # Determine layer for gate and output
        layer1 = G.nodes[input1].get("layer", 0)
        layer2 = G.nodes[input2].get("layer", 0)
        gate_layer = max(layer1, layer2) + 1

        # Add gate as a node
        G.add_node(output, label=f"{gate_type}", color="lightgreen", layer=gate_layer)

        # Connect inputs to the gate
        G.add_edge(input1, output)
        G.add_edge(input2, output)

    return G

def draw_interactive_circuit_graph(G):
    """
    Draw the circuit graph interactively using Plotly.
    """
    pos = nx.multipartite_layout(G, subset_key="layer")
    edge_x = []
    edge_y = []

    # Create edges
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_x = []
    node_y = []
    node_text = []
    node_color = []

    # Create nodes
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(G.nodes[node].get('label', node))
        node_color.append(G.nodes[node].get('color', 'gray'))

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=node_text,
        textposition='top center',
        marker=dict(
            size=20,
            color=node_color,
            line=dict(width=2, color='black')
        ),
        hoverinfo='text'
    )

    # Create the figure
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title="Interactive Circuit Diagram",
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                    ))

    fig.show()

def parse_input(input_text):
    """
    Parse the input text into initial wire values and gate definitions.
    """
    lines = input_text.strip().split("\n")
    initial_values_section = []
    gate_definitions_section = []

    # Separate initial values and gate definitions
    section = 0
    for line in lines:
        if line.strip() == "":
            section += 1
            continue
        if section == 0:
            initial_values_section.append(line)
        elif section == 1:
            gate_definitions_section.append(line)

    # Parse initial values
    initial_values = {}
    for line in initial_values_section:
        wire, value = line.split(": ")
        initial_values[wire] = int(value)

    # Parse gate definitions
    gate_definitions = []
    for line in gate_definitions_section:
        parts = line.split(" ")
        gate_definitions.append({
            "input1": parts[0],
            "gate": parts[1],
            "input2": parts[2],
            "output": parts[4]
        })

    return initial_values, gate_definitions

# Example Usage
if __name__ == "__main__":
    # Example input
    input_text = """\
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z00
x01 AND y01 -> z01
x02 AND y02 -> z02
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z05
"""

    filename = "./24/input"
    with open(filename, 'r') as fd:
        input_text = fd.read()

    initial_values, gate_definitions = parse_input(input_text)

    # Create and draw the interactive graph
    circuit_graph = create_circuit_graph(initial_values, gate_definitions)
    draw_interactive_circuit_graph(circuit_graph)
