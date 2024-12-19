from textwrap import dedent
from tqdm import tqdm
from functools import lru_cache


global towels


def solve(input: str) -> int:
    global towels

    towels, patterns = input.strip().split("\n\n")
    towels = [t.strip() for t in towels.split(",")]
    patterns = [p.strip() for p in patterns.split("\n")]

    possible_patterns = [n_possible_patterns(pattern) for pattern in tqdm(patterns)]

    return sum(p for p in possible_patterns if p > 0)


@lru_cache
def n_possible_patterns(pattern: str) -> int:
    global towels
    if not pattern:
        return 1

    patterns_to_check = [pattern[len(towel) :] for towel in towels if pattern.startswith(towel)]

    return sum(n_possible_patterns(p) for p in patterns_to_check)


def test_solve():
    input = dedent("""
        r, wr, b, g, bwu, rb, gb, br

        brwrr
        bggr
        gbbr
        rrbgbr
        ubwu
        bwurrg
        brgr
        bbrgwb
    """)
    assert solve(input) == 16


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
