import os

i = 'input'
i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')

def process(line):
    print("-----------")
    count = 0
    diagram = line.split("]")[0].split("[")[1]
    lights = []
    temp = []
    for i in diagram:
        if i == "#":
            lights.append(True)
        else:
            lights.append(False)
        temp.append(False)
    wiring = line.split("]")[1].split("{")[0]
    #print(wiring)
    #joltage = line.split("{")[1].split("}")[0]
    #print(joltage)

    wiring_list = []
    for i in wiring.split():
        x = eval(i)
        wiring_list.append(x)

    print(line)    #main
    print(diagram) #graphical
    print(lights)  #goal
    print(temp)    #temp
    print(wiring_list) #switches
    switch = len(wiring_list)
    print(f"total switches: {switch}")
    for s in wiring_list:
        #print(type(s))
        pass

    lowest = 0
    for i in range(1,2**switch):
        print(i)
        
        





    return count

for line in lines[:1]:
    c = process(line)
    #print(c)
    #print(line.count("("))