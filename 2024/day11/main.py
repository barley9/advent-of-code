with open("input.txt", 'r') as infile:
    arrangement = [int(n) for n in infile.readlines()[0].strip().split(' ')]


##### Part 1 #####

global length
length = len(arrangement)

class LLNode():
    """Simple linked list node class"""
    def __init__(self, val: int=None, next: 'LLNode'=None):
        self.val = val
        self.next = next

def to_string(head: LLNode) -> str:
    result = '['
    current = head
    while current:
        result += str(current.val) + ', '
        current = current.next
    return result[:-2] + ']'

def blink_next(node: LLNode) -> LLNode:
    """Applies a `blink` transformation to the `node`s next node"""
    global length
    current = node.next
    s = str(current.val)
    if current.val == 0:
        current.val = 1
        return current
    elif not len(s) & 1:
        current.val = int(s[:len(s) // 2])
        right = LLNode(
            val=int(s[len(s) // 2:]),
            next=current.next
        )
        current.next = right
        length += 1
        return right
    else:
        current.val *= 2024
        return current

header = LLNode()
current = header
for val in arrangement:
    current.next = LLNode()
    current.next.val = val
    current = current.next

# print(arrangement)
# print(to_string(header), length)

N = 25
for _ in range(N):
    current = header
    while current.next:
        current = blink_next(current)
    # print(to_string(header), length)

print(f"Part 1: The number of nodes after {N} blinks will be {length}.")


##### Part 2 #####

"""
Optimization strategy brainstorm:
The stones, once created, don't interact with one another. Each is an island
unto itself. Therefore, it doesn't matter if we insert new nodes in the
"correct" position or just append them to the end. Also, many calculations are
repeated if we have multiple stones with the same label number.
"""

import math
import collections
import functools

def digits_count(n: int) -> int:
    if n == 0:
        return 1
    else:
        return int(math.log10(n)) + 1

@functools.lru_cache(maxsize=None)
def blink(n: int) -> tuple:
    if n == 0:
        return (1,)
    elif digits_count(n) & 1:
        return (n * 2024,)
    else:
        s = str(n)
        return (
            int(s[:len(s) // 2]),
            int(s[len(s) // 2:])
        )

stones = collections.Counter(arrangement)

N = 75
for _ in range(N):
    for label, count in list(stones.items()):
        new_stones = blink(label)
        # print(label, count, new_stones, stones)
        stones[label] -= count
        for val in new_stones:
            stones[val] += count
    # print(list(stones.elements()), stones.total(), len(stones))

print(f"Part 2: The number of stones after {N} blinks will be {stones.total()}.")
# print(blink.cache_info())


##### Just for fun #####

import matplotlib.pyplot as plt

stones = collections.Counter(arrangement)

N = 500
totals = [stones.total()]
for _ in range(N):
    for label, count in list(stones.items()):
        new_stones = blink(label)
        # print(label, count, new_stones, stones)
        stones[label] -= count
        for val in new_stones:
            stones[val] += count
    totals.append(float(stones.total()))

fig, ax = plt.subplots(1, 1)
ax.set_yscale("log")
ax.plot(list(range(N + 1)), totals)
ax.set_xlabel("number of iterations")
ax.set_ylabel("number of stones")
ax.grid(True)
plt.show()

# From the graph, it is clear that the number of stones is an exponentially
# growing sequence. Specifically, it seems to be growing approximately
# according to $y = 6.34234 e^{0.418015 x}$. There is likely more that could be
# learned about this sequence.