import operator


with open("input.txt", 'r') as infile:
    equations = []
    for line in infile.readlines():
        line = line.strip().split(' ')
        equations.append(
            [int(line[0][:-1])] + \
            [int(n) for n in line[1:]]
        )


##### Part 1 #####

ops = [operator.add, operator.mul]

total = 0
for eqn in equations:
    # print(eqn)
    target = eqn[0]
    # For every combination of add() and mul() operations...
    for i in range(2 ** (len(eqn) - 2)):
        operands = eqn[1:][::-1]
        # print('\t' + bin(i), operands, end=' ')
        operators = []
        mask = 1
        for shift in range(len(operands) - 1):
            if (mask << shift) & i:
                operators.append(ops[0])  # append add()
            else:
                operators.append(ops[1])  # append mul()
        # print('[' + ', '.join(('+' if op == operator.add else '*') for op in operators) + ']', end=' ')
        
        # Evaluate list of numbers/operators
        for j in range(len(operators)):
            operands.append(operators[j](operands.pop(), operands.pop()))
        # print(str(operands))

        if operands[0] == target:
            total += target
            break

print(f"Part 1: The total calibration result from the equations that might be true is {total}")


##### Part 2 #####

ops = [operator.add, operator.mul, lambda a, b: int(str(a) + str(b))]