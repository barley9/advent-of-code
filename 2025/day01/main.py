NUM_TICKS = 100

with open("test1.txt", 'r') as infile:
    commands = [
        [line[0], int(line[1:])]
        for line in infile
    ]

########## PART 1 ##########

position = 50
zeros_count = 0
for direction, distance in commands:
    if direction == 'R':
        position = (position + distance) % NUM_TICKS
    else:
        position = (position + NUM_TICKS - distance) % NUM_TICKS

    # print(f"command: {direction}{distance}, position: {position}")

    if position == 0:
        zeros_count += 1

print(f"The number of times the dial ended on '0' is {zeros_count}.")

########## PART 2 ##########
