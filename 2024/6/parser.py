def load_grid(filename):
    """
    Load the grid from a text file and return it as a 2D array.
    """
    with open(filename, 'r') as file:
        lines = file.read().strip().split("\n")
    return [list(line) for line in lines]


def find_plus_positions(grid):
    """
    Find all positions of '+' in the grid.
    """
    positions = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "+":
                positions.append((i, j))
    return positions


def is_valid_rectangle(grid, top_left, top_right, bottom_left, bottom_right):
    """
    Check if a rectangle defined by four corners is valid.
    """
    # Check horizontal paths
    for j in range(top_left[1] + 1, top_right[1]):
        if grid[top_left[0]][j] not in ["-", "+"]:
            return False
    for j in range(bottom_left[1] + 1, bottom_right[1]):
        if grid[bottom_left[0]][j] not in ["-", "+"]:
            return False

    # Check vertical paths
    for i in range(top_left[0] + 1, bottom_left[0]):
        if grid[i][top_left[1]] not in ["|", "+"]:
            return False
    for i in range(top_right[0] + 1, bottom_right[0]):
        if grid[i][top_right[1]] not in ["|", "+"]:
            return False

    return True


def find_rectangles_for_plus(grid, positions):
    """
    Find all rectangles for each '+' in the grid.
    """
    rectangles = {}
    for top_left in positions:
        rectangles[top_left] = []
        for top_right in positions:
            if top_right[0] != top_left[0] or top_right[1] <= top_left[1]:
                continue  # Must be on the same row and to the right

            for bottom_left in positions:
                if bottom_left[1] != top_left[1] or bottom_left[0] <= top_left[0]:
                    continue  # Must be on the same column and below

                bottom_right = (bottom_left[0], top_right[1])
                if bottom_right in positions:
                    if is_valid_rectangle(grid, top_left, top_right, bottom_left, bottom_right):
                        rectangles[top_left].append((top_left, top_right, bottom_left, bottom_right))

    return rectangles


def print_rectangles(rectangles):
    """
    Print all rectangles found for each '+'.
    """
    for plus, rects in rectangles.items():
        #print(f"Rectangles for '+' at {plus}:")
        for rect in rects:
            print(f"  {rect}")


# Main execution
filename = "grid.txt"  # Replace with your file name
grid = load_grid(filename)

print("Initial Grid Loaded:")
for line in grid:
    print("".join(line))

# Find '+' positions
plus_positions = find_plus_positions(grid)

# Find rectangles for each '+'
rectangles = find_rectangles_for_plus(grid, plus_positions)

# Print rectangles
print("\nRectangles Found:")
print_rectangles(rectangles)
