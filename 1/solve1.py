import os
# 7299 is too high
# 6723 is too high
# 3797 is too low

with open('input2', 'r') as fd:
    f = fd.read()
    lines = f.split('\n')

counter = 0
current = 50

###############################################

for line in lines:
    print('----------------------')
    print(f"Counter is: {counter}")
    print(f"Current is: {current}")
    print(f"Item is:    {line}")
    direction = line[0]
    amount = int(line[1:])
    #print(direction)
    #print(amount)


    if direction == "L":
        current_zero = False
        if current == 0:
            current_zero = True
        else:
            current_zero = False

        if amount 

        current -= amount
        if amount > current:
            current = 100 + current
            #print(amount / 100)
            if not current_zero:
                counter += int(current / 100)  # current or amount
                counter += 1
            print(f"Counter is (L): {counter}")
        current = current % 100
        print(current)


    else:
        current_zero = False
        if current == 100:
            current_zero = True
        else:
            current_zero = False

        current += amount
        if current > 99:
            if not current_zero:
                counter += int(current / 100)
                counter += 1
            print(f"Counter is (R): {counter}")
        current = current % 100
        print(current)


###############################################
print(f"\n--------\nFinal counter is: {counter}")





