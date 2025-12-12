filename = 'test'
filename = 'testb'
filename = 'input'

with open(filename, 'r') as fd:
    f = fd.read()

lines = f.split("\n")[:-1]
array = []

for line in lines:
    array.append([i for i in line])
#print(array)

def xmas1(array, dim):
    counter = 0
    for i in range(1,dim):
        for c in range(dim):
            try:
                if array[i][c] == "A":
                    if array[i-1][c-1] == "M":
                        if array[i+1][c-1] == "M":
                            if array[i-1][c+1] == "S":
                                if array[i+1][c+1] == "S":
                                    counter += 1
            except:
                pass
    print(f"xmas1 {counter}")
    return counter

def xmas2(array, dim):
    counter = 0
    for i in range(1,dim):
        for c in range(dim):
            try:
                if array[i][c] == "A":
                    if array[i-1][c-1] == "S":
                        if array[i+1][c-1] == "S":
                            if array[i-1][c+1] == "M":
                                if array[i+1][c+1] == "M":
                                    counter += 1
            except:
                pass
    print(f"xmas2 {counter}")
    return counter

def xmas3(array, dim):
    counter = 0
    for i in range(1,dim):
        for c in range(dim):
            try:
                if array[i][c] == "A":
                    if array[i-1][c-1] == "M":
                        if array[i+1][c-1] == "S":
                            if array[i-1][c+1] == "M":
                                if array[i+1][c+1] == "S":
                                    counter += 1
            except:
                pass
    print(f"xmas3 {counter}")
    return counter

def xmas4(array, dim):
    counter = 0
    for i in range(1,dim):
        for c in range(dim):
            try:
                if array[i][c] == "A":
                    if array[i-1][c-1] == "S":
                        if array[i+1][c-1] == "M":
                            if array[i-1][c+1] == "S":
                                if array[i+1][c+1] == "M":
                                    counter += 1
            except:
                pass
    print(f"xmas4 {counter}")
    return counter






dim = len(array[0])
main = 0
main += xmas1(array, dim)
main += xmas2(array, dim)
main += xmas3(array, dim)
main += xmas4(array, dim)

print("FINAL:")
print(main)

