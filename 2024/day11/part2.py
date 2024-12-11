from collections import defaultdict
from textwrap import dedent
from tqdm import tqdm


def solve(input: str, blinks: int) -> int:
    # Now that the list becomes unmanageably large as we iterate, note that many digits repeat many times in the row
    # --> Instead of handling every stone individually, handle all stones with the same number together
    stones = {int(s): 1 for s in input.strip().split(" ")}
    for _ in tqdm(range(blinks), desc="Blinks"):
        stones_new = defaultdict(int)
        for stone, count in stones.items():
            if stone == 0:
                stones_new[1] += count
            else:
                stone_str = str(stone)
                if len(stone_str) % 2 == 0:
                    x = len(stone_str) // 2
                    left_digits, right_digits = stone_str[:x], stone_str[x:]
                    stones_new[int(left_digits)] += count
                    stones_new[int(right_digits)] += count
                else:
                    stones_new[stone * 2024] += count
        stones = stones_new

    return sum(stones.values())


def test_solve():
    input = dedent("""
        125 17
    """)
    assert solve(input, 25) == 55312


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input, 75)
    print(ans)
