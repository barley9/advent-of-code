import numpy as np

with open("test1.txt", 'r') as infile:
    codes = [
        list(line.strip())
        for line in infile
    ]


##### Part 1 #####

# Construct map from (start, target) to sequence of moves for numerical keypad
numpad = np.vstack((
    np.flipud(np.arange(1, 10).reshape((3, 3))),
    [['.', '0', 'A']]
))

numpad_keypos = {
    numpad[i,j] : (i, j)
    for i in range(numpad.shape[0])
    for j in range(numpad.shape[1])
}
del numpad_keypos['.']

numpad_paths = {}
for start in numpad.flatten():
    if start == '.':
        continue
    r, c = numpad_keypos[start]
    for target in numpad.flatten():
        if target == '.':
            continue
        i, j = numpad_keypos[target]
        numpad_paths[(start, target)] = ''
        if i - r > 0:
            numpad_paths[(start, target)] += 'v' * (i - r)
        else:
            numpad_paths[(start, target)] += '^' * (r - i)
        
        if j - c > 0:
            numpad_paths[(start, target)] += '>' * (j - c)
        else:
            numpad_paths[(start, target)] += '<' * (c - j)

# Construct map from (start, target) to sequence of moves for directional keypad
dirpad = np.array([
    ['.', '^', 'A'],
    ['<', 'v', '>'],
])

dirpad_keypos = {
    dirpad[i,j] : (i, j)
    for i in range(dirpad.shape[0])
    for j in range(dirpad.shape[1])
}
del dirpad_keypos['.']

dirpad_paths = {}
for start in dirpad.flatten():
    if start == '.':
        continue
    r, c = dirpad_keypos[start]
    for target in dirpad.flatten():
        if target == '.':
            continue
        i, j = dirpad_keypos[target]
        dirpad_paths[(start, target)] = ''
        
        if j - c > 0:
            dirpad_paths[(start, target)] += '>' * (j - c)
        else:
            dirpad_paths[(start, target)] += '<' * (c - j)

        if i - r > 0:
            dirpad_paths[(start, target)] += 'v' * (i - r)
        else:
            dirpad_paths[(start, target)] += '^' * (r - i)

def test_result(moves: str, start=(0, 2), keypad=dirpad) -> str:
    dirmap = {
        '^' : (-1,  0),
        'v' : (+1,  0),
        '<' : ( 0, -1),
        '>' : ( 0, +1),
    }

    pos = np.array(start)  # position of 'A' on directional keypad
    result = ''
    for move in moves:
        if move == 'A':
            result += keypad[pos[0], pos[1]]
        else:
            pos += dirmap[move]

    return result

# result = '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'
# print(result)
# for _ in range(2):
#     result = test_result(result)
#     print(result)
# result = test_result(result, start=(3, 2), keypad=numpad)
# print(result)


# import sys
# sys.exit(0)


# Construct movement codes
numerals = {chr(i) for i in range(ord('0'), ord('9') + 1)}
total = 0
for code0 in codes:
    print()
    print(len(code0), ''.join(code0))

    code1 = numpad_paths['A', code0[0]] + 'A'
    for i in range(len(code0) - 1):
        code1 += numpad_paths[(code0[i], code0[i + 1])] + 'A'
    print(len(code1), code1)

    code2 = dirpad_paths['A', code1[0]] + 'A'
    for i in range(len(code1) - 1):
        code2 += dirpad_paths[(code1[i], code1[i + 1])] + 'A'
    print(len(code2), code2)

    code3 = dirpad_paths['A', code2[0]] + 'A'
    for i in range(len(code2) - 1):
        code3 += dirpad_paths[(code2[i], code2[i + 1])] + 'A'
    print(len(code3), code3)

    print(''.join(code0), len(code3), int(''.join(n for n in code0 if n in numerals)))
    total += len(code3) * int(''.join(n for n in code0 if n in numerals))

print(f"Part 1: The sum of the complexities of the codes is {total}")