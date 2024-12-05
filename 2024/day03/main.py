import re


with open("input.txt", 'r') as infile:
    string = infile.read()


##### Part 1 #####

pattern = re.compile('mul\([0-9]{1,3},[0-9]{1,3}\)')
matches = re.findall(pattern, string)

total = 0
for match in matches:
    args = match.split(',')
    total += int(args[0][4:]) * int(args[1][:-1])

print(f"Part 1: The total of all the uncorrupted mul() instructions is {total}.")


##### Part 2 #####

pattern = re.compile('mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)')
matches = re.findall(pattern, string)

total = 0
enabled = True
for match in matches:
    if match[:3] == 'mul' and enabled:
        args = match.split(',')
        total += int(args[0][4:]) * int(args[1][:-1])
    elif match[:3] == 'do(':
        enabled = True
    elif match[:3] == 'don':
        enabled = False

print(f"Part 1: The total of all the uncorrupted and enabled mul() instructions is {total}.")

    