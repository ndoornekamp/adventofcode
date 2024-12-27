from functools import cache
import itertools
from textwrap import dedent
import time

import pytest


def solve(input: str, max_depth: int) -> int:
    ans = 0
    codes = input.strip().split("\n")

    for code in codes:
        ans += int(code[:-1]) * shortest_sequence_len(code, max_depth=max_depth)

    return ans


def shortest_sequence_len(code: str, max_depth: int) -> int:
    first_robot_pos = "A"
    moves_first_robot: list[list[str]] = []

    for numeric_key in code:
        moves_first_robot += [list(possible_moves_on_numeric_pad(first_robot_pos, numeric_key))] + [["A"]]
        first_robot_pos = numeric_key

    ans = float("inf")
    for possible_step_sequence_first_robot in list(itertools.product(*moves_first_robot)):
        m = min_moves(possible_step_sequence_first_robot, depth=1, max_depth=max_depth)
        if ans > m:
            ans = m

    assert isinstance(ans, int)
    return ans


def min_moves(step_sequence_prevous_robot: tuple[str, ...], depth: int, max_depth: int) -> int:
    robot_pos = "A"
    moves_this_robot: list[list[str]] = []
    for step in step_sequence_prevous_robot:
        for direction in step:
            if robot_pos != direction:
                moves_this_robot += [list(possible_moves_on_directional_pad(robot_pos, direction))]
                moves_this_robot += [["A"]]
                robot_pos = direction
            else:
                moves_this_robot += [["A"]]

    if depth == max_depth:
        return sum([len(m[0]) for m in moves_this_robot])
    else:
        n_moves_per_sequence = []
        for step_sequence_this_robot in itertools.product(*moves_this_robot):
            n_moves_per_sequence.append(min_moves(step_sequence_this_robot, depth=depth + 1, max_depth=max_depth))
        return min(n_moves_per_sequence)


def find_possible_moves(grid: list[list[str]], start: str, end: str, invalid_pos: tuple[int, int]) -> set[str]:
    rs, re, cs, ce = -99, -99, -99, -99
    for i, row in enumerate(grid):
        for j, key in enumerate(row):
            if key == start:
                rs, cs = i, j
            if key == end:
                re, ce = i, j

    dr = rs - re
    dc = cs - ce

    unordered_moves = abs(dc) * [((0, -1) if cs >= ce else (0, 1))] + abs(dr) * [((-1, 0) if rs >= re else (1, 0))]
    movesets = itertools.permutations(unordered_moves)

    allowed_movesets = set()
    for moveset in movesets:
        pos_row, pos_col = rs, cs
        valid = True
        for step_row, step_col in moveset:
            pos_row += step_row
            pos_col += step_col

            if (pos_row, pos_col) == invalid_pos:
                valid = False

        if valid:
            moves = [{(0, -1): "<", (0, 1): ">", (-1, 0): "^", (1, 0): "v"}.get(move) for move in moveset]
            allowed_movesets.add("".join(moves))

    return allowed_movesets


def possible_moves_on_numeric_pad(start: str, end: str) -> set[str]:
    grid = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["", "0", "A"],
    ]
    return find_possible_moves(grid, start, end, invalid_pos=(3, 0))


@cache
def possible_moves_on_directional_pad(start: str, end: str) -> set[str]:
    grid = [
        ["", "^", "A"],
        ["<", "v", ">"],
    ]
    return find_possible_moves(grid, start, end, invalid_pos=(0, 0))


@pytest.mark.parametrize(
    ("start", "end", "expecteded_moves"),
    [
        ("A", "0", {"<"}),
        ("0", "A", {">"}),
        ("A", "1", {"^<<", "<^<"}),  # Avoid empty corner: <<^ is not valid
        ("7", "0", {">vvv", "v>vv", "vv>v"}),  # Avoid empty corner: vvv> is not valid
    ],
)
def test_moves_on_numeric_pad(start: str, end: str, expecteded_moves: str):
    assert possible_moves_on_numeric_pad(start, end) == expecteded_moves


@pytest.mark.parametrize(
    ("start", "end", "expecteded_moves"),
    [
        ("A", "^", {"<"}),
        ("^", "A", {">"}),
        ("<", "A", {">>^", ">^>"}),  # Avoid empty corner: ^>> is not valid
        ("A", "<", {"v<<", "<v<"}),  # Avoid empty corner: <<v is not valid
    ],
)
def test_moves_on_directional_pad(start: str, end: str, expecteded_moves: str):
    assert possible_moves_on_directional_pad(start, end) == expecteded_moves


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("029A", len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")),
        ("980A", len("<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A")),
        ("179A", len("<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")),
        ("456A", len("<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A")),
        ("379A", len("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")),
    ],
)
def test_shortest_sequence(code: str, expected: str):
    assert shortest_sequence_len(code, max_depth=2) == expected


def test_solve():
    input = dedent("""
        029A
        980A
        179A
        456A
        379A
    """)
    assert solve(input, max_depth=2) == 126384


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    start = time.time()
    ans = solve(input, max_depth=2)
    print(ans, time.time() - start)
