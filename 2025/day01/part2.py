from textwrap import dedent


def solve(input: str) -> int:
    ans = 0
    position = 50

    instructions = [l for l in input.split("\n") if l]
    for instruction in instructions:
        moved_past = 0
        if instruction[0] == "L":
            position = position - (int(instruction[1:]))

            while position < 0:
                position += 100
                moved_past += 1
        else:
            position = position + (int(instruction[1:]))

            while position >= 100:
                position -= 100
                moved_past += 1

        print(f"The dial is rotated {instruction} to point at {position}")

        if position == 0:
            ans += moved_past
        else:
            ans += moved_past
            if moved_past:
                print(f"The dial moved past 0 {moved_past} times")

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
