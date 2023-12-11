image = []

with open("input.txt", 'r') as infile:
    for line in infile:
        image.append(list(line.strip()))

print("[")
for line in image:
    print("\t", line)
print("]")

# Find positions of empty columns
empty_cols = []
for j in range(len(image[0])):
    if not any(image[i][j] == '#' for i in range(len(image))):
        empty_cols.append(j)
print(empty_cols)

# Find positions of empty rows
empty_rows = []
for i in range(len(image)):
    if '#' not in image[i]:
        empty_rows.append(i)
print(empty_rows)

# Find positions of galaxies
galaxies = []
for i in range(len(image)):
    for j in range(len(image[i])):
        if image[i][j] == '#':
            galaxies.append((i, j))

# Compute distances between pairs of galaxies
expansion = 1_000_000  # factor to multiply empty rows/columns
total = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        (y1, x1) = galaxies[i]
        (y2, x2) = galaxies[j]
        total += abs(x2 - x1) + abs(y2 - y1)  # taxicab distance
        for row in empty_rows:
            if (y1 < row < y2) or (y2 < row < y1):
                total += expansion - 1
        for col in empty_cols:
            if (x1 < col < x2) or (x2 < col < x1):
                total += expansion - 1

print(total)