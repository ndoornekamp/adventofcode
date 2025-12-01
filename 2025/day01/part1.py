from textwrap import dedent


def solve(input: str) -> int:
    ans = 0
    position = 50

    instructions = [l for l in input.split("\n") if l]
    for instruction in instructions:
        if instruction[0] == "L":
            position = position - (int(instruction[1:])) % 100

            if position < 0:
                position += 100
        else:
            position = position + (int(instruction[1:])) % 100

            if position >= 100:
                position -= 100

        if position == 0:
            ans += 1
        print(f"The dial points at {position}")

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
    assert solve(input) == 3


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
