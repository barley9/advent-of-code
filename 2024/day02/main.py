with open("input.txt", 'r') as infile:
    reports = [
        [int(level) for level in line.strip().split(' ')]
        for line in infile.readlines()
    ]


##### Part 1 #####

def is_safe(report: list) -> bool:
    increasing = []
    for i in range(len(report) - 1):
        if 0 < report[i + 1] - report[i] < 4:
            increasing.append(True)
        elif -4 < report[i + 1] - report[i] < 0:
            increasing.append(False)
        else:
            return False
    return all(increasing) or not any(increasing)

# for report in reports:
#     print(report, 'Safe' if is_safe(report) else 'Unsafe')

total = sum(is_safe(report) for report in reports)
print(f"Part 1: There were {total} safe reports")


##### Part 2 #####

def is_safe(report: list) -> bool:
    increasing = []
    for i in range(len(report) - 1):
        if 0 < report[i + 1] - report[i] < 4:
            increasing.append(True)
        elif -4 < report[i + 1] - report[i] < 0:
            increasing.append(False)
        else:
            return False
    return all(increasing) or not any(increasing)

total = 0
for report in reports:
    # print(report)
    if is_safe(report):
        # print("\talready SAFE")
        total += 1
    else:
        # print("\tUNSAFE")
        for i in range(len(report)):
            # print("\ttrying", report[:i] + report[i + 1:], f'(removed {report[i]})...')
            if is_safe(report[:i] + report[i + 1:]):
                # print('\t...is now SAFE')
                total += 1
                break
        else:
            # print("\t...is still UNSAFE")
            pass

print(f"Part 2: There were {total} safe reports")