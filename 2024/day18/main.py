import numpy as np

with open("test1.txt", 'r') as infile:
    obstacles = [
        [
            int(n)
            for n in line.strip().split(',')
        ]
        for line in infile
    ]

nrows, ncols = max(ob[1] for ob in obstacles) + 1, max(ob[0] for ob in obstacles) + 1

grid = np.zeros(shape=(nrows, ncols), dtype=np.int16)

N = 12
for i in range(min(len(obstacles), N)):
    grid[obstacles[i][1], obstacles[i][0]] = 1

print('\n'.join(''.join('#' if n else '.' for n in row) for row in grid))

# TODO: research and implement A* search algorithm