import math

import numpy as np

with open("input.txt", 'r') as infile:
    machines = [
        [
            [
                int(coord[2:]) for coord in param.split(': ')[1].split(', ')
            ]
            for param in machine.split('\n')
        ]
        for machine in infile.read().strip().split('\n\n')
    ]

# for machine in machines:
#     print(machine)


##### Part 1 #####

total_tokens = 0
for machine in machines:
    # print()
    ax, ay = machine[0]
    bx, by = machine[1]
    tx, ty = machine[2]
    det = ax * by - bx * ay
    if det == 0:
        continue  # there is no way to win the prize
    
    inverse = np.array([
        [ by, -bx],
        [-ay,  ax]
    ]) / det

    presses = inverse.dot([[tx], [ty]]).flatten()

    # print(presses)

    # If numbers of presses are integers...
    if all(math.isclose(p, round(p)) for p in list(presses.flatten())):
        total_tokens += round(3 * presses[0] + 1 * presses[1])
        # print(f"It will cost {round(3 * presses[0] + 1 * presses[1])} tokens to win the prize.")

print(f"In total, it will cost {total_tokens} tokens to win all possible prizes.")


##### Part 2 #####

offset = 10_000_000_000_000

total_tokens = 0
for machine in machines:
    ax, ay = machine[0]
    bx, by = machine[1]
    tx, ty = machine[2]
    det = ax * by - bx * ay
    
    if det == 0:
        continue  # there is no way to win the prize
    
    # inverse before reducing by the determinant
    pseudo_inverse = [
        [ by, -bx],
        [-ay,  ax]
    ]

    presses = [
        pseudo_inverse[0][0] * (tx + offset) + pseudo_inverse[0][1] * (ty + offset),
        pseudo_inverse[1][0] * (tx + offset) + pseudo_inverse[1][1] * (ty + offset),
    ]

    # Divide by determinant
    presses = [divmod(press, det) for press in presses]
    
    # If determinant divides evenly, add to tokens
    if all(r == 0 for q, r in presses):
        total_tokens += 3 * presses[0][0] + 1 * presses[1][0]

print(f"In total, it will cost {total_tokens} tokens to win all possible prizes.")