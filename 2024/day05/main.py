with open("input.txt", 'r') as infile:
    rules = []
    line = infile.readline().strip()
    while line:
        rules.append([int(n) for n in line.split('|')])
        line = infile.readline().strip()

    updates = [
        [int(n) for n in line.strip().split(',')]
        for line in infile.readlines()
    ]

# print(rules)
# print(updates)


##### Part 1 #####

follows = {}
for rule in rules:
    if rule[0] in follows:
        follows[rule[0]].add(rule[1])
    else:
        follows[rule[0]] = {rule[1]}
# print(follows)

valid = [True] * len(updates)
for i, update in enumerate(updates):
    seen = set()
    for n in update:
        if (n in follows) and (follows[n] & seen):  # if we've seen something that musn't precede `n`...
            valid[i] = False
            break
        seen.add(n)

total = sum(update[len(update) // 2] for v, update in zip(valid, updates) if v)

print(f"Part 1: The sum of the middle elements of the valid updates is {total}")


##### Part 2 #####

