import os

# 6602278312187 is too high
# 17195321609 is too low
# 5346286649122 is right

# part 2
#10385316362219 too low

 
i = 'input'
i = 'input2'
i = 'new'
#i = 'input2test'

total = 0

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
#print(lines)
#print(lines[3])

counter = 0
part = []
goodparts = []
goodoprand = []
for c in lines[0]:
    a = lines[0][counter]
    b = lines[1][counter]
    c = lines[2][counter]
    d = lines[3][counter]
    x = lines[4][counter]
    
    #print(f"{a} {b} {c} {d} {x}")
    if a == " " and b == " " and c == " " and d == " " and x == " ":
        #print("----------------")
    
        subtotal = 0
        if len(part) > 2:
            if x == "*":
                subtotal = int(part[0]) * int(part[1]) * int(part[2])
            else:
                subtotal = int(part[0]) + int(part[1]) + int(part[2])

        #print(subtotal)
        #print(total)
        total += subtotal
        goodparts.append(part)
        
        part = []
        
    else:
        part.append(a + b + c + d)
    goodparts.append(x)
        #print(x)
        #print(part)
        
    counter += 1  
    




print("\nanswer")
total = 0

for i in goodparts:
    print(i)



print(total)
