from collections import Counter
from textwrap import dedent


def solve(input_lines: str) -> int:
    l1, l2 = [], []
    for line in input_lines.strip().split("\n"):
        d1, d2 = line.split("  ")
        l1.append(int(d1))
        l2.append(int(d2))

    c2 = Counter(l2)

    ans = 0
    for d1 in l1:
        ans += d1 * c2.get(d1, 0)

    return ans


def test_solve():
    input = dedent("""
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
    """)
    assert solve(input) == 31


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
