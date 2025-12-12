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
    # Initialize wire values
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


def calculate_output(wire_values):
    """
    Combine the values of wires starting with 'z' into a binary number and convert to decimal.
    """
    z_wires = {k: v for k, v in wire_values.items() if k.startswith("z")}
    binary_string = "".join(
        str(z_wires[f"z{i:02}"]) for i in range(len(z_wires))
    )
    decimal_value = int(binary_string[::-1], 2)  # Reverse binary string for correct bit order
    return decimal_value, binary_string


def main(input_text):
    """
    Main function to parse input, simulate circuit, and calculate output.
    """
    initial_values, gate_definitions = parse_input(input_text)
    wire_values = boolean_simulation(initial_values, gate_definitions)

    # Print all wire values for debugging and verification
    print("Wire Values:")
    for wire, value in sorted(wire_values.items()):
        print(f"{wire}: {value}")

    # Compute the final output
    decimal_value, binary_string = calculate_output(wire_values)

    # Print the computed output
    print("\nz-wire values:")
    for i in range(len(binary_string)):
        print(f"z{i:02}: {binary_string[::-1][i]}")

    print(f"\nBinary value: {binary_string[::-1]}")
    print(f"Decimal value: {decimal_value}")
    return decimal_value


# Example usage
input_text = """\
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

filename = "./24/input"
with open(filename, 'r') as fd:
    input_text = fd.read()

result = main(input_text)
print(f"\nFinal Decimal Value: {result}")





