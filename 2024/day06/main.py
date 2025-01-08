with open("input.txt", 'r') as infile:
    grid = [
        list(line.strip())
        for line in infile
    ]

EMPTY   = '.'
WALL    = '#'
VISITED = 'X'

NROWS = len(grid)
NCOLS = len(grid[0])

guard_symbols = {
    '^' : [-1,  0],
    'v' : [+1,  0],
    '<' : [ 0, -1],
    '>' : [ 0, +1],
}


##### Part 1 #####

# Locate guard and determine their current direction
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in guard_symbols:
            pos = [i, j]
            vel = guard_symbols[grid[i][j]]
            # Mark guard's current position as 'visited'
            grid[pos[0]][pos[1]] = VISITED
            # Initialize count of visited cells
            num_visited = 1
            break
    else:
        continue
    break


# print('\n'.join(''.join(row) for row in grid))

while True:
    if (0 <= pos[0] + vel[0] < NROWS) and (0 <= pos[1] + vel[1] < NCOLS):
        # If guard hit wall, turn right; else move forward
        if grid[pos[0] + vel[0]][pos[1] + vel[1]] == WALL:
            vel[0], vel[1] = vel[1], -vel[0]
        else:
            pos[0] += vel[0]
            pos[1] += vel[1]
            # If not already visited, increment count and mark as visited
            if grid[pos[0]][pos[1]] == EMPTY:
                num_visited += 1
                grid[pos[0]][pos[1]] = VISITED
    else:
        break

# print()
# print('\n'.join(''.join(row) for row in grid))
print(f"Part 1: The guard will visit a total of {num_visited} unique positions.")


##### Part 2 #####

"""
If the guard reaches the same position with the same velocity, that can produce a loop?
"""
with open("test1.txt", 'r') as infile:
    grid = [
        list(line.strip())
        for line in infile
    ]

NROWS = len(grid)
NCOLS = len(grid[0])

# Locate guard and determine their current direction
pos = []
vel = []
visited = {}  # pos : {vel1, vel2, ...}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in guard_symbols:
            pos = [i, j]
            vel = guard_symbols[grid[i][j]]
            # Keep track of the velocity the guard had when visiting position
            visited[tuple(pos)] = {tuple(vel)}
            # Mark guard's current position as 'visited'
            grid[pos[0]][pos[1]] = VISITED
            break
    else:
        continue
    break

num_loops = 0
while (0 <= pos[0] + vel[0] < NROWS) and (0 <= pos[1] + vel[1] < NCOLS):
    print(pos, vel)
    print(visited)
    print()
    if grid[pos[0] + vel[0]][pos[1] + vel[1]] == WALL:  # if guard hits wall...
        vel[0], vel[1] = vel[1], -vel[0]  # ...turn right
        continue

    # Move forward
    pos[0] += vel[0]
    pos[1] += vel[1]
    
    # Keep track of the velocity the guard had when visiting position
    if tuple(pos) in visited:
        visited[tuple(pos)].add(tuple(vel))
    else:
        visited[tuple(pos)] = {tuple(vel)}

    # If already visted cell...
    if grid[pos[0]][pos[1]] == VISITED:
        # ...if guard was traveling -90deg from current trajectory...
        if (-vel[1], vel[0]) in visited[tuple(pos)]:
            num_loops += 1  # ...we've found a cycle
    else:
        # Mark cell as 'visited'
        grid[pos[0]][pos[1]] = VISITED

print(f"Part 2: The number of positions an obstacle can be placed to create a loop is {num_loops}.")