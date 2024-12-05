import re

import numpy as np


with open("input.txt", 'r') as infile:
    puzzle = np.array([
        list(line.strip())
        for line in infile
    ])

# print(puzzle)


##### Part 1 #####

pattern = re.compile('(?=(XMAS|SAMX))')

total = 0
for row in puzzle:
    total += len(re.findall(pattern, ''.join(row)))
for col in puzzle.T:
    total += len(re.findall(pattern, ''.join(col)))
for offset in range(-(puzzle.shape[0] - 4), puzzle.shape[1] - 4 + 1):
    total += len(re.findall(pattern, ''.join(np.diagonal(puzzle, offset))))
for offset in range(-(puzzle.shape[0] - 4), puzzle.shape[1] - 4 + 1):
    total += len(re.findall(pattern, ''.join(np.diagonal(np.flipud(puzzle), offset))))

print(f"Part 1: There are {total} occurences of the string 'XMAS' in the wordsearch.")


##### Part 2 #####

mask = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
]).astype(bool)

patterns = [
    np.array([['M', '.', 'M'],
              ['.', 'A', '.'],
              ['S', '.', 'S']]),
    np.array([['S', '.', 'M'],
              ['.', 'A', '.'],
              ['S', '.', 'M']]),
    np.array([['S', '.', 'S'],
              ['.', 'A', '.'],
              ['M', '.', 'M']]),
    np.array([['M', '.', 'S'],
              ['.', 'A', '.'],
              ['M', '.', 'S']]),
]

total = 0
for row in range(puzzle.shape[0] - 3 + 1):
    for col in range(puzzle.shape[1] - 3 + 1):
        region = np.where(mask, puzzle[row:row + 3,col:col + 3], '.')
        if any(np.all(region == pattern) for pattern in patterns):
            total += 1

print(f"Part 2: There are {total} occurences of an X-MAS in the puzzle.")