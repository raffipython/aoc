import os
import math

i = 'input'
i = './input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
#print(lines)

x = []

def distance(a, b):
    aparts = a.split(",")
    ax = int(aparts[0])
    ay = int(aparts[1])
    az = int(aparts[2])
    bparts = b.split(",")
    bx = int(bparts[0])
    by = int(bparts[1])
    bz = int(bparts[2])
    return math.dist((ax, ay, az), (bx, by, bz))

shortest = 10000000

parts = []

for z in lines:
    for i in lines:
        if z != i:
            d = distance(z, i)
            if d < shortest:
                shortest = d
                print(f"{z} {i} {d}")
                
                
#print(shortest)

