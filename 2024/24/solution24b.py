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


def boolean_simulation(initial_values, gate_definitions):
    """
    Simulate the circuit based on the initial values and gate definitions.
    """
    wire_values = initial_values.copy()

    # Define gate operations
    gate_operations = {
        "AND": lambda x, y: x & y,
        "OR": lambda x, y: x | y,
        "XOR": lambda x, y: x ^ y
    }

    # Process gates repeatedly until all wires stabilize
    unresolved_gates = gate_definitions.copy()
    resolved = set(wire_values.keys())

    while unresolved_gates:
        next_unresolved = []
        for gate in unresolved_gates:
            input1, input2, operation, output = (
                gate["input1"],
                gate["input2"],
                gate["gate"],
                gate["output"],
            )

            # Check if inputs are ready
            if input1 in resolved and input2 in resolved:
                val1 = wire_values[input1]
                val2 = wire_values[input2]
                wire_values[output] = gate_operations[operation](val1, val2)
                resolved.add(output)
            else:
                next_unresolved.append(gate)
        unresolved_gates = next_unresolved

    return wire_values


def compare(x, y, z):
    """
    Compare x AND y with z to identify mismatches and validate pairings.
    """
    xx = sorted(x.keys())
    yy = sorted(y.keys())
    zz = sorted(z.keys())
    swaps = []
    valid_pairings = []

    print("---------------")
    for i in range(len(xx)):
        expected = x.get(xx[i]) & y.get(yy[i])
        actual = z.get(zz[i])
        print(f"Expected ({xx[i]} AND {yy[i]}): {expected}, Actual ({zz[i]}): {actual}")
        if expected != actual:
            swaps.append((zz[i], expected, actual))
        else:
            valid_pairings.append((xx[i], yy[i], zz[i]))
    print("---------------")
    return swaps, valid_pairings


def find_swap_pairs(swaps):
    """
    Find valid pairs of swaps to process.
    """
    swap_pairs = []
    for i in range(0, len(swaps) - 1, 2):
        swap_pairs.append((swaps[i][0], swaps[i + 1][0]))
    return swap_pairs


def validate_gate_pairings(gate_definitions, valid_pairings):
    """
    Ensure gates are correctly paired based on valid pairings.
    """
    for x_wire, y_wire, z_wire in valid_pairings:
        for gate in gate_definitions:
            if gate["output"] == z_wire:
                if gate["input1"] != x_wire or gate["input2"] != y_wire:
                    print(f"Fixing gate for {z_wire}: {gate}")
                    gate["input1"] = x_wire
                    gate["input2"] = y_wire


def swap_gate_outputs(gate_definitions, swap_pairs):
    """
    Swap the output wires for the given pairs of gates.
    """
    for gate1, gate2 in swap_pairs:
        # Find the gates corresponding to these outputs
        idx1 = next(i for i, g in enumerate(gate_definitions) if g["output"] == gate1)
        idx2 = next(i for i, g in enumerate(gate_definitions) if g["output"] == gate2)
        # Swap the outputs
        gate_definitions[idx1]["output"], gate_definitions[idx2]["output"] = (
            gate_definitions[idx2]["output"],
            gate_definitions[idx1]["output"],
        )


def main(input_text):
    """
    Main function to parse input, simulate circuit, and calculate output.
    """
    initial_values, gate_definitions = parse_input(input_text)

    x_wires = {k: v for k, v in initial_values.items() if k.startswith("x")}
    y_wires = {k: v for k, v in initial_values.items() if k.startswith("y")}
    all_swaps = set()  # Keep track of all swaps performed

    iteration = 0  # Track the iteration for debugging
    while True:
        iteration += 1
        print(f"\nIteration {iteration}: Simulating circuit...")
        # Simulate the circuit
        wire_values = boolean_simulation(initial_values, gate_definitions)

        # Extract z wires
        z_wires = {k: v for k, v in wire_values.items() if k.startswith("z")}

        # Compare outputs and identify swaps
        swaps, valid_pairings = compare(x_wires, y_wires, z_wires)
        if not swaps:
            print("\nNo swaps needed. Circuit is correct.")
            break  # If no swaps are needed, the circuit is correct

        # Print the swaps for debugging
        print(f"Swaps identified in iteration {iteration}: {[swap[0] for swap in swaps]}")

        # Add the swaps to the global set
        all_swaps.update(swap[0] for swap in swaps)

        # Find pairs of swaps and process them
        swap_pairs = find_swap_pairs(swaps)
        swap_gate_outputs(gate_definitions, swap_pairs)

        # Validate and fix gate pairings
        validate_gate_pairings(gate_definitions, valid_pairings)

    # Sort and join all swaps for output
    corrected_swaps = sorted(all_swaps)
    return ",".join(corrected_swaps)


# Input and Execution
filename = "./24/test_b"

with open(filename, "r") as fd:
    input_text = fd.read()

corrected_swaps = main(input_text)
print(f"\nCorrected Swaps: {corrected_swaps}")
