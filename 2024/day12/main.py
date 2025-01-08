orda = ord('A')
with open("test3.txt", 'r') as infile:
    grid = [
        [ord(c) - orda for c in line.strip()]
        for line in infile
    ]

global nrows, ncols
nrows, ncols = len(grid), len(grid[0])

print("[" + '\n '.join(str(row) for row in grid) + "]")


##### Part 1 #####

def get_neighbors(pos: tuple) -> list:
    """Helper function to get all valid neighboring positions"""
    global nrows, ncols

    row, col = pos
    result = []
    if row > 0:
        result.append((row - 1, col))
    if row < nrows - 1:
        result.append((row + 1, col))
    if col > 0:
        result.append((row, col - 1))
    if col < ncols - 1:
        result.append((row, col + 1))
    return result

# This is wrong. If there are multiple regions with the same crop ID but
# different perimeters/area, this will overcount. TODO: How to fix this?
# Perhaps flood-fill algorithm?
area = [0] * 26
perimeter = [0] * 26
for row in range(nrows):
    for col in range(ncols):
        crop = grid[row][col]
        area[crop] += 1
        neighbors = get_neighbors((row, col))
        perimeter[crop] += sum(crop != grid[i][j] for i, j in neighbors)
        perimeter[crop] += 4 - len(neighbors)  # fencing for edge of grid

for i in range(len(area)):
    if area[i] > 0:
        print(chr(i + orda), area[i], perimeter[i])