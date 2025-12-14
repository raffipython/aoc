import os
#593 too low
#598 works
#print("PART TWO")

i = 'good'
i = 'exceltest'
#i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')

newranges = []
for line in lines:
    newranges.append([int(line.split(" ")[0]),int(line.split(" ")[1])])

print(newranges)
total = 0 
for r in newranges:
    x = (r[1] - r[0]) + 2
    print(f"{r[0]:15} {r[1]:15} {x:15}")
    total += x
print(total)
