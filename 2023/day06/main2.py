import math

EPSILON = 10 ** -7

with open("input.txt", 'r') as infile:
    time  = int(''.join(n for n in infile.readline().split()[1:]))
    score = int(''.join(n for n in infile.readline().split()[1:]))
print(time, score)

r = math.sqrt(1 - 4 * score / (time * time))
minh = time * (1 - r) / 2 + EPSILON
maxh = time * (1 + r) / 2 - EPSILON
print(minh, maxh)

minh = math.ceil(minh)
maxh = math.floor(maxh)
print(minh, maxh)

print(maxh - minh + 1)