import os
#593 too low

i = 'input'
#i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')

empty = lines.index("")

rangesTemp = lines[:empty]
ranges = []
for r in rangesTemp:
    ranges.append([int(r.split("-")[0]),int(r.split("-")[1])])

items = lines[empty+1:]

def is_in_range(x):
    for y in ranges:
        if x >= int(y[0]) and x <= int(y[1]):
            return True
    return False

for r in ranges:
    start = r[0]
    end =   r[1]
    size = len(str(start))
    diff = end - start

total = 0
for x in items:
    size = len(x)
    is_in = is_in_range(int(x))
    if is_in:
        total += 1
print(total)