def add_corners(grid):
    """Preprocess the grid to replace corners with `+`."""
    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] in "|-":
                # Check if it forms a valid corner
                is_top_left = x > 0 and y > 0 and grid[x - 1][y] == "|" and grid[x][y - 1] == "-"
                is_top_right = x > 0 and y < cols - 1 and grid[x - 1][y] == "|" and grid[x][y + 1] == "-"
                is_bottom_left = x < rows - 1 and y > 0 and grid[x + 1][y] == "|" and grid[x][y - 1] == "-"
                is_bottom_right = x < rows - 1 and y < cols - 1 and grid[x + 1][y] == "|" and grid[x][y + 1] == "-"

                if is_top_left or is_top_right or is_bottom_left or is_bottom_right:
                    grid[x][y] = "+"  # Replace with corner marker

    return grid


def detect_rectangles(grid):
    """Detect all rectangular loops in the grid."""
    rows, cols = len(grid), len(grid[0])
    rectangles = []

    for x1 in range(rows):
        for y1 in range(cols):
            if grid[x1][y1] == "+":
                for x2 in range(x1 + 1, rows):
                    for y2 in range(y1 + 1, cols):
                        # Check if all four corners of the rectangle are `+`
                        if (
                            grid[x2][y1] == "+" and
                            grid[x1][y2] == "+" and
                            grid[x2][y2] == "+"
                        ):
                            # Validate horizontal and vertical edges
                            if (
                                all(grid[x1][j] in "-+" for j in range(y1, y2 + 1)) and
                                all(grid[x2][j] in "-+" for j in range(y1, y2 + 1)) and
                                all(grid[i][y1] in "|+" for i in range(x1, x2 + 1)) and
                                all(grid[i][y2] in "|+" for i in range(x1, x2 + 1))
                            ):
                                rectangles.append([(x1, y1), (x1, y2), (x2, y1), (x2, y2)])

    return rectangles


# Input Processing
filename = 'answer'  # Replace with your file
with open(filename, 'r') as fd:
    f = fd.read()

lines = f.split("\n")
grid = [list(line) for line in lines if line.strip()]

# Add corners
grid = add_corners(grid)

# Detect rectangles
rectangles = detect_rectangles(grid)

# Output the rectangles
print(f"Found {len(rectangles)} rectangles:")
for rectangle in rectangles:
    print(f"Rectangle corners: {rectangle}")

# Optionally print the updated grid with corners
print("\nUpdated Grid:")
for line in grid:
    print("".join(line))

