from collections import defaultdict
import functools
import itertools
import math
from textwrap import dedent

# TODO: does this act as global state?
best_n_presses: defaultdict[str, float | int] = defaultdict(default_factory=math.inf)


def solve(input: str) -> int:
    ans = 0
    for i, line in enumerate(input.strip().splitlines()):
        print(f"Line {i + 1}")
        lights, *buttons, _ = line.split(" ")
        buttons = tuple([tuple([int(number) for number in b[1:-1].split(",")]) for b in buttons])

        lights = lights[1:-1]
        ans += fewest_presses(lights, buttons)

    return ans


def fewest_presses(lights_desired: str, buttons: tuple[tuple[int, ...], ...]) -> int:
    ans = 1_000_000

    # Order doesn't matter; pressing a button twice does not need to be considered
    for button in itertools.chain.from_iterable(itertools.combinations(buttons, r) for r in range(len(buttons) + 1)):
        lights_after = "." * len(lights_desired)
        for b in button:
            lights_after = press_button(lights_after, b)

        if lights_after == lights_desired:
            ans = min(ans, len(button))

    return ans


def press_button(lights: str, button: tuple[int, ...]) -> str:
    return "".join(char if i not in button else ("#" if char == "." else ".") for i, char in enumerate(lights))


def test_solve():
    input = dedent("""
        [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
        [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    """)
    assert solve(input) == 7


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
