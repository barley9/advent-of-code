with open("test1.txt", 'r') as infile:
    rows = [
        [
            [run for run in line.split()[0].split('.') if run],
            tuple(int(n) for n in line.split()[1].split(','))
        ] for line in infile
    ]

print("[")
for row in rows:
    print("\t", row)
print("]")