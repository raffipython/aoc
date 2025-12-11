import os

# 6602278312187 is too high
# 17195321609 is too low
# 5346286649122 is right
 
i = 'input3'
#i = 'input2'
grid = []

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')
print(lines)

ops = []
counter = 0
prev = ""

for c in lines[4]:
    print("----")
    current = lines[4][counter]
    try:
        next = lines[4][counter+1]
    except:
        pass
    if current != " ":
        prev = current

    print(prev,current,next)



    if current == " ":
        ops.append(prev)
    else:
        ops.append(" ")


    counter += 1

print(ops)

with open("new", 'w') as fd:
    fd.write(lines[0])
    fd.write("\n")
    fd.write(lines[1])
    fd.write("\n")
    fd.write(lines[2])
    fd.write("\n")
    fd.write(lines[3])
    fd.write("\n")
    for i in ops:
        fd.write(i)











