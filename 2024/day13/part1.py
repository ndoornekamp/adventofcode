import re
from textwrap import dedent
import numpy as np


def solve(input: str) -> int:
    ans = 0
    for problem in input.strip().split("\n\n"):
        numbers = re.findall(r"\d+", problem)
        assert len(numbers) == 6
        numbers = [int(n) for n in numbers]

        A = np.array([[numbers[0], numbers[2]], [numbers[1], numbers[3]]])
        b = np.array([numbers[4], numbers[5]])

        solution = np.linalg.solve(A, b)

        # A solution is guaranteed to exist without constraining the inputs to integer, but for this problem
        # the solution is only relevant if it is integer
        fp_errors = np.array([abs(solution[0] - round(solution[0])), abs(solution[1] - round(solution[1]))])
        if all(fp_error < 1e-5 for fp_error in fp_errors):
            ans += 3 * round(solution[0]) + round(solution[1])

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
    assert solve(input) == 480


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
