import os
# 7299 is too high
# 6723 is too high
# 3797 is too low
# 6350 is bad
# 6219 is 
# 6126 is 

i = 'input'
i = 'input2'
#i = 'input3'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')

counter = 0
current = 50
print("The dial starts by pointing at 50.")
###############################################

for line in lines:
    direction = line[0]
    amount = int(line[1:])
    if direction == "L":
        #     10        50 
        if amount < current:
            current -= amount
        #     50        50
        elif amount == current:
            current -= amount
            counter += 1
        #     160       50
        elif amount > current: 
            rotations = int(amount / 100)
            print(f"rotations {rotations}")
            if rotations == 0:
                counter += 1
            
            counter += rotations
            current -= amount
            print(f"current counter after rotations (L) {counter}")
        else:
            pass
        current = current % 100
        #print(current)

    else:
        #print('problem here')
        #print(current)
        #print(amount)
        sum = amount + current
        #print(f"sum: {sum}")
        if sum < 100:
            current += amount
        elif sum == 100:
            current = 0
            counter += 1
        elif sum > 100:
            print(f"current: {current}")
            print(f"counter: {counter}")

            # could be 101 or 201...
            rotations = int(amount / 100)
            if current != 0:
                counter += 1
            counter += rotations
            #print(rotations)
            #print(f"current counter after rotations (R) {counter}")
            #print(current)
            current = sum
        current = current % 100
        #print(current)
        
    print(f"The dial is rotated {line} to point at {current}. COUNTER: {counter}")




       


###############################################
print(f"\n--------\nFinal counter is: {counter}")





