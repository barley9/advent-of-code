import collections

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

bag = collections.Counter({
    'red': 12,
    'green': 13,
    'blue': 14,
})
print(bag)
total = 0
for i, game in enumerate(games):
    alltrue = True
    for reveal in game:
        reveal = collections.Counter(reveal)
        print("\t", reveal)
        for color in ['red', 'green', 'blue']:
            try:
                alltrue *= (bag[color] >= reveal[color])
            except KeyError:
                pass
    if alltrue:
        total += i + 1
        print("\t\tpossible")
    else:
        print("\t\timpossible")

print(total)