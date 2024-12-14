with open("input.txt", 'r') as infile:
    robots = [
        [
            [int(n) for n in vec[2:].split(',')]
            for vec in line.strip().split(' ')
        ]
        for line in infile
    ]

nrows = max(robot[0][1] for robot in robots) + 1
ncols = max(robot[0][0] for robot in robots) + 1

def print_robots(robots: list) -> None:
    import collections
    positions = collections.Counter(tuple(robot[0]) for robot in robots)
    result = ''
    for i in range(nrows):
        result += ''.join(f'{positions[(j, i)]}' if positions[(j, i)] > 0 else '.' for j in range(ncols)) + '\n'
    print(result)

seconds = 100
for _ in range(seconds):
    for i, (pos, vel) in enumerate(robots):
        robots[i][0] = [
            (pos[0] + vel[0] + ncols) % ncols,
            (pos[1] + vel[1] + nrows) % nrows
        ]

# print(nrows, ncols)
# for pos, vel in robots:
#     print(f"pos = {pos}, vel = {vel}")
# print_robots(robots)

quadrant_counts = [0] * 4
for pos, vel in robots:
    if pos[0] < ncols / 2 - 1:
        if pos[1] < nrows / 2 - 1:
            quadrant_counts[0] += 1
        elif pos[1] > nrows / 2:
            quadrant_counts[2] += 1
    elif pos[0] > ncols / 2:
        if pos[1] < nrows / 2 - 1:
            quadrant_counts[1] += 1
        elif pos[1] > nrows / 2:
            quadrant_counts[3] += 1

# print(quadrant_counts)

import math
print(f"Part 1: The safety factor after {seconds} seconds is {math.prod(quadrant_counts)}.")


##### Part 2 #####

solution = 8159

"""
Strategy:
After viewing thousands of printouts of the robots' positions, something
suspicious stood out. Rarely, it appeared as though a greater-than-average
number of robots were concentrated within certain position 'bands'. While the
frequency of these anomalies appeared to be random, the horizontal and vertical
positions of these 'overfull bands' seemed to be consistent. I then started 
printing out only those configurations where the robots were concentrated in
one of these bands, et voila! The tree first appeared after 8159 iterations.
"""

# Reload pristine copy of `robots`
with open("input.txt", 'r') as infile:
    robots = [
        [
            [int(n) for n in vec[2:].split(',')]
            for vec in line.strip().split(' ')
        ]
        for line in infile
    ]

nrows = max(robot[0][1] for robot in robots) + 1
ncols = max(robot[0][0] for robot in robots) + 1

# Iterate forward
for k in range(solution):
    for i in range(len(robots)):
        robots[i][0][0] = (robots[i][0][0] + robots[i][1][0]) % ncols
        robots[i][0][1] = (robots[i][0][1] + robots[i][1][1]) % nrows

print_robots(robots)
print(f"Part 2: The easter egg first appears after {solution} seconds.")


##### BREAK #####
import sys
sys.exit(0)

# The code used to locate the solution
import time

for k in range(1_000_000):  # arbitrary large number
    if sum(35 < robot[0][1] < 68 for robot in robots) > (0.4 * len(robots)) and sum(22 < robot[0][0] < 54 for robot in robots) > (0.4 * len(robots)):
        positions = set(tuple(robot[0]) for robot in robots)

        result = f'elapsed: {k}\n'
        for i in range(nrows):
            result += ''.join('#' if (j, i) in positions else ' ' for j in range(ncols)) + '\n'
        print(result)

        time.sleep(10 / 1000)

    for i in range(len(robots)):
        robots[i][0][0] = (robots[i][0][0] + robots[i][1][0]) % ncols
        robots[i][0][1] = (robots[i][0][1] + robots[i][1][1]) % nrows