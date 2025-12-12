filename = "./24/input"
filename = "./24/test"
filename = "./24/test1"


with open(filename, 'r') as fd:
    data = fd.read()

lines = data.split("\n")

init  = lines[:lines.index("")]
gates = lines[lines.index("") + 1:]

def boolean(x):
    if x == "1":
        return True
    return False

data_dict = {}
for i in init:
    data_dict.update({i[:3]:boolean(i[5])})

gates_dict = {}
for i in gates:
    parts = i.split(" ")
    if data_dict.get(parts[0]):
        gates_dict.update({parts[0]: data_dict.get(parts[0])})
    else:
        gates_dict.update({parts[0]: False})
    if data_dict.get(parts[2]):
        gates_dict.update({parts[2]: data_dict.get(parts[2])})
    else:
        gates_dict.update({parts[2]: False})
    if data_dict.get(parts[4]):
        gates_dict.update({parts[4]: data_dict.get(parts[4])})
    else:
        gates_dict.update({parts[4]: False})

def or_gate(x, y):
    return x or y

def and_gate(x, y):
    return x and y

def xor_gate(x, y):
    if x and y or (not x and not y):
        return False
    return True

#print(gates_dict)

for i in gates:
    parts = i.split(" ")
    #print(parts)
    if parts[1] == "AND":
        gates_dict.update({parts[4]:and_gate(gates_dict.get(parts[0]), gates_dict.get(parts[2]))})
    elif parts[1] == "OR":
        gates_dict.update({parts[4]:or_gate(gates_dict.get(parts[0]), gates_dict.get(parts[2]))})
    elif parts[1] == "XOR":
        gates_dict.update({parts[4]:xor_gate(gates_dict.get(parts[0]), gates_dict.get(parts[2]))})
    else:
        pass  

#print(gates_dict)
output = []
for z in sorted(gates_dict.keys()):
    if "z" in z:
        if gates_dict.get(z):
            output.append("1")
        else:
            output.append("0")

print("".join(output[::-1]))

