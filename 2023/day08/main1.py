with open("input.txt", 'r') as infile:
    inst_map = {'L': 0, 'R': 1}
    insts = [inst_map[inst] for inst in infile.readline()[:-1]]

    for _ in range(2):
        line = infile.readline()  # skip 2 lines

    network = {}
    while line:
        node, _, lchild, rchild = line.split()
        children = (lchild[1:-1], rchild[:-1])
        network[node] = children

        line = infile.readline()

i = 0
node = 'AAA'
while node != 'ZZZ':
    node = network[node][insts[i % len(insts)]]
    i += 1

print(i)