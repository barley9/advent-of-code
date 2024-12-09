with open("test1.txt", 'r') as infile:
    disk_map = infile.read().strip()


##### Part 1 #####

# Construct file system as a list
ord0 = ord('0')
file_system = []
j = 0
for i in range(len(disk_map)):
    if i & 1:
        file_system.extend([None] * (ord(disk_map[i]) - ord0))
    else:
        file_system.extend([j] * (ord(disk_map[i]) - ord0))
        j += 1

# print(file_system)

# Use two-pointers technique: write from `right` index to `left` index
left = 0
while file_system[left] is not None:
    left += 1

right = len(file_system) - 1
while file_system[right] is None:
    right -= 1

while right > left:
    # print(' ' * left + str(left) + ' ' * (right - left - 1) + str(right))
    # print(''.join([('.' if item is None else str(item)) for item in file_system]))
    # print()

    file_system[left] = file_system[right]
    file_system[right] = None
    while file_system[left] is not None:
        left += 1
    while file_system[right] is None:
        right -= 1

# print(' ' * left + str(left) + ' ' * (right - left - 1) + str(right))
# print(''.join([('.' if item is None else str(item)) for item in file_system]))

checksum = sum(i * file_system[i] for i in range(len(file_system)) if file_system[i] is not None)
print(f"Part 1: The resulting filesystem checksum is {checksum}.")


##### Part 2: #####

# Create file system as list
file_system = []
j = 0  # location index into file system 
k = 0  # file name index
for i in range(len(disk_map)):
    size = ord(disk_map[i]) - ord0
    if i & 1:
        file_system.append([j, size, None])  # [position, length, contents]
    else:
        file_system.append([j, size, k])
        k += 1
    j += size

# print(file_system)

files = [f for f in file_system if f[2] is not None]
free  = [f for f in file_system if f[2] is None]

# print(files)
# print(free)

# print(''.join((str(f[2]) * f[1] if f[2] is not None else '.' * f[1]) for f in sorted(files + free, key=lambda f: f[0])))

for i in range(len(files) - 1, -1, -1):
    for j in range(len(free)):
        if free[j][0] > files[i][0]:  # if empty space is to the right of file, stop
            break
        elif free[j][1] >= files[i][1]:  # if we found enough space...
            free.append(files[i][:])  # ...mark file's old location as free...
            free[-1][2] = None
            files[i][0] = free[j][0]  # ...and move file to new location
            if free[j][1] == files[i][1]:
                del free[j]  # if file fits perfectly, delete free chunk
            else:
                free[j][0] += files[i][1]  # if not, move chunk right...
                free[j][1] -= files[i][1]  # ...and reduce size
            break
    print(''.join(
        (str(f[2]) * f[1] if f[2] is not None else '.' * f[1])
        for f in sorted(files + free, key=lambda f: f[0])
    ))

# print()
# print(files)
# print(free)

checksum = ''.join(
    (str(f[2]) * f[1] if f[2] is not None else '.' * f[1])
    for f in sorted(files + free, key=lambda f: f[0])
)
checksum = sum(
    (ord(checksum[i]) - ord0) * i
    for i in range(len(checksum))
    if checksum[i] != '.'
)

print(f"Part 1: The resulting filesystem checksum is {checksum}.")