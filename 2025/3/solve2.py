import os

i = 'input'
i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
#print(lines)
totalfinal = 0

#####################
for line in lines[:]:
    print("-----------------")
    l = 0
    print(line)
    print(line[:-11])
    line = line[:-11]
    for i in line:
        if int(i) > l:
            l = int(i)
    max = l # max digit in line

    print(line.index(str(max)))


    cmax = line.count(str(l)) # count of that max
    second = None
    if cmax == 1:
        if int(line[-1]) == l:
            x = l # second digit
            found = False
            c = 1 # local counter
            while not found:
                temp = line.count(str(l-c))
                if temp > 0:
                    found = True
                else:
                    c += 1
            y = l-c
            z = f"{y}{x}"
            print(z)
            totalfinal += int(z)
        else:
            x = l # first digit
            found = False
            c = 1 # local counter
            templine = line[line.index(str(l))+1:]
            #print(templine)
            templ = 0
            for i in templine:
                if int(i) > templ:
                    templ = int(i)
            tempmax = templ # max digit in line    
            z = f"{x}{tempmax}"
            print(z)
            totalfinal += int(z)
    else:
        z = int(f"{l}{l}")
        print(z)
        totalfinal += z

#####################
print("----")
print(totalfinal)
