from textwrap import dedent


def solve(input: str) -> int:
    ans = 0
    position = 50

    instructions = [l for l in input.split("\n") if l]
    for instruction in instructions:
        clicks = int(instruction[1:])

        for _ in range(clicks):
            if instruction[0] == "R":
                position = (position + 1) % 100
            else:
                position = (position - 1) % 100

            if position == 0:
                ans += 1

    return ans


def test_solve():
    input = dedent("""
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
    """)
    assert solve(input) == 6


def test_solve__multiple_rotations_past_0_example():
    input = dedent("""
        L200
        R200
    """)
    assert solve(input) == 4


def test_solve_landing_on_zero():
    input = dedent("""
        L150
        L50
    """)
    assert solve(input) == 2


def test_solve_landing_on_zero_2():
    input = dedent("""
        L150
        R50
    """)
    assert solve(input) == 2


def test_solve__multiple_rotations_past_0():
    input = dedent("""
        L68
        L230
        R48
        L5
        R160
        L55
        L1
        L99
        R14
        L82
    """)
    assert solve(input) == 9


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
