import math
EPSILON = 10 ** -7

with open("input.txt", 'r') as infile:
    times  = [int(n) for n in infile.readline().split()[1:]]
    scores = [int(n) for n in infile.readline().split()[1:]]

wins = []
for t, s in zip(times, scores):
    print()
    r = math.sqrt(1 - 4 * s / (t * t))
    minh = t * (1 - r) / 2 + EPSILON
    maxh = t * (1 + r) / 2 - EPSILON
    print(minh, maxh)

    minh = math.ceil(minh)
    maxh = math.floor(maxh)
    print(minh, maxh)

    wins.append(maxh - minh + 1)
    print(maxh - minh + 1)

print(math.prod(wins))