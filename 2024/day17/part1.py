import math
import re
from textwrap import dedent


def solve(input: str) -> str:
    nums = [int(n) for n in re.findall(r"\d+", input)]

    register_a, register_b, register_c = nums[0], nums[1], nums[2]
    program = nums[3:]

    pointer = 0
    ans = []
    while pointer < len(program):
        jumped = False
        opcode, literal_operand = program[pointer], program[pointer + 1]

        match literal_operand:
            case 0:
                combo_operand = 0
            case 1:
                combo_operand = 1
            case 2:
                combo_operand = 2
            case 3:
                combo_operand = 3
            case 4:
                combo_operand = register_a
            case 5:
                combo_operand = register_b
            case 6:
                combo_operand = register_c
            case _:
                raise

        match opcode:
            case 0:
                register_a = math.floor(register_a / 2 ** combo_operand)
            case 1:
                register_b = register_b ^ literal_operand
            case 2:
                register_b = combo_operand % 8
            case 3:
                if register_a != 0:
                    pointer = literal_operand
                    jumped = True
            case 4:
                register_b = register_b ^ register_c
            case 5:
                ans += [combo_operand % 8]
            case 6:
                register_b = math.floor(register_a / 2**combo_operand)
            case 7:
                register_c = math.floor(register_a / 2**combo_operand)

        if not jumped:
            pointer += 2

    return ",".join((str(c) for c in ans))


def test_solve():
    input = dedent("""
        Register A: 729
        Register B: 0
        Register C: 0

        Program: 0,1,5,4,3,0
    """)
    assert solve(input) == "4,6,3,5,6,3,5,2,1,0"


def test_solve_part2_example():
    input = dedent("""
        Register A: 117440
        Register B: 0
        Register C: 0

        Program: 0,3,5,4,3,0
    """)
    assert solve(input) == "0,3,5,4,3,0"


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
