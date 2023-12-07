
import collections
from functools import cmp_to_key


input_file_path = '2023/day07/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()


card_strength = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10
}

for rank in range(2, 10):
    card_strength[str(rank)] = rank


def compare(hand1, hand2):
    """
    Return 1 if hand 1 is stronger than hand 2; -1 otherwise
    Hands can not have equal strength unless they're identical
    """

    if hand1["type"] > hand2["type"]:
        return 1
    elif hand2["type"] > hand1["type"]:
        return -1
    else:
        for card_hand1, card_hand2 in zip(hand1["hand"], hand2["hand"]):
            # print(card_hand1, card_hand2)
            if card_strength[card_hand1] == card_strength[card_hand2]:
                continue
            else:
                if card_strength[card_hand1] > card_strength[card_hand2]:
                    # print(f"{card_hand1} beats {card_hand2}")
                    return 1
                else:
                    return -1
        raise

hands = []
for line in input:
    hand, bid = line.split(" ")

    cards = collections.Counter(hand)

    n_most_common_card = max(cards.values())
    if n_most_common_card == 5:
        type_strength = 6
        print(f"{hand} is Five of a kind")
    elif n_most_common_card == 4:
        type_strength = 5
        print(f"{hand} is Four of a kind")
    elif n_most_common_card == 3:
        if len(cards.values()) == 2:
            type_strength = 4
            print(f"{hand} is Full house")
        else:
            type_strength = 3
            print(f"{hand} is Three of a kind")
    elif n_most_common_card == 2:
        if len(cards.values()) == 3:
            type_strength = 2
            print(f"{hand} is two pair")
        else:
            type_strength = 1
            print(f"{hand} is a pair")
    else:
        type_strength = 0
        print(f"{hand} is high card")

    hands.append({"hand": hand, "cards": cards, "type": type_strength, "bid": int(bid)})

ranked_hands = sorted(hands, key=cmp_to_key(compare))

ans = 0
for rank, hand in enumerate(ranked_hands, start=1):
    ans += rank * hand["bid"]

print(ans)
