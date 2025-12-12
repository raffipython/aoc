filename = "15/input"
#filename = "15/test"
#filename = "15/small"

with open(filename, 'r') as fd:
    f = fd.read()
    lines = f.split("\n")[:-1]

# Read map and directions
map_data = lines[:lines.index("")]
directions = "".join(lines[lines.index("") + 1:]).replace("\n", "")
array = [list(line) for line in map_data]

# Helper function to locate the robot
def locate_robot(array):
    """Locate the current position of the robot."""
    for x, row in enumerate(array):
        if "@" in row:
            return x, row.index("@")
    return -1, -1

# Helper function to locate all the boxes
def locate_boxes(array):
    """Locate the current position of the boxes."""
    boxes = []
    for x in range(len(array)):
        for y in range(len(array[x])):
            if array[x][y] == "O":
                boxes.append((x, y))
    return boxes

# Function to check if a chain of boxes can be pushed
def can_push_chain(array, x, y, dx, dy):
    """Check if a chain of boxes can be pushed."""
    while 0 <= x < len(array) and 0 <= y < len(array[0]):
        x, y = x + dx, y + dy
        if not (0 <= x < len(array) and 0 <= y < len(array[0])):
            return False  # Out of bounds
        if array[x][y] == "#":  # Wall encountered
            return False
        if array[x][y] == ".":  # Empty space found
            return True
        if array[x][y] == "O":
            continue  # Keep checking the chain
    return False  # No valid space found

# Function to move the robot and handle box movements
def move_robot_and_box(array, x, y, new_x, new_y, dx, dy):
    """Move the robot and push a box chain if valid."""
    if array[new_x][new_y] == "O":  # If there's a box, check the chain
        if can_push_chain(array, new_x, new_y, dx, dy):  # Validate the entire chain
            current_x, current_y = new_x, new_y
            box_positions = []
            while 0 <= current_x < len(array) and 0 <= current_y < len(array[0]) and array[current_x][current_y] == "O":
                box_positions.append((current_x, current_y))
                current_x, current_y = current_x + dx, current_y + dy
            for cx, cy in reversed(box_positions):
                nx, ny = cx + dx, cy + dy
                array[nx][ny] = "O"  # Move the box
                array[cx][cy] = "."  # Clear old position
            array[new_x][new_y] = "@"  # Move the robot
            array[x][y] = "."  # Clear old robot position
        else:
            return False  # Cannot push the chain, do nothing
    elif array[new_x][new_y] == ".":  # Move to an empty square
        array[new_x][new_y] = "@"  # Move the robot
        array[x][y] = "."  # Clear old robot position
    else:
        return False  # Cannot move into a wall or another box
    return True

# Function to move the robot
def move(array, direction):
    """Move the robot in the given direction."""
    x, y = locate_robot(array)
    if direction == "<":
        dx, dy = 0, -1
    elif direction == ">":
        dx, dy = 0, 1
    elif direction == "^":
        dx, dy = -1, 0
    elif direction == "v":
        dx, dy = 1, 0
    else:
        return

    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < len(array) and 0 <= new_y < len(array[0]) and array[new_x][new_y] != "#":
        move_robot_and_box(array, x, y, new_x, new_y, dx, dy)

# Process the directions and compare outputs
array = [list(row) for row in map_data]
for i, d in enumerate(directions):
    move(array, d)
    current_output = "\n".join("".join(row) for row in array)
    #print(f"Move {d} (Step {i + 1}):")
    #print(current_output)

boxes = locate_boxes(array)
total = 0
for box in boxes:
    total += ((100) * box[0] + box[1])
print(total)

