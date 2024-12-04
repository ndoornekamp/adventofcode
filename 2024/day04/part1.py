import re
from textwrap import dedent


def solve(input: str) -> int:
    input = input.strip()

    ans = 0
    for line in input.split("\n"):
        ans += len(re.findall(r"XMAS", line))
        ans += len(re.findall(r"SAMX", line))

    cols = [[] for _ in range(len(input.split("\n")[0]))]
    for i, line in enumerate(input.split("\n")):
        for j, char in enumerate(line):
            cols[j].append(char)

    for col in cols:
        line = "".join(col)
        ans += len(re.findall(r"XMAS", line))
        ans += len(re.findall(r"SAMX", line))

    diagonals = []
    rows = [list(row) for row in input.split("\n")]
    i = 0
    while not all(len(row) == 0 for row in rows):
        diagonal = ""
        for j in range(i + 1):
            if j >= len(rows):
                continue

            if len(rows[j]) > 0:
                diagonal += rows[j].pop(0)
        diagonals.append(diagonal)
        i += 1

    anti_diagonals = []
    rows = [list(row) for row in input.split("\n")]
    i = 0
    while not all(len(row) == 0 for row in rows):
        diagonal = ""
        for j in range(i + 1):
            if j >= len(rows):
                continue

            if len(rows[j]) > 0:
                diagonal += rows[j].pop()
        anti_diagonals.append(diagonal)
        i += 1

    for line in diagonals + anti_diagonals:
        ans += len(re.findall(r"XMAS", line))
        ans += len(re.findall(r"SAMX", line))

    return ans


def test_solve_example_small():
    input = dedent("""
        ..X...
        .SAMX.
        .A..A.
        XMAS.S
        .X....
        ......
    """)
    assert solve(input) == 4


def test_solve_example_large():
    input = dedent("""
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
    """)
    assert solve(input) == 18


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
