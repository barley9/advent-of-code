global height_map

ord0 = ord('0')
with open("test1.txt", 'r') as infile:
    height_map = [
        [ord(n) - ord0 for n in line.strip()]
        for line in infile
    ]

nrows, ncols = len(height_map), len(height_map[0])

print("[" + '\n '.join(str(row) for row in height_map) + "]")

# Start by locating all possible trail heads
trail_heads = []
for i in range(len(height_map)):
    for j in range(len(height_map[i])):
        if height_map[i][j] == 0:
            trail_heads.append((i, j))

def get_neighbors(pos: tuple) -> list:
    """Helper function to get all valid neighboring positions"""
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


##### Part 1 #####

def count_reachable_tops(pos: tuple, height=0, seen=set()) -> int:
    global height_map

    candidates = set(
        cand
        for cand in get_neighbors(pos)
        if height_map[cand[0]][cand[1]] == height + 1
    ) - seen

    for cand in candidates:
        seen.add(cand)

    if height == 8:
        return len(candidates)
    else:
        return sum(
            count_reachable_tops(cand, height + 1, seen)
            for cand in candidates
        )

# print([count_reachable_tops(head, 0, set()) for head in trail_heads])

total = sum(
    count_reachable_tops(head, 0, set())
    for head in trail_heads
)
print(f"Part 1: The sum of scores of all the trailheads is {total}")


##### Part 2: #####
