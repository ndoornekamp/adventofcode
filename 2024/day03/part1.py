import re
from textwrap import dedent


def solve(input: str) -> int:
    valid_muls = re.findall(r"mul\((:?\d+),(:?\d+)\)", input)

    ans = 0
    for m in valid_muls:
        ans += int(m[0]) * int(m[1])

    return ans


def test_solve():
    input = dedent("""
        xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    """)
    assert solve(input) == 161


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
