from colorama import init, Fore, Style
init()

# RGB to ANSI 24-bit escape code function
def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

# RGB Color
r, g, b = 100, 200, 50  # Replace with your RGB values
color_code = rgb_to_ansi(r, g, b)

# Print with color

def locate_guard(array, guard_symbols):
    """Locate the current position of the guard."""
    for x, row in enumerate(array):
        for symbol in guard_symbols:
            if symbol in row:
                y = row.index(symbol)
                return x, y, symbol
    return -1, -1, None  # Guard not found



def up(array):
    x, y, symbol = locate_guard(array, ["^"])
    if x == -1:
        print("Guard '^' not found in the matrix.")
        return True

    print(f"Guard at RIGHT: {y+1}, DOWN: {x+1} moving up.")
    array[x][y] = "+"
    for i in range(x - 1, -1, -1):
        if array[i][y] == "#":
            break
        array[i][y] = "|"

    if i >= 0 and y + 1 < len(array[0]):
        array[i + 1][y + 1] = ">"
    return False


def down(array):
    x, y, symbol = locate_guard(array, ["v"])
    if x == -1:
        print("Guard 'v' not found in the matrix.")
        return True

    print(f"Guard at RIGHT: {y+1}, DOWN: {x+1} moving down.")
    array[x][y] = "+"
    for i in range(x + 1, len(array)):
        if array[i][y] == "#":
            break
        array[i][y] = "|"

    if i < len(array) and y - 1 >= 0:
        array[i - 1][y - 1] = "<"
    return False


def left(array):
    x, y, symbol = locate_guard(array, ["<"])
    if x == -1:
        print("Guard '<' not found in the matrix.")
        return True

    print(f"Guard at RIGHT: {y+1}, DOWN: {x+1} moving left.")
    array[x][y] = "+"
    for j in range(y - 1, -1, -1):
        if array[x][j] == "#":
            break
        array[x][j] = "-"

    if j >= 0 and x - 1 >= 0:
        array[x - 1][j + 1] = "^"
    return False


def right(array):
    x, y, symbol = locate_guard(array, [">"])
    if x == -1:
        print("Guard '>' not found in the matrix.")
        return True

    print(f"Guard at RIGHT: {y+1}, DOWN: {x+1} moving right.")
    array[x][y] = "+"
    for j in range(y + 1, len(array[0])):
        if array[x][j] == "#":
            break
        array[x][j] = "-"

    if j < len(array[0]) and x + 1 < len(array):
        array[x + 1][j - 1] = "v"
    return False


# Main logic to process the grid
filename = 'input'
filename = 'test'
with open(filename, 'r') as fd:
    f = fd.read()

lines = f.split("\n")[:-1]
array = [list(line) for line in lines]

end = False
import os
import time
counter = 0
### 38
for _ in range(40):  # Allow enough iterations for processing 1000
    # Print with color
    #print(f"{color_code}")

    if end:
        break
    end = up(array)
    ############
    os.system('clear')
    for line in array:
        print("".join(line))
        pass
    end = right(array)
    os.system('clear')
    for line in array:
        print("".join(line))
        pass
    end = down(array)
    os.system('clear')
    for line in array:
        print("".join(line))
        pass
    end = left(array)
    os.system('clear')
    for line in array:
        print("".join(line))
        pass
    #time.sleep(0.2)
    input()
    counter += 1
    print(counter)
    print(f"This is your colored text!{Style.RESET_ALL}")

# Display the final state of the grid
#for line in array:
#    print("".join(line))

#PLUS one
#$ python solution6a.py |grep -v Guard |grep -o x | wc -l

