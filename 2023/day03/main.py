digits = set(chr(i) for i in range(ord('0'), ord('9') + 1))

matrix = []  # matrix of numbers corresponding to each cell of input
symbols = []  # list of (row, col) positions of each symbol

with open("input.txt", 'r') as infile:
    for line in infile:
        matrix.append([])
        i = j = 0
        while i < len(line):
            if line[i] in digits:
                matrix[-1].extend([(None, set())] * (i - j))  # add empty cells before number
                j = i + 1
                while line[j] in digits:
                    j += 1
                # Store (number, set of cells number occupies) in each matrix cell number occupies
                matrix[-1].extend([(int(line[i:j]), set((len(matrix) - 1, k) for k in range(i, j)))] * (j - i))
                i = j - 1
            elif (line[i] != '.') and (line[i] != '\n'):
                symbols.append((len(matrix) - 1, i))
            i += 1

print("[")
for line in matrix:
    print("\t" + str([n[0] for n in line]))
print("]")

print(symbols)

total = 0
for (row, col) in symbols:
    to_search = {
        (row - 1, col - 1),
        (row - 1, col    ),
        (row - 1, col + 1),
        (row    , col - 1),
        (row    , col + 1),
        (row + 1, col - 1),
        (row + 1, col    ),
        (row + 1, col + 1),
    }

    print((row, col))

    while to_search:
        print("\t" + str(sorted(to_search)))

        # Pop (row, col) coordinate from to_search
        for r, c in to_search:
            break
        to_search.remove((r, c))

        # Attempt to lookup number in that cell
        try:
            num, positions = matrix[r][c]
        except IndexError:
            continue

        # If cell is empty
        if num is None:
            continue
        
        print(f"\tfound {num}")

        total += num
        to_search -= positions  # remove other instances of number from to_search

print(total)
