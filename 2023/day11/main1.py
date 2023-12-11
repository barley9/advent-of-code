image = []

with open("input.txt", 'r') as infile:
    for line in infile:
        image.append(list(line.strip()))

# print("[")
# for line in image:
#     print("\t", line)
# print("]")

# Expand image horizontally
for j in range(len(image[0]) - 1, -1, -1):
    if not any(image[i][j] == '#' for i in range(len(image))):
        for i in range(len(image)):
            image[i].insert(j, '.')

# Expand image vertically
for i in range(len(image) - 1, -1, -1):
    if '#' not in image[i]:
        image.insert(i, image[i])

print("[")
for line in image:
    print("\t", line)
print("]")

# Find positions of galaxies
pos = []
for i in range(len(image)):
    for j in range(len(image[i])):
        if image[i][j] == '#':
            pos.append((i, j))

# print(len(pos))

# Compute distances between pairs of galaxies
total = 0
for i in range(len(pos) - 1):
    for j in range(i + 1, len(pos)):
        (y1, x1) = pos[i]
        (y2, x2) = pos[j]
        total += abs(x2 - x1) + abs(y2 - y1)  # taxicab distance
        # print(
        #     i, j,
        #     pos[i], pos[j],
        #     abs(x2 - x1),
        #     abs(y2 - y1),
        #     abs(x2 - x1) + abs(y2 - y1)
        # )

print(total)