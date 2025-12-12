# Registers
reg_a = 0
reg_b = 0
reg_c = 0

# Outputs
output = []

def combo_value(operand):
    """
    Resolve the value of a combo operand.
    """
    if operand in [0, 1, 2, 3]:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c
    else:
        raise ValueError("Invalid combo operand: 7 is reserved.")

def adv(operand):
    """
    Opcode 0: Perform integer division of A by 2^combo_operand.
    """
    global reg_a
    denominator = 2 ** combo_value(operand)
    reg_a = reg_a // denominator

def bxl(operand):
    """
    Opcode 1: XOR register B with the literal operand.
    """
    global reg_b
    reg_b = reg_b ^ operand

def bst(operand):
    """
    Opcode 2: Write (combo operand mod 8) to register B.
    """
    global reg_b
    reg_b = combo_value(operand) % 8

def jnz(operand):
    """
    Opcode 3: Jump to literal operand if A is not zero.
    """
    global reg_a
    return operand if reg_a != 0 else None

def bxc(operand):
    """
    Opcode 4: XOR register B with register C and ignore operand.
    """
    global reg_b, reg_c
    reg_b = reg_b ^ reg_c

def out(operand):
    """
    Opcode 5: Output (combo operand mod 8).
    """
    value = combo_value(operand) % 8
    output.append(value)

def bdv(operand):
    """
    Opcode 6: Perform integer division of A by 2^combo_operand and store in B.
    """
    global reg_b
    denominator = 2 ** combo_value(operand)
    reg_b = reg_a // denominator

def cdv(operand):
    """
    Opcode 7: Perform integer division of A by 2^combo_operand and store in C.
    """
    global reg_c
    denominator = 2 ** combo_value(operand)
    reg_c = reg_a // denominator

# Instruction map
instructions = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

def run_program(registers, program):
    """
    Execute a program on the virtual machine.
    :param registers: A tuple (A, B, C) representing the initial state of registers.
    :param program: A list of opcodes and operands.
    """
    global reg_a, reg_b, reg_c, output
    reg_a, reg_b, reg_c = registers
    output = []

    eip = 0  # Instruction pointer

    while eip < len(program):
        opcode = program[eip]
        operand = program[eip + 1]
        eip += 2  # Default increment

        if opcode not in instructions:
            raise ValueError(f"Invalid opcode: {opcode}")

        if opcode == 3:  # jnz has a special behavior
            new_eip = instructions[opcode](operand)
            if new_eip is not None:
                eip = new_eip
                continue
        else:
            instructions[opcode](operand)

    return reg_a, reg_b, reg_c, output

registers = (35200350,0,0)
program = [2,4,1,2,7,5,4,7,1,3,5,5,0,3,3,0]
result = run_program(registers, program)
print("Registers:", result[:3])
print("Output:", result[3])

out = ""
for i in result[3]:
    out = out + str(i) + ","

print(out[:-1])
