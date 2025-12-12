import json

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


def export_graph_data(initial_values, gate_definitions):
    """
    Export the graph data to a JSON format suitable for embedding in an HTML file.
    """
    nodes = []
    links = []

    # Add initial values as nodes
    for wire, value in initial_values.items():
        nodes.append({
            "id": wire,
            "label": f"{wire}\\n{value}",
            "color": "lightblue"
        })

    # Add gates and connections
    for gate in gate_definitions:
        input1 = gate["input1"]
        input2 = gate["input2"]
        gate_type = gate["gate"]
        output = gate["output"]

        # Add nodes if they don't exist
        if input1 not in [node["id"] for node in nodes]:
            nodes.append({"id": input1, "label": input1, "color": "red"})
        if input2 not in [node["id"] for node in nodes]:
            nodes.append({"id": input2, "label": input2, "color": "red"})
        if output not in [node["id"] for node in nodes]:
            nodes.append({"id": output, "label": gate_type, "color": "lightgreen"})

        # Add links
        links.append({"source": input1, "target": output})
        links.append({"source": input2, "target": output})

    return {"nodes": nodes, "links": links}


def generate_html(graph_data, output_file):
    """
    Generate an HTML file with the graph data embedded.
    """
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Circuit Diagram</title>
        <script src="https://d3js.org/d3.v7.min.js"></script>
        <style>
            .node circle {{
                stroke: #000;
                stroke-width: 1.5px;
            }}
            .node text {{
                font-size: 12px;
                text-anchor: middle;
            }}
            .link {{
                fill: none;
                stroke: #888;
                stroke-width: 1.5px;
            }}
        </style>
    </head>
    <body>
        <script>
            const graph = {json.dumps(graph_data)};

            function drawGraph(graph) {{
                const width = window.innerWidth;
                const height = window.innerHeight;

                const svg = d3.select("body").append("svg")
                    .attr("width", width)
                    .attr("height", height)
                    .call(d3.zoom().on("zoom", (event) => {{
                        svgGroup.attr("transform", event.transform);
                    }}))
                    .append("g");

                const svgGroup = svg.append("g");

                const link = svgGroup.selectAll(".link")
                    .data(graph.links)
                    .enter().append("line")
                    .attr("class", "link")
                    .style("stroke", "#999")
                    .style("stroke-width", 2);

                const node = svgGroup.selectAll(".node")
                    .data(graph.nodes)
                    .enter().append("g")
                    .attr("class", "node")
                    .call(d3.drag()
                        .on("start", dragstarted)
                        .on("drag", dragged)
                        .on("end", dragended));

                node.append("circle")
                    .attr("r", 10)
                    .style("fill", d => d.color);

                node.append("text")
                    .text(d => d.label)
                    .attr("dy", -12)
                    .attr("dx", 0);

                const simulation = d3.forceSimulation(graph.nodes)
                    .force("link", d3.forceLink(graph.links).id(d => d.id).distance(100))
                    .force("charge", d3.forceManyBody().strength(-300))
                    .force("center", d3.forceCenter(width / 2, height / 2))
                    .on("tick", () => {{
                        link.attr("x1", d => d.source.x)
                            .attr("y1", d => d.source.y)
                            .attr("x2", d => d.target.x)
                            .attr("y2", d => d.target.y);

                        node.attr("transform", d => `translate(${{d.x}},${{d.y}})`);
                    }});

                function dragstarted(event, d) {{
                    if (!event.active) simulation.alphaTarget(0.3).restart();
                    d.fx = d.x;
                    d.fy = d.y;
                }}

                function dragged(event, d) {{
                    d.fx = event.x;
                    d.fy = event.y;
                }}

                function dragended(event, d) {{
                    if (!event.active) simulation.alphaTarget(0);
                    d.fx = null;
                    d.fy = null;
                }}
            }}

            drawGraph(graph);
        </script>
    </body>
    </html>
    """

    with open(output_file, "w") as f:
        f.write(html_template)


# Example Usage
if __name__ == "__main__":

    # Input and Execution
    filename = "./24/input"

    with open(filename, "r") as fd:
        input_text = fd.read()

    print(input_text)

    initial_values, gate_definitions = parse_input(input_text)
    graph_data = export_graph_data(initial_values, gate_definitions)
    print(graph_data)
    generate_html(graph_data, "./24/index.html")
    print("HTML file generated: ./24/index.html")
