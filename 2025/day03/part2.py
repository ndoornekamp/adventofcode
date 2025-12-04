from textwrap import dedent

import pytest


def solve(input: str) -> int:
    input = input.strip()
    ans = 0

    for bank in input.split("\n"):
        ans += int(find_max_joltage(bank, 12, ""))

    return ans


def find_max_joltage(input: str, exclude_last_n_digits: int, max_joltage: str) -> str:
    """
    Append the next digit to the maximum joltage in the given input string, where the last <n> digits have to be
    excluded to ensure the answer has the correct length
    """
    if exclude_last_n_digits == 1:
        return max_joltage + max(input)

    search_in = input[:-exclude_last_n_digits+1]
    next_digit = max(search_in)
    split_idx = input.index(next_digit)
    return find_max_joltage(input[split_idx + 1 :], exclude_last_n_digits - 1, max_joltage + next_digit)


def test_solve():
    input = dedent("""
        987654321111111
        811111111111119
        234234234234278
        818181911112111
    """)
    assert solve(input) == 3121910778619


@pytest.mark.parametrize(
    ("input", "out"),
    [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ],
)
def test_one_bank(input: str, out: int):
    assert solve(input) == out


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
