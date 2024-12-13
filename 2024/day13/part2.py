import re
from textwrap import dedent

import z3


def solve(input: str) -> int:
    ans = 0
    for problem in input.strip().split("\n\n"):
        numbers = re.findall(r"\d+", problem)
        assert len(numbers) == 6
        numbers = [int(n) for n in numbers]

        numbers[4] = numbers[4] + 10000000000000
        numbers[5] = numbers[5] + 10000000000000

        a = z3.Int('a')
        b = z3.Int('b')
        s = z3.Solver()

        s.add(a > 0)
        s.add(b > 0)
        s.add(a * numbers[0] + b * numbers[2] == numbers[4])
        s.add(a * numbers[1] + b * numbers[3] == numbers[5])

        if s.check() == z3.sat:
            model = s.model()
            ans += model[a].as_long() * 3 + model[b].as_long()

    return int(ans)


def test_solve():
    input = dedent("""
        Button A: X+94, Y+34
        Button B: X+22, Y+67
        Prize: X=8400, Y=5400

        Button A: X+26, Y+66
        Button B: X+67, Y+21
        Prize: X=12748, Y=12176

        Button A: X+17, Y+86
        Button B: X+84, Y+37
        Prize: X=7870, Y=6450

        Button A: X+69, Y+23
        Button B: X+27, Y+71
        Prize: X=18641, Y=10279
    """)
    assert solve(input) == 875318608908


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
