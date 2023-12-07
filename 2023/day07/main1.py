import collections
import operator


types = [
    'high card',
    'one pair',
    'two pair',
    'three of a kind',
    'full house',
    'four of a kind',
    'five of a kind',
]
cards = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))
card_vals = {cards[i] : i + 2 for i in range(len(cards))}

def hand_type(hand: str) -> int:
    counts = collections.Counter(hand)
    if len(counts) == 1:  # must be 5-of-a-kind
        return 6
    elif len(counts) == 2:  # could be either 4-of-a-kind or full-house
        if counts.most_common(1)[0][1] == 4:
            return 5
        else:
            return 4
    elif len(counts) == 3:  # could be either three-of-a-kind or two-pair
        if counts.most_common(1)[0][1] == 3:
            return 3
        else:
            return 2
    elif len(counts) == 4:  # must be one-pair
        return 1
    else:  # must be high-card
        return 0

hands = []
with open("input.txt", 'r') as infile:
    for line in infile:
        h, b = line.split()
        b = int(b)
        hands.append((
            (
                hand_type(h),
                *(card_vals[c] for c in h)
            ),
            b
        ))

hands.sort(key=operator.itemgetter(0))

print(sum((i + 1) * hands[i][1] for i in range(len(hands))))