import os

i = 'input'
#i = 'input2'
#i = 'test2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
print(lines)

#################
global grid
global size
global answer
grid = lines
answer = [list(row) for row in grid]

size = len(grid[0])
print(size)
def checkaround(x, y):
    # A B C
    # D   E
    # F G H
    counter = 0
    edge = False

    if x == 0 or x == size - 1:
        edge = True
    if y == 0 or y == size - 1:
        edge = True

    if not edge:
        a = grid[x-1][y-1]
        b = grid[x-1][y]
        c = grid[x-1][y+1]
        d = grid[x][y-1]
        e = grid[x][y+1]
        f = grid[x+1][y-1]
        g = grid[x+1][y]
        h = grid[x+1][y+1]
        #print(a,b,c,d,e,f,g,h)
        for i in [a,b,c,d,e,f,g,h]:
            if i == "@":
                counter += 1
        if counter < 4:
            answer[x][y] = "x"
    else:
        # top line
        if x == 0:
            # left corner
            if y == 0:
                #a = grid[x-1][y-1]
                #b = grid[x-1][y]
                #c = grid[x-1][y+1]
                #d = grid[x][y-1]
                e = grid[x][y+1]
                #f = grid[x+1][y-1]
                g = grid[x+1][y]
                h = grid[x+1][y+1]
                #print(a,b,c,d,e,f,g,h)
                #print(e,g,h)
                for i in [e,g,h]:
                    if i == "@":
                        counter += 1
                if counter < 4:
                    answer[x][y] = "x"
            # right corner
            elif y == size - 1:
                #a = grid[x-1][y-1]
                #b = grid[x-1][y]
                #c = grid[x-1][y+1]
                d = grid[x][y-1]
                #e = grid[x][y+1]
                f = grid[x+1][y-1]
                g = grid[x+1][y]
                #h = grid[x+1][y+1]
                #print(a,b,c,d,e,f,g,h)
                #print(e,f,g)
                for i in [e,f,g]:
                    if i == "@":
                        counter += 1
                if counter < 4:
                    answer[x][y] = "x"
            else:
                #a = grid[x-1][y-1]
                #b = grid[x-1][y]
                #c = grid[x-1][y+1]
                d = grid[x][y-1]
                e = grid[x][y+1]
                f = grid[x+1][y-1]
                g = grid[x+1][y]
                h = grid[x+1][y+1]
                #print(a,b,c,d,e,f,g,h)
                #print(d,e,f,g,h)
                for i in [d,e,f,g,h]:
                    if i == "@":
                        counter += 1
                if counter < 4:
                    answer[x][y] = "x"
        # left
        elif x > 0 and x < size - 1 and y == 0:
            #a = grid[x-1][y-1]
            b = grid[x-1][y]
            c = grid[x-1][y+1]
            #d = grid[x][y-1]
            e = grid[x][y+1]
            #f = grid[x+1][y-1]
            g = grid[x+1][y]
            h = grid[x+1][y+1]
            #print(a,b,c,d,e,f,g,h)
            #print(e,f,g)
            for i in [b,c,e,g,h]:
                if i == "@":
                    counter += 1
            if counter < 4:
                answer[x][y] = "x"
        # right
        elif x > 0 and x < size - 1 and y == size - 1:
            a = grid[x-1][y-1]
            b = grid[x-1][y]
            #c = grid[x-1][y+1]
            d = grid[x][y-1]
            #e = grid[x][y+1]
            f = grid[x+1][y-1]
            g = grid[x+1][y]
            #h = grid[x+1][y+1]
            #print(a,b,c,d,e,f,g,h)
            #print(e,f,g)
            for i in [a,b,d,f,g]:
                if i == "@":
                    counter += 1
            if counter < 4:
                answer[x][y] = "x"
        # bottom
        elif x == size - 1:
            # left corner
            if y == 0:
                #a = grid[x-1][y-1]
                b = grid[x-1][y]
                c = grid[x-1][y+1]
                #d = grid[x][y-1]
                e = grid[x][y+1]
                #f = grid[x+1][y-1]
                #g = grid[x+1][y]
                #h = grid[x+1][y+1]
                #print(a,b,c,d,e,f,g,h)
                for i in [b,c,e]:
                    if i == "@":
                        counter += 1
                if counter < 4:
                    answer[x][y] = "x"
            # right corner
            elif y == size - 1:
                a = grid[x-1][y-1]
                b = grid[x-1][y]
                #c = grid[x-1][y+1]
                d = grid[x][y-1]
                #e = grid[x][y+1]
                #f = grid[x+1][y-1]
                #g = grid[x+1][y]
                #h = grid[x+1][y+1]
                #print(a,b,c,d,e,f,g,h)
                #print(e,f,g)
                for i in [a,b,d]:
                    if i == "@":
                        counter += 1
                if counter < 4:
                    answer[x][y] = "x"
            else:
                a = grid[x-1][y-1]
                b = grid[x-1][y]
                c = grid[x-1][y+1]
                d = grid[x][y-1]
                e = grid[x][y+1]
                #f = grid[x+1][y-1]
                #g = grid[x+1][y]
                #h = grid[x+1][y+1]
                #print(a,b,c,d,e,f,g,h)
                #print(d,e,f,g,h)
                for i in [a,b,c,d,e]:
                    if i == "@":
                        counter += 1
                if counter < 4:
                    answer[x][y] = "x"
    #print('-------')
    #for i in answer:
    #    print(i)

for x in range(size):
    for y in range(size):
        if grid[x][y] == "@":
            checkaround(x,y)
#print("-------")
total = 0
for answerline in answer:
    #print(answerline)
    for x in answerline:
        if x == "x":
            total+=1
print(total)
