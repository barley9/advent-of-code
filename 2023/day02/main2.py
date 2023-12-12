import collections
import math

with open("input.txt", 'r') as infile:
    games = [
        [
            {
                color.split()[1]: int(color.split()[0]) for color in reveal.split(', ')
            } for reveal in line.strip().split(': ')[1].split('; ')
        ] for line in infile
    ]

print("[")
for game in games:
    print("\t", game)
print("]")

total = 0
for i, game in enumerate(games):
    min_cubes = collections.Counter({
        'red': 0,
        'green': 0,
        'blue': 0
    })
    for reveal in game:
        reveal = collections.Counter(reveal)
        for color in ['red', 'green', 'blue']:
            min_cubes[color] = max(reveal[color], min_cubes[color])
    total += math.prod(min_cubes.values())

print(total)