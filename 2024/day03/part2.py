import re
from textwrap import dedent


def result(input: str) -> int:
    valid_muls = re.findall(r"mul\((:?\d+),(:?\d+)\)", input)
    ans = 0
    for m in valid_muls:
        ans += int(m[0]) * int(m[1])

    return ans


def solve(input: str) -> int:
    splits = input.split("don't()")

    ans = result(splits[0])
    for split in splits[1:]:
        if "do()" in split:
            after_do = " ".join(split.split("do()")[1:])
            ans += result(after_do)

    return ans


def test_solve():
    input = dedent("""
        xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    """)
    assert solve(input) == 48


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
