filename = "14/one"
filename = "14/test"
filename = "14/input"

with open(filename, 'r') as fd:
    f = fd.read()
    robot_lines = f.split("\n")[:-1]

X = 101 #11 # 101
Y = 103 #7  # 103

def draw_grid(X, Y):
    """
    Creates an empty grid initialized with zeros.
    """
    return [[0 for _ in range(X)] for _ in range(Y)]

def print_grid(grid):
    """
    Prints the grid, replacing zeros with dots for readability.
    """
    for row in grid:
        print("".join(str(cell) if cell > 0 else "." for cell in row))

def place_robots(grid, robots):
    """
    Places robots on the grid by incrementing the cell for each robot's position.
    """
    for robot in robots.values():
        x, y = robot[0]
        grid[y][x] += 1

def move_robots(robots, X, Y):
    """
    Updates robot positions based on their velocities.
    Wraps positions around the grid boundaries.
    """
    for robot_id, data in robots.items():
        (x, y), (vx, vy) = data
        new_x = (x + vx) % X
        new_y = (y + vy) % Y
        robots[robot_id] = [(new_x, new_y), (vx, vy)]

def simulate(seconds, X, Y, robots):
    """
    Simulates the movement of robots over a given number of seconds.
    Prints the grid state after each second.
    """
    for second in range(seconds + 1):
        grid = draw_grid(X, Y)  # Reset the grid
        place_robots(grid, robots)  # Place robots on the grid

        if second == 0:
            print("Initial state:")
        else:
            print(f"After {second} second{'s' if second > 1 else ''}:")

        print_grid(grid)
        print()

        move_robots(robots, X, Y)  # Move robots for the next second
    
    print("\n")
    safety(grid)

def safety(grid):
    print_grid(grid)
    print()
    #print(len(grid))
    #print(len(grid[0]))
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    
    for i in grid[:int(len(grid)/2)]:
        index = int(len(grid[0])/2)
        for q in i[:index]:
            q1 += q
        
        for q in i[index+1:]:
            q2 += q

    print("\n")

    for i in grid[int(len(grid)/2)+1:]:
        index = int(len(grid[0])/2)
        for q in i[:index]:
            q3 += q
        
        for q in i[index+1:]:
            q4 += q


    print(f"Q1= {q1}")
    print(f"Q2= {q2}")
    print(f"Q3= {q3}")
    print(f"Q4= {q4}")
    print(f"SAFETY: {q1*q2*q3*q4}")

# Initialize robots
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
    
    robots.update({counter: [(locationx, locationy), (velocityx, velocityy)]})
    counter += 1

# Simulate robot movement for 100 seconds
simulate(100, X, Y, robots)



