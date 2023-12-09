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

# Find all nodes that end in 'A' as starting nodes
nodes = []
for k in network.keys():
    if k[-1] == 'A':
        nodes.append(k)

# Find the cycle properties of each starting node
cycles = []
for node in nodes:
    i = 0
    loc = (node, i % len(insts))
    seen = {}
    goals = []
    while loc not in seen:
        # Add node to `seen` and store location in sequence
        seen[loc] = i  # store (node, i % len(insts)) : i
        if node[-1] == 'Z':
            goals.append(loc)  # if we found an endpoint 'xxZ', save its location

        # Follow instruction i % len(insts) to next node
        node = network[node][insts[loc[1]]]
        i += 1
        loc = (node, i % len(insts))  # must encounter again same node at same position in instructions
    
    cycles.append((seen[goals[0]], (i - loc[1])))

print(cycles)

# Find index which makes every cycle end on a node matching 'xxZ'
k = 0
node = nodes[k]
to_print = {cycles[k][0] + cycles[k][1] * j for j in range(10)}
for j in range(200_000):
    if j in to_print:
        print(node)
    node = network[node][insts[j % len(insts)]]
