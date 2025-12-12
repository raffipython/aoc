filename = 'input.txt'
filename = 'test.txt'

with open(filename, 'r') as fd:
    f = fd.read()

lines = f.split("\n")[:-1]
array = [list(line) for line in lines]

for i in array:
    print(i)