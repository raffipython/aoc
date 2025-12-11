import os
i = 'input'
with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
def area(a, b):
    apart = a.split(",")
    bpart = b.split(",")
    dx = abs(int(bpart[0]) - int(apart[0]) + 1)
    dy = abs(int(bpart[1]) - int(apart[1]) + 1)
    return  dx*dy
biggest = 0
for x in lines:
    prev = x
    for i in lines:
        if prev != i:
            a = area(prev, i)
            if biggest < a:
                biggest = a
print(biggest)