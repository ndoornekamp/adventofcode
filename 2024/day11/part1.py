from textwrap import dedent
from tqdm import tqdm


def solve(input: str, blinks: int) -> int:
    stones = [int(s) for s in input.strip().split(" ")]

    for _ in tqdm(range(blinks), desc="Blinks"):
        stones_new = []
        for stone in stones:
            if stone == 0:
                stones_new.append(1)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                x = int(len(stone) / 2)
                left_digits, right_digits = stone[:x], stone[x:]
                stones_new.append(int(left_digits))
                stones_new.append(int(right_digits))
            else:
                stones_new.append(stone * 2024)
        stones = stones_new

    return len(stones)


def test_solve():
    input = dedent("""
        125 17
    """)
    assert solve(input, 25) == 55312


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input, 25)
    print(ans)
