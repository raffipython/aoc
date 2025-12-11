import os

i = 'final'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')[:-1]
print(lines)

total = 0
for i in lines:
    print("------")
    parts = i.split()
    op = parts[0]
    items = parts[1:]
    print(op)
    sub = 0
    for x in items:
        x = int(x)
        print(x)
        if op == "+":
            sub += x
        else:
            sub *= x
    print(sub)
    total += sub

print(total)


