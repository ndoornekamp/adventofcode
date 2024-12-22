from collections import defaultdict
import math
from textwrap import dedent

import pytest
from tqdm import tqdm


def solve(input: str) -> int:
    price_change_sequences = []
    for buyer_secret in tqdm(input.strip().split("\n"), "Change sequence per buyer"):
        old_price = int(str(buyer_secret)[-1])
        price_changes = [{"price": old_price, "change": None}]
        buyer_secret = int(buyer_secret)
        for _ in range(2000):
            buyer_secret = next_secret(buyer_secret)
            new_price = int(str(buyer_secret)[-1])
            price_changes.append({"price": new_price, "change": new_price - old_price})
            old_price = new_price

        price_change_sequences.append(price_changes)

    total_profit_per_sequence = defaultdict(int)
    for buyer_prices in tqdm(price_change_sequences, "Profit per sell sequence"):
        buyer_profit = {}
        changes = [p["change"] for p in buyer_prices]
        for sequence_start in range(len(changes) - 3):
            change_sequence = tuple(changes[sequence_start: sequence_start + 4])
            if change_sequence not in buyer_profit:
                buyer_profit[change_sequence] = buyer_prices[sequence_start + 3]["price"]

        for sequence, profit in buyer_profit.items():
            total_profit_per_sequence[sequence] += profit

    return max(total_profit_per_sequence.values())


def next_secret(secret: int) -> int:
    secret = mix(secret * 64, secret)
    secret = prune(secret)
    secret = mix(math.floor(secret / 32), secret)
    secret = prune(secret)
    secret = mix(secret * 2048, secret)
    return prune(secret)


def mix(value: int, secret: int) -> int:
    return value ^ secret


def prune(secret: int) -> int:
    return secret % 16777216


def test_mix():
    assert mix(15, 42) == 37


def test_prune():
    assert prune(100000000) == 16113920


@pytest.mark.parametrize(
    ("secret", "expected"),
    [
        (123, 15887950),
        (15887950, 16495136),
        (16495136, 527345),
        (527345, 704524),
        (704524, 1553684),
        (1553684, 12683156),
    ],
)
def test_next_secret(secret: int, expected: int):
    assert next_secret(secret) == expected


def test_solve():
    input = dedent("""
        1
        2
        3
        2024
    """)
    assert solve(input) == 23


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)

    # 2596 is too high