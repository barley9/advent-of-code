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

# Find all nodes that end in 'A'
nodes = []
for k in network.keys():
    if k[-1] == 'A':
        nodes.append(k)


# Find cycles(?)
i = 0
node = nodes[0]
seen = {}
goals = []
loc = (node, i % len(insts))
while loc not in seen:
    print(node)
    seen[loc] = i  # store (node, i % len(insts)) : i
    if node[-1] == 'Z':
        goals.append(loc)
    node = network[node][insts[loc[1]]]
    
    i += 1
    loc = (node, i % len(insts))  # must encounter again same node at same position in instructions
print(node)
print(seen)
print(i, loc, i - seen[loc])
print(goals, seen[goals[0]])


# # Follow all nodes in network until all end in 'Z' (NOTE: not fast enough)
# i = 0
# while not all(node[-1] == 'Z' for node in nodes):
#     # print(nodes)
#     for j in range(len(nodes)):
#         nodes[j] = network[nodes[j]][insts[i % len(insts)]]
#     i += 1

# print(nodes)
# print(i)