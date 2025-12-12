filename = 'test'
filename = 'test1'
filename = 'input'

with open(filename, 'r') as fd:
    f = fd.read()

lines = f.split("\n")[:-1]
array = []

word = "XMAS"

for line in lines:
    array.append([i for i in line])
print(array)

def hor(array, w, dim):
    counter = 0
    for i in range(dim):
        for c in range(dim):
            try:
                if array[i][c] == w[0]:
                    if array[i][c+1] == w[1]:
                        if array[i][c+2] == w[2]:
                            if array[i][c+3] == w[3]:
                                counter += 1
            except:
                pass
    print(f"hor {counter}")
    return counter

def ver(array, w, dim):
    counter = 0
    for i in range(dim):
        for c in range(dim):
            try:
                if array[i][c] == w[0]:
                    if array[i+1][c] == w[1]:
                        if array[i+2][c] == w[2]:
                            if array[i+3][c] == w[3]:
                                counter += 1
            except:
                pass
    print(f"ver {counter}")
    return counter

def diag1(array, w, dim):
    counter = 0
    for i in range(dim):
        for c in range(dim):
            try:
                if array[i][c] == w[0]:
                    if array[i+1][c+1] == w[1]:
                        if array[i+2][c+2] == w[2]:
                            if array[i+3][c+3] == w[3]:
                                counter += 1
            except:
                pass
    print(f"di1 {counter}")
    return counter

def diag2(array, w, dim):
    counter = 0
    for i in range(dim):
        for c in range(3,dim):
            try:
                if array[i][c] == w[0]:
                    if array[i+1][c-1] == w[1]:
                        if array[i+2][c-2] == w[2]:
                            if array[i+3][c-3] == w[3]:
                                counter += 1
                                print(i,c)
                                print(array[i][c])
                                print(array[i+1][c-1])
                                print(array[i+2][c-2])
                                print(array[i+3][c-3])
            except:
                pass
    print(f"di2 {counter}")
    return counter

dim = len(array[0])
main = 0
main += hor(array, word, dim)
main += hor(array, word[::-1], dim)
main += ver(array, word, dim)
main += ver(array, word[::-1], dim)
main += diag1(array, word, dim)
main += diag1(array, word[::-1], dim)
main += diag2(array, word, dim)
main += diag2(array, word[::-1], dim)

print("FINAL:")
print(main)

