from textwrap import dedent


def solve(input: str) -> int:
    fresh_ranges_str, _ = input.strip().split("\n\n")

    ranges: list[tuple[int, int]] = []
    for fresh_range_str in fresh_ranges_str.split("\n"):
        range_start, range_end = fresh_range_str.split("-")
        ranges.append((int(range_start), int(range_end)))

    ranges = sorted(ranges)
    
    ranges_merged = []
    start, end = ranges.pop(0)
    while ranges:
        overlaps_with_next = end >= ranges[0][0]
        if overlaps_with_next:
            # Extend the range we're working on if it overlaps
            end = max(end, ranges.pop(0)[1])
        else:
            # Add the range we're done with and start a new one
            ranges_merged.append((start, end))
            start, end = ranges.pop(0)

    # Add the last range if that was not done yet
    if (start, end) not in ranges_merged:
        ranges_merged.append((start, end))

    ans = 0
    for r in ranges_merged:
        ans += r[1] - r[0] + 1

    return ans


def test_solve():
    input = dedent("""
        3-5
        10-14
        16-20
        12-18

        1
        5
        8
        11
        17
        32
    """)
    assert solve(input) == 14


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
