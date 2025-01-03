from textwrap import dedent


def solve(input: str) -> int:

    locks, keys = [], []
    for block in input.strip().split("\n\n"):
        is_lock = block[0] == "#"

        rows = block.split("\n") if is_lock else reversed(block.split("\n"))
        heights = [-1 for _ in range(5)]
        for row in rows:
            for i, val in enumerate(row):
                if val == "#":
                    heights[i] += 1

        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)

    ans = 0
    for key in keys:
        for lock in locks:
            if all(key[i] + lock[i] <= 5 for i in range(len(key))):
                ans += 1

    return ans


def test_solve():
    input = dedent("""
        #####
        .####
        .####
        .####
        .#.#.
        .#...
        .....

        #####
        ##.##
        .#.##
        ...##
        ...#.
        ...#.
        .....

        .....
        #....
        #....
        #...#
        #.#.#
        #.###
        #####

        .....
        .....
        #.#..
        ###..
        ###.#
        ###.#
        #####

        .....
        .....
        .....
        #....
        #.#..
        #.#.#
        #####
    """)
    assert solve(input) == 3


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
