from textwrap import dedent


def solve(input: str) -> int:
    ranges = input.split(",")
    ans = 0

    for id_range in ranges:
        range_start, range_end = id_range.split("-")
        for id in range(int(range_start), int(range_end) + 1):
            str_id = str(id)
            length = int(len(str_id) / 2)

            if str_id[:length] == str_id[length:]:
                print(f"Invalid ID! {str_id}")
                ans += id
    return ans


def test_solve():
    input = dedent("""
        11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
    """)
    assert solve(input) == 1227775554


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
