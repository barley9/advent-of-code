with open("input.txt", 'r') as infile:
    cards = []
    for line in infile.readlines():
        winning, mynums = line.split(':')[1].split('|')
        winning = set(int(n) for n in winning.split())
        mynums  = set(int(n) for n in  mynums.split())
        cards.append([1, winning, mynums])

total_cards = 0
for i, (_, winning, mynums) in enumerate(cards):
    for j in range(1, len(winning & mynums) + 1):
        cards[i + j][0] += cards[i][0]

print(sum(card[0] for card in cards))