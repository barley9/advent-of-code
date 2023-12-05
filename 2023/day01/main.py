digits = set(chr(i) for i in range(ord('0'), ord('9') + 1))
digit_words = [
    ("one",   1),
    ("two",   2),
    ("three", 3),
    ("four",  4),
    ("five",  5),
    ("six",   6),
    ("seven", 7),
    ("eight", 8),
    ("nine",  9),
]

first_letters = {}
for word, dig in digit_words:
    if word[0] in first_letters:
        first_letters[word[0]].append((word, dig))
    else:
        first_letters[word[0]] = [(word, dig)]

with open("input.txt", 'r') as infile:
    total = 0
    for line in infile:
        print(line[:-1], end=", ")

        # Left-to-right replace digit words with digit character
        left_line = line
        i = 0
        while i < len(left_line):
            if left_line[i] in first_letters:
                for word, dig in first_letters[left_line[i]]:
                    if left_line[i:i + len(word)] == word:
                        left_line = left_line[:i] + str(dig) + left_line[i + len(word):]
            i += 1
        print(left_line[:-1], end=", ")

        # Right-to-left replace digit words with digit character 
        right_line = line
        i = len(right_line) - 1
        while i > -1:
            if right_line[i] in first_letters:
                for word, dig in first_letters[right_line[i]]:
                    if right_line[i:i + len(word)] == word:
                        right_line = right_line[:i] + str(dig) + right_line[i + len(word):]
            i -= 1
        print(right_line[:-1], end=", ")

        # Seek for left-most digit
        for left in range(len(left_line)):
            if left_line[left] in digits:
                break

        # Seek for right-most digit
        for right in range(len(right_line) - 1, -1, -1):
            if right_line[right] in digits:
                break

        # Update total
        total += int(left_line[left] + right_line[right])
        print(int(left_line[left] + right_line[right]))

print(total)