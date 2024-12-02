from textwrap import dedent


def solve(input_lines: str) -> int:
    l1, l2 = [], []
    for line in input_lines.strip().split("\n"):
        d1, d2 = line.split("  ")
        l1.append(int(d1))
        l2.append(int(d2))

    l1.sort()
    l2.sort()

    ans = 0
    for d1, d2 in zip(l1, l2):
        ans += abs(d1 - d2)

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
    assert solve(input) == 11


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
