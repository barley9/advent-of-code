games = []
with open("test1.txt", 'r') as infile:
    # for line in infile:
    #     games.append([])
    #     reveals = line.strip().split(': ')[1].split('; ')
    #     for reveal in reveals:
    #         games[-1].append([])
    #         for color in reveal.split(', '):
    #             games[-1][-1].append([0, 0, 0])
    #             num, col = color.split()
    #             if col == 'red':
    #                 games[-1][-1][0] = int(num)
    #             elif col == 'green':
    #                 games[-1][-1][1] = int(num)
    #             elif col == 'blue':
    #                 games[-1][-1][2] = int(num)

    games = [
        [
            {
                color.split()[1]: int(color.split()[0]) for color in reveal.split(', ')
            } for reveal in line.strip().split(': ')[1].split('; ')
        ] for line in infile
    ]

print("[")
for game in games:
    print("\t", game)
print("]")