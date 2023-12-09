with open("input.txt", 'r') as infile:
    histories = [[int(n) for n in line.split()] for line in infile]

predicted = []
for hist in histories:
    sequences = [hist]
    while not all(elem == 0 for elem in sequences[-1]):
        sequences.append([(sequences[-1][i + 1] - sequences[-1][i]) for i in range(len(sequences[-1]) - 1)])

    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
    
    predicted.append(sequences[0][-1])

print(sum(predicted))