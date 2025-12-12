def convert(item):
    result = []
    print()
    one = []
    two = []
    three = []
    four = []
    five = []
    for i in range(1,6):
        one.append(item[i][0])
        two.append(item[i][1])
        three.append(item[i][2])
        four.append(item[i][3])
        five.append(item[i][4])
    result.append(one.count("#"))
    result.append(two.count("#"))
    result.append(three.count("#"))
    result.append(four.count("#"))
    result.append(five.count("#"))
    return result

def match(lock, key):
    for i in range(5):
        if lock[i] + key[i] > 5:
            return 0
    return 1

filename = "./25/test"
filename = "./25/input"

with open(filename, 'r') as fd:
    f = fd.read().split("\n")

locks = []
keys = []
for i in range(0, len(f), 8):
    item = f[i:i+7]
    if item[0] == "#####" and item[-1] == ".....":
        locks.append(item)
    else:
        keys.append(item)

locks_converted = []
for lock in locks:
    locks_converted.append(convert(lock))

keys_converted = []
for key in keys:
    keys_converted.append(convert(key))
    
matches = 0

for lock in locks_converted:
    for key in keys_converted:
        matches += match(lock, key)

print(matches)