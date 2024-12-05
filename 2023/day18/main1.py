with open("test1.txt", 'r') as infile:
    steps = [line.split() for line in infile.readlines()]

for i in range(len(steps)):
    steps[i][1] = int(steps[i][1])
    steps[i][2] = tuple(int(steps[i][2][2:-1][j:j + 2], 16) for j in range(0, len(steps[i][2][2:-1]), 2))

print("[")
for step in steps:
    print("\t", step)
print("]")