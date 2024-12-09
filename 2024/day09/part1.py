from textwrap import dedent


def solve(input: str) -> int:
    reversed_input = list(reversed(input.strip()))

    file_id = 0
    blocks = []
    compacted_length = 0
    while reversed_input:
        file_length = int(reversed_input.pop())
        compacted_length += file_length
        blocks += file_length * [str(file_id)]
        file_id += 1
        try:
            gap_length = int(reversed_input.pop())
            blocks += gap_length * ["."]
        except IndexError:
            break

    compacted = blocks[:compacted_length]
    to_empty = [b for b in blocks[compacted_length:] if b != "."]
    gaps = list(reversed([i for i, v in enumerate(blocks) if v == "."]))

    while to_empty:
        print(len(to_empty))
        block_to_move = to_empty.pop()
        new_block_location = gaps.pop()

        if len(compacted) < new_block_location:
            compacted.append(block_to_move)
        else:
            compacted[new_block_location] = block_to_move

    ans = 0
    for i, v in enumerate(compacted):
        ans += i * int(v)

    return ans


def test_solve():
    input = dedent("""
        2333133121414131402
    """)
    assert solve(input) == 1928


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
