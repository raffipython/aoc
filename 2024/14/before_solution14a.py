from pprint import pprint as pp
filename = "14/test"
with open(filename, 'r') as fd:
    f = fd.read()
    robot_lines = f.split("\n")[:-1]

X = 11
Y = 7
grid = []

def draw_grid(X, Y):
    grid = []
    for y in range(Y):
        xx = []
        for x in range(X): 
            xx.append(0)
        grid.append(xx)
    return grid

def print_grid(grid):
    for x in grid:
        for y in x:
            print(str(y), end="")
        print()

def place_robots(grid, robots):
    for robot in robots.keys():
        x, y = robots.get(robot)[0]
        grid[y][x] += 1
    return grid


grid = draw_grid(X, Y)
robots = {}
counter = 1
for line in robot_lines:
    parts = line.split(" ")
    location = parts[0].split("=")[1]
    locationx = int(location.split(",")[0])
    locationy = int(location.split(",")[1])

    velocity = parts[1].split("=")[1]
    velocityx = int(velocity.split(",")[0])
    velocityy = int(velocity.split(",")[1])
    
    robots.update({counter:[(locationx, locationy), (velocityx, velocityy)]})
    counter += 1

place_robots(grid, robots)
print_grid(grid)
print("\n\n")




