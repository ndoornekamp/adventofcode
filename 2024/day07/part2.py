from itertools import product
import re
from textwrap import dedent
from tqdm import tqdm


def add(n1: int, n2: int) -> int:
    return n1 + n2


def multiply(n1: int, n2: int) -> int:
    return n1 * n2


def concat(n1: int, n2: int) -> int:
    return int(str(n1) + str(n2))


operators = [add, multiply, concat]


def solve(input: str) -> int:
    ans = 0
    for line in tqdm(input.strip().split("\n")):
        m = re.findall(r"\d+", line)
        test_value = int(m[0])
        numbers = [int(v) for v in m[1:]]

        for op in product(operators, repeat=len(numbers) - 1):
            outcome = numbers[0]
            for i, number in enumerate(numbers[1:]):
                outcome = op[i](outcome, number)

            if outcome == test_value:
                ans += test_value
                break

    return ans


def test_solve():
    input = dedent("""
        190: 10 19
        3267: 81 40 27
        83: 17 5
        156: 15 6
        7290: 6 8 6 15
        161011: 16 10 13
        192: 17 8 14
        21037: 9 7 18 13
        292: 11 6 16 20
    """)
    assert solve(input) == 11387


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
