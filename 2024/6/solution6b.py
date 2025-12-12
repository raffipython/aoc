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
        return True

    for i in range(x - 1, -1, -1):
        if array[i][y] == "#":
            array[i + 1][y] = "+"  # Mark the corner
            break
        if array[i][y] in ["x", ">"]:
            array[i][y] = "+"  # Mark intersection
        else:
            array[i][y] = "x"

    if i >= 0 and y + 1 < len(array[0]):
        array[i + 1][y + 1] = ">"  # Move guard to the new position
    return False


def down(array):
    x, y, symbol = locate_guard(array, ["v"])
    if x == -1:
        return True

    for i in range(x + 1, len(array)):
        if array[i][y] == "#":
            array[i - 1][y] = "+"  # Mark the corner
            break
        if array[i][y] in ["x", "<"]:
            array[i][y] = "+"  # Mark intersection
        else:
            array[i][y] = "x"

    if i < len(array) and y - 1 >= 0:
        array[i - 1][y - 1] = "<"
    return False


def left(array):
    x, y, symbol = locate_guard(array, ["<"])
    if x == -1:
        return True

    for j in range(y - 1, -1, -1):
        if array[x][j] == "#":
            array[x][j + 1] = "+"  # Mark the corner
            break
        if array[x][j] in ["x", "^"]:
            array[x][j] = "+"  # Mark intersection
        else:
            array[x][j] = "x"

    if j >= 0 and x - 1 >= 0:
        array[x - 1][j + 1] = "^"
    return False


def right(array):
    x, y, symbol = locate_guard(array, [">"])
    if x == -1:
        return True

    for j in range(y + 1, len(array[0])):
        if array[x][j] == "#":
            array[x][j - 1] = "+"  # Mark the corner
            break
        if array[x][j] in ["x", "v"]:
            array[x][j] = "+"  # Mark intersection
        else:
            array[x][j] = "x"

    if j < len(array[0]) and x + 1 < len(array):
        array[x + 1][j - 1] = "v"
    return False


# Main logic to process the grid
lines = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip().split("\n")
array = [list(line) for line in lines]

end = False

def loop():
    input("Press Enter to continue...")
    # Display the current state of the grid
    for line in array:
        print("".join(line))
    print("\n")

for _ in range(39):  # Allow 39 iterations
    if end:
        break
    end = up(array)
    loop()
    end = right(array)
    loop()
    end = down(array)
    loop()
    end = left(array)
    loop()

print("\n\nFinal Grid:")
# Display the final state of the grid
for line in array:
    print("".join(line))
