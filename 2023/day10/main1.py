# List of (dx, dy) connections for each pipe symbol
pipes = {
    '|': [( 1,  0), (-1,  0)],
    '-': [( 0,  1), ( 0, -1)],
    'L': [(-1,  0), ( 0,  1)],
    'J': [(-1,  0), ( 0, -1)],
    '7': [( 1,  0), ( 0, -1)],
    'F': [( 1,  0), ( 0,  1)],
    '.': [( 0,  0), ( 0,  0)],
    'S': [],
}

matrix = []

with open("input.txt", 'r') as infile:
    for line in infile:
        matrix.append([pipes[symbol] for symbol in line.split()[0]])

# Locate starting pipe and replace with correct connections, inferred from adjacent cells
start = ()
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if matrix[i][j] == []:
            start = (i, j)
            for (dy, dx) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # If adjacent cell is within bounds of matrix and connects back to starting cell...
                if (0 <= i + dy < len(matrix)) and \
                   (0 <= j + dx < len(row)) and \
                   any((dy + by == 0) and (dx + bx == 0) for (by, bx) in matrix[i + dy][j + dx]):
                        matrix[i][j].append((dy, dx))  # ...add connection to cell (i, j)
            break
    else:
        continue
    break

print("[")
for row in matrix:
    print("\t", row)
print("]")

print(start)

count = 0
loc = start
# Take first step manually because of branching path
seen = {start}
prev = loc
(dy, dx) = matrix[loc[0]][loc[1]][0]
loc = (loc[0] + dy, loc[1] + dx)
count += 1
while loc not in seen:
    seen.add(loc)

    # print(loc)
    # print(matrix[loc[0]][loc[1]])
    # print()

    # Make sure not to retrace our steps
    (dy, dx) = matrix[loc[0]][loc[1]][0]
    if (loc[0] + dy, loc[1] + dx) == prev:
        (dy, dx) = matrix[loc[0]][loc[1]][1]

    prev = loc
    loc = (loc[0] + dy, loc[1] + dx)
    count += 1

print(count // 2)
