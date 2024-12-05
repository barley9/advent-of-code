with open("input.txt", 'r') as infile:
    locations = [
        [int(n) for n in line.strip().split('   ')]
        for line in infile.readlines()
    ]

locs1 = sorted(loc[0] for loc in locations)
locs2 = sorted(loc[1] for loc in locations)


##### PART 1 #####

distances = [abs(loc1 - loc2) for loc1, loc2 in zip(locs1, locs2)]

total = sum(distances)

print(f"Part 1: The total distance between the lists is {total}")


##### PART 2 #####

import collections

# counts1 = collections.Counter(locs1)
counts2 = collections.Counter(locs2)

score = 0
for loc in locs1:
    score += loc * counts2[loc]

print(f"Part 2: The similarity score of the two lists is {score}")