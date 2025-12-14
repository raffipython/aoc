
i = 'areas'
#i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')

def process(line):
    print(line)
    a = line.split(":")[0]
    x = int(a.split("x")[0])
    y = int(a.split("x")[1])
    area = x*y
    parts = line.split(": ")[1].split()
    print(parts)
    total = 0
    for part in parts:
        part = int(part)
        total += part*9
    print(total)
    if total > area:
        return False
    return True

answer = 0
for line in lines:
    if process(line):
        answer += 1
    else:
        pass

print(answer)