import os
import ast
i = 'results2'
#i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('--')

for i in lines:
    #print('---------')
    #print(i)
    x = i.split("\n")
    op = x[1]
    items = x[2]
    print(op + items)



#print(lines)


