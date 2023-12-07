
import collections
from functools import cmp_to_key


input_file_path = '2023/day07/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()


card_strength = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 0,  # J cards are now the weakest cards
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
            if card_strength[card_hand1] == card_strength[card_hand2]:
                continue
            else:
                if card_strength[card_hand1] > card_strength[card_hand2]:
                    return 1
                else:
                    return -1
        raise

hands = []
for line in input:
    original_hand, bid = line.split(" ")

    original_cards = collections.Counter(original_hand)

    # J cards can pretend to be whatever card is best for the purpose of determining hand type
    # What is best is always to mimic the most common card, UNLESS THAT CARD IS J

    if original_hand == "JJJJJ":
        hands.append({"hand": original_hand, "cards": {"K": 5}, "type": 6, "bid": int(bid)})
    else:
        if "J" in original_cards:
            del original_cards["J"]

        most_common_card = max(original_cards, key=original_cards.get)

        hand = original_hand.replace("J", most_common_card)
        cards = collections.Counter(hand)

        n_most_common_card = max(cards.values())
        if n_most_common_card == 5:
            type_strength = 6
        elif n_most_common_card == 4:
            type_strength = 5
        elif n_most_common_card == 3:
            if len(cards.values()) == 2:
                type_strength = 4
            else:
                type_strength = 3
        elif n_most_common_card == 2:
            if len(cards.values()) == 3:
                type_strength = 2
            else:
                type_strength = 1
        else:
            type_strength = 0

        hands.append({"hand": original_hand, "cards": cards, "type": type_strength, "bid": int(bid)})

ranked_hands = sorted(hands, key=cmp_to_key(compare))

ans = 0
for rank, original_hand in enumerate(ranked_hands, start=1):
    ans += rank * original_hand["bid"]

print(ans)
