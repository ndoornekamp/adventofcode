import copy
from dataclasses import dataclass
from textwrap import dedent


@dataclass
class Gap:
    length: int


@dataclass
class File:
    length: int
    file_id: int


def solve(input: str) -> int:
    reversed_input = list(reversed(input.strip()))

    file_id = 0
    blocks: list[Gap | File] = []
    while reversed_input:
        file_length = int(reversed_input.pop())
        blocks.append(File(length=file_length, file_id=file_id))
        file_id += 1

        try:
            gap_length = int(reversed_input.pop())
            blocks.append(Gap(gap_length))
        except IndexError:
            break

    blocks_to_try_to_move = copy.deepcopy(blocks)

    while blocks_to_try_to_move:
        if len(blocks_to_try_to_move) % 1000 == 0:
            print(f"Blocks remaining: {len(blocks_to_try_to_move)}")
        b1 = blocks_to_try_to_move.pop()
        if isinstance(b1, File):
            current_b1_idx = blocks.index(b1)
            for j, b2 in enumerate(blocks):
                if j > current_b1_idx:
                    # No sense in moving files right of their current location
                    continue

                if isinstance(b2, Gap):
                    if b2.length == b1.length:
                        blocks[j] = b1
                        blocks[current_b1_idx] = Gap(length=b1.length)
                        # TODO: merge adjacent gaps?
                        break
                    elif b2.length > b1.length:
                        blocks[j] = b1
                        blocks[current_b1_idx] = Gap(length=b1.length)
                        blocks.insert(j + 1, Gap(length=b2.length - b1.length))
                        # TODO: merge adjacent gaps?
                        break

    ans = 0
    idx = 0
    for block in blocks:
        for _ in range(block.length):
            if isinstance(block, File):
                ans += block.file_id * idx
            idx += 1

    return ans


def test_solve():
    input = dedent("""
        2333133121414131402
    """)
    assert solve(input) == 2858


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
