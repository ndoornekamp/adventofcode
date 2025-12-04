from textwrap import dedent


def solve(input: str) -> int:
    input = input.strip()
    ans = 0
    for bank in input.split("\n"):
        highest = max(bank)

        if bank.index(highest) == len(bank) - 1:
            second_highest = max(bank[:-1])
            ans += int(second_highest + highest)
        else:
            # Find the second highest number _to the right_ of the highest
            second_highest = max(bank[bank.index(highest) + 1 :])
            ans += int(highest + second_highest)

    return ans


def test_solve():
    input = dedent("""
        987654321111111
        811111111111119
        234234234234278
        818181911112111
    """)
    assert solve(input) == 357


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
