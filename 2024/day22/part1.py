import math
from textwrap import dedent

import pytest


def solve(input: str) -> int:
    ans = 0
    for buyer_secret in input.strip().split("\n"):
        buyer_secret = int(buyer_secret)
        for _ in range(2000):
            buyer_secret = next_secret(buyer_secret)

        ans += buyer_secret

    return ans


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
        10
        100
        2024
    """)
    assert solve(input) == 37327623


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
