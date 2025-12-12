def replace_corners_with_plus(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [row[:] for row in grid]  # Create a copy of the grid

    # Helper to check valid coordinates
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Iterate through the grid
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] in {"|", "-"}:  # Path cell
                # Check neighbors to detect corners
                has_vertical = (
                    (is_valid(x - 1, y) and grid[x - 1][y] == "|") or
                    (is_valid(x + 1, y) and grid[x + 1][y] == "|")
                )
                has_horizontal = (
                    (is_valid(x, y - 1) and grid[x][y - 1] == "-") or
                    (is_valid(x, y + 1) and grid[x][y + 1] == "-")
                )
                if has_vertical and has_horizontal:
                    new_grid[x][y] = "+"

    return new_grid


# Input Processing
filename = 'answer'  # Replace with your file
with open(filename, 'r') as fd:
    f = fd.read()

lines = f.split("\n")
grid = [list(line) for line in lines if line.strip()]

# Replace corners
new_grid = replace_corners_with_plus(grid)

# Output the updated grid
for line in new_grid:
    print("".join(line))

