import os

# 56777254206 too high
# 52316131093 right!

i = 'input'
#i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split(',')
#print(lines)

bad = []

def is_bad(i):
    l = len(str(i))

    if l == 1:
        return False
    if l == 2:
        if str(i)[0] == str(i)[1]:
            return True
    if l == 3:
        return False
    if l == 4:
        if str(i)[:2] == str(i)[2:]:
            return True
    if l == 5:
        return False
    if l == 6:
        # 22 22 22
        if str(i)[:2] == str(i)[2:4]:
            if str(i)[:2] == str(i)[4:]:
                if str(i)[:3] == str(i)[3:]:
                    return True
        # 222 222
        if str(i)[:3] == str(i)[3:]:
            return True  
    if l == 7:
        return False
    if l == 8:
        # 22 22 22 22 
        if str(i)[:2] == str(i)[2:4]:
            if str(i)[:2] == str(i)[4:6]:
                if str(i)[:2] == str(i)[6:]:
                    return True
        # 2222 2222 
        if str(i)[:4] == str(i)[4:]:
            return True
    if l == 9:
        return False
    if l == 10:
        # 22222 22222 
        if str(i)[:5] == str(i)[5:]:
            return True
        # 22 22 22 22 22
        if str(i)[:2] == str(i)[2:4]:
            if str(i)[:2] == str(i)[4:6]:
                if str(i)[:2] == str(i)[6:8]:
                    if str(i)[:2] == str(i)[8:]:
                        if str(i)[:5] == str(i)[5:]:
                            return True

    return False

for item in lines:
    #print('----')
    first = int(item.split("-")[0])
    last =  int(item.split("-")[1])
    #print(first)
    #print(last)
    #print()
    for i in range(first, last+1):
        #print(i)
        #print(is_bad(i))
        #print(f"z {len(str(i))}")
        if is_bad(i):
            bad.append(i)

print(bad)
total = 0
for i in bad:
    total += i
print(total)