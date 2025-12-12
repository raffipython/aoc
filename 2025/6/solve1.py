import os

# 6602278312187 is too high
# 17195321609 is too low
# 17195321609
# 5346286649122 
 
i = 'input'
#i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
print(lines)

a = lines[0].split()
b = lines[1].split()
c = lines[2].split()
d = lines[3].split()
z = lines[4].split()

total = 0
for i in range(len(a)):
    #print(i)
    print("----")
    aa = int(a[i])  
    bb = int(b[i]) 
    cc = int(c[i])
    dd = int(d[i])
    zz = z[i]
    print(f"{aa} {zz} {bb} {zz} {cc} {zz} {dd}")
    if zz == "+":
        t = aa + bb + cc + dd
        print(t)
        total += t
    else:
        t = aa * bb * cc * dd
        print(t)
        total += t
print("\nanswer")
print(total)

