def solve(input: str) -> int:
    lines = input.strip().split("\n")

    ans = 0
    for line in lines:
        digits = [int(d) for d in line.strip().split(" ")]
        increments = [digits[i + 1] - digits[i] for i in range(len(digits) - 1)]

        if (all(i > 0 for i in increments) or all(i < 0 for i in increments)) and all(
            0 < abs(i) <= 3 for i in increments
        ):
            ans += 1

    return ans


def test_solve():
    input = """
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
    """
    assert solve(input) == 2


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
