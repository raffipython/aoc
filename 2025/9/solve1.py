import os
# 4763040296 good

i = 'input'
#i = './input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
print(lines)

biggest = []

def area(a, b):
    apart = a.split(",")
    ax = int(apart[0])
    ay = int(apart[1])
    bpart = b.split(",")
    bx = int(bpart[0])
    by = int(bpart[1])

    #print("-----")
    #print(ax, ay)
    #print(ax, by)
    #print(bx, by)
    #print(bx, ay)
    dx = abs(bx - ax + 1)
    dy = abs(by - ay + 1)
    if dy == 0:
        dy = 1
    if dx == 0:
        dy = 1
    #print("distance")
    #print(dx)
    #print(dy)
    print(f"{a:7} {b:7} area: {dx*dy}")
    #return 

for x in lines:
    prev = x
    for i in lines:
        if prev == i:
            pass
        else:
            a = area(prev, i)
            #print(a)
