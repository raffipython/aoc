import os

i = 'input'
i = 'input2'
#i = 'test2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
print(lines)

#################
grid = lines
global size
global answer
answer = grid

size = len(grid[0])
print(size)

def is_valid_edges(x, y):
    print('-------------')
    xedge = False
    yedge = False
    if x == 0 or x == (size - 1):
        xedge = True
    if y == 0 or y == (size - 1):
        yedge = True
    #if xedge:
    #    print("xedge")
    #if yedge:
    #    print("yedge")
    print(grid[x][y])

    # A B C
    # D   E
    # F G H

    if x == 0 and y == 0:
        print(grid[x][y+1],grid[x+1][y],grid[x+1][y+1])

    if x == 0 and y == size - 1:
        print(grid[x][y-1],grid[x+1][y-1],grid[x+1][y])

    if x == size - 1 and y == 0:
        print(grid[x-1][y],grid[x-1][y+1],grid[x][y+1])

    if x == size - 1 and y == size - 1:
        print(grid[x-1][y-1],grid[x-1][y],grid[x][y-1])

    


#is_valid_edges(0,0)
#is_valid_edges(0,9)
#is_valid_edges(9,0)
#is_valid_edges(9,8)

def checkaround(x, y):
    # A B C
    # D   E
    # F G H
    counter = 0
    a = grid[x-1][y-1]
    b = grid[x-1][y]
    c = grid[x-1][y+1]
    d = grid[x][y-1]
    e = grid[x][y+1]
    f = grid[x+1][y-1]
    g = grid[x+1][y]
    h = grid[x+1][y+1]
    print(a,b,c,d,e,f,g,h)
    for i in [a,b,c,d,e,f,g,h]:
        if i == "@":
            counter += 1
    print(counter) 



checkaround(1,1)


    #for line in lines[1:-1]:
    #for i in line[1:-1]:
        #print(i)
    #print(line[1:-1])
















