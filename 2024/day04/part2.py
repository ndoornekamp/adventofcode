from textwrap import dedent


def solve(input: str) -> int:
    input = input.strip()
    rows = input.split("\n")

    ans = 0
    for i in range(1, len(rows) - 1):
        for j in range(1, len(rows) - 1):
            if rows[i][j] == "A":
                for p in [("M", "S", "M", "S"), ("M", "S", "S", "M"), ("S", "M", "M", "S"), ("S", "M", "S", "M")]:
                    if all(
                        (
                            rows[i - 1][j - 1] == p[0],
                            rows[i + 1][j + 1] == p[1],
                            rows[i - 1][j + 1] == p[2],
                            rows[i + 1][j - 1] == p[3],
                        )
                    ):
                        ans += 1
                        break

    return ans


def test_solve_example():
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
    assert solve(input) == 9


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
