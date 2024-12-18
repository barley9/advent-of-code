velocity_map = {
    '^' : (-1,  0),
    'v' : (+1,  0),
    '>' : ( 0, +1),
    '<' : ( 0, -1),
}

##### Part 1 #####

with open("input.txt", 'r') as infile:
    grid, moves = infile.read().split('\n\n')

grid = [list(row) for row in grid.split('\n')]
moves = [velocity_map[sym] for sym in moves if sym != '\n']
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == '@':
            robot = [row, col]
grid[robot[0]][robot[1]] = '.'

nrows, ncols = len(grid), len(grid[0])

def print_grid(grid: list, robot: list) -> None:
    global nrows, ncols

    result = '\n'.join(''.join(row) for row in grid)
    print('robot:', robot)
    print(result[:(ncols + 1) * robot[0] + robot[1]] + '@' + result[(ncols + 1) * robot[0] + robot[1] + 1:])

# print_grid(grid, robot)

for move in moves:
    if not ((0 <= robot[0] + move[0] < nrows) and (0 <= robot[1] + move[1] < ncols)):
        pass  # robot is trying to exit the grid; do nothing
    elif grid[robot[0] + move[0]][robot[1] + move[1]] == '.':
        robot[0] += move[0]
        robot[1] += move[1]
    elif grid[robot[0] + move[0]][robot[1] + move[1]] == 'O':
        to_check = [robot[0] + 2 * move[0], robot[1] + 2 * move[1]]
        outcome = None
        while True:
            if not ((0 <= to_check[0] < nrows) and (0 <= to_check[1] < ncols)):
                outcome = 0
                break
            elif grid[to_check[0]][to_check[1]] == '#':
                outcome = 1
                break
            elif grid[to_check[0]][to_check[1]] == '.':
                outcome = 2
                break
            to_check[0] += move[0]
            to_check[1] += move[1]
        if outcome == 2:
            # move box into available empty space
            grid[to_check[0]][to_check[1]] = 'O'
            # remove box where robot is attempting to move
            grid[robot[0] + move[0]][robot[1] + move[1]] = '.'
            # move robot
            robot[0] += move[0]
            robot[1] += move[1]
    elif grid[robot[0] + move[0]][robot[1] + move[1]] == '#':
        pass  # robot is trying to push a wall; do nothing

# print_grid(grid, robot)

total_score = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 'O':
            total_score += 100 * row + col

print(f"Part 1: The sum of the boxes' GPS coordinates is {total_score}")


##### Part 2 #####

with open("test1.txt", 'r') as infile:
    unscaled_grid, moves = infile.read().split('\n\n')
    
# Map move symbols to move vectors
moves = [velocity_map[sym] for sym in moves if sym != '\n']

# Scale up grid
unscaled_grid = [
    list(row)
    for row in unscaled_grid.split('\n')
]
grid = [
    [None] * (2 * len(unscaled_grid[i]))
    for i in range(len(unscaled_grid))
]
robot = [None, None]
for i in range(len(unscaled_grid)):
    for j in range(len(unscaled_grid[i])):
        if unscaled_grid[i][j] == '#':
            grid[i][2 * j] = '#'
            grid[i][2 * j + 1] = '#'
        elif unscaled_grid[i][j] == '.':
            grid[i][2 * j] = '.'
            grid[i][2 * j + 1] = '.'
        elif unscaled_grid[i][j] == 'O':
            grid[i][2 * j] = '['
            grid[i][2 * j + 1] = ']'
        elif unscaled_grid[i][j] == '@':
            grid[i][2 * j] = '.'
            grid[i][2 * j + 1] = '.'
            robot[0] = i
            robot[1] = 2 * j

nrows, ncols = len(grid), len(grid[0])

print_grid(grid, robot)

for move in moves:
    if not ((0 <= robot[0] + move[0] < nrows) and (0 <= robot[1] + move[1] < ncols)):
        pass  # robot is trying to exit the grid; do nothing
    elif grid[robot[0] + move[0]][robot[1] + move[1]] == '#':
        pass  # robot is trying to push a wall; do nothing
    elif grid[robot[0] + move[0]][robot[1] + move[1]] == '.':
        robot[0] += move[0]
        robot[1] += move[1]
    elif grid[robot[0] + move[0]][robot[1] + move[1]] == '[':
        pass
    elif grid[robot[0] + move[0]][robot[1] + move[1]] == ']':
        pass