filename = "./23/test"
filename = "./23/input"

with open(filename, 'r') as fd:
    connections = fd.read().split("\n")

all_computers = []
for i in connections:
    computers = i.split("-")
    all_computers.append(computers[0])
    all_computers.append(computers[1])

all_computers = set(all_computers)


for computer in all_computers:
    print(computer)
    for x in connections:
        if computer in x:
            print(x)

print(f"CONNECTIONS: {len(connections)}")
print(f"COMPUTERS: {all_computers}")
print(f"COMPUTERS: {len(all_computers)}")



