digits = set(chr(i) for i in range(ord('0'), ord('9') + 1))
map_names = [
    'seed',
    'soil',
    'fert',
    'watr',
    'lght',
    'temp',
    'hmdy',
    'locn',
]

maps = []
with open("test.txt", 'r') as infile:
    # Get list of seed numbers
    seeds = [int(n) for n in infile.readline().split(':')[1].split()]
    
    for _ in range(3):
        line = infile.readline()  # skip three lines

    # Get list of mappings [seed-to-soil, soil-to-fertilizer, ...]
    while line:
        maps.append([])
        while line and (line[0] in digits):  # get list of ranges
            maps[-1].append(tuple(int(n) for n in line.split()))
            line = infile.readline()

        for _ in range(2):
            line = infile.readline()  # skip two lines

map_func = lambda n, src, dst: n - src + dst  # maps source range to destination range

seeds = [seed for i in range(len(seeds) // 2) for seed in range(seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1])]

print(seeds, len(seeds))

# for i in range(len(seeds)):
#     print()
#     for j in range(len(maps)):
#         for dst, src, size in maps[j]:
#             if src <= seeds[i] < src + size:
#                 print(f"{map_names[j]} {seeds[i]} ==> {map_names[j + 1]} {map_func(seeds[i], src, dst)}")
#                 seeds[i] = map_func(seeds[i], src, dst)
#                 break
#         else:
#             print(f"{map_names[j]} {seeds[i]} ==> {map_names[j + 1]} {seeds[i]}")

# print("The lowest location number is", min(seeds))