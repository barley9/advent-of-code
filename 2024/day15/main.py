# char_map = {
#     '@' : 0,  # robot
#     '.' : 1,  # empty
#     'O' : 2,  # box
#     '#' : 3,  # wall
# }

velocity_map = {
    '^' : (-1,  0),
    'v' : (+1,  0),
    '>' : ( 0, +1),
    '<' : ( 0, -1),
}

with open("test2.txt", 'r') as infile:
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


##### Part 1 #####

print_grid(grid, robot)

for move in moves:
    print('\nmove:', move)
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
            if grid[to_check[0]][to_check[1]] != '#':
                outcome = 1
                break
            if grid[to_check[0]][to_check[1]] != '.':
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
    print_grid(grid, robot)