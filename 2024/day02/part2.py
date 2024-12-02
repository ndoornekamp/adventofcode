def solve(input: str) -> int:
    lines = input.strip().split("\n")

    ans = 0
    for line in lines:
        digits = [int(d) for d in line.strip().split(" ")]
        safe = False

        for j in range(len(digits)):
            digits_with_jth_removed = digits[:j] + digits[j + 1 :]
            increments = [
                digits_with_jth_removed[i + 1] - digits_with_jth_removed[i]
                for i in range(len(digits_with_jth_removed) - 1)
            ]

            if (all(i > 0 for i in increments) or all(i < 0 for i in increments)) and all(
                0 < abs(i) <= 3 for i in increments
            ):
                safe = True

        if safe:
            ans += 1
            continue

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
    assert solve(input) == 4


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
