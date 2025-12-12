filename = "11/input"
with open(filename, 'r') as fd:
    f = fd.read().split()

#print(f)
#print()

#first applicable rule in this list

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.

# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
#    The left  half of the digits are engraved on the new left stone, and 
#    the right half of the digits are engraved on the new right stone. 
#    (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

# If none of the other rules apply, the stone is replaced by a new stone; 
#    the old stone's number multiplied by 2024 is engraved on the new stone.

def zero_apply(item):
    if int(item) == 0:
        return True
    
def zero(item):
    if int(item) == 0:
        return "1"

def even_apply(item):
    if len(item) % 2 == 0:
        return True

def even(item):
    left = str(item[:int(len(item)/2)]).lstrip("0")
    right = str(item[int(len(item)/2):]).lstrip("0")
    if not right:
        right = "0" 
    return [left, right]


def yep(item):
    return str(int(item) * 2024)

def fix(array):
    temp_array = []
    for i in array:
        if not isinstance(i, list):
            temp_array.append(i)
        else:
            for x in i:
                temp_array.append(x)
    return temp_array

def blinker(array):
    temp_array = []
    for item in array:
        if zero_apply(item):
            temp_array.append(zero(item))
        elif even_apply(item):
            temp_array.append(even(item))
        else:
            temp_array.append(yep(item))

    return temp_array

blinks = 75
# 196445 too high!
# 191690 worked!!!
from itertools import chain
array = f
for i in range(blinks):
    array = blinker(array)
    #print(array)
    array = fix(array)
    print(f"\nAFTER BLINK {i+1}")
    #print(array)
    print(f"The length is {len(array)}")

print("\n\nINITIAL")
print(f)
