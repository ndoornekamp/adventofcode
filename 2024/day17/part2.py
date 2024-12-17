import math
import re
from textwrap import dedent
from tqdm import tqdm


def solve(input: str) -> int:
    nums = [int(n) for n in re.findall(r"\d+", input)]

    _, register_b_in, register_c_in = nums[0], nums[1], nums[2]
    program = nums[3:]

    out = []

    # register_a_lower = 35_184_000_000_000  # outputs with register_a_in are length <16 before this
    # register_a_lower = 246_759_890_000_000  # looping in steps of 10m, a bunch of outputs had 10 matching digits after this
    register_a_lower = 247_839_536_500_000  # looping in steps of 1m, a match of 13 digits was soon after this
    # register_a_upper = 281_475_529_304_000  # outputs have length 17 after this
    register_a_upper = register_a_lower + 10_000_000

    max_matching_digits = 0
    for register_a_in in tqdm(range(register_a_lower, register_a_upper, 1)):
        register_a = register_a_in
        register_b = register_b_in
        register_c = register_c_in
        pointer = 0
        out = []
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
                    register_a = math.floor(register_a / 2**combo_operand)
                case 1:
                    register_b = register_b ^ literal_operand  # TODO: check
                case 2:
                    register_b = combo_operand % 8
                case 3:
                    if register_a != 0:
                        pointer = literal_operand
                        jumped = True
                case 4:
                    register_b = register_b ^ register_c
                case 5:
                    out += [combo_operand % 8]
                case 6:
                    register_b = math.floor(register_a / 2**combo_operand)
                case 7:
                    register_c = math.floor(register_a / 2**combo_operand)

            if not jumped:
                pointer += 2

        matching_digits = 0
        for i in range(len(out)):
            if out[-i] == program[-i]:
                matching_digits += 1

        if matching_digits >= max_matching_digits:
            max_matching_digits = matching_digits
            print(f"Found {matching_digits} matching digits with {register_a_in=}")

        if out == program:
            print(f"Exact match: {register_a_in=}")
            break

    return register_a_in


def test_solve():
    input = dedent("""
        Register A: 2024
        Register B: 0
        Register C: 0

        Program: 0,3,5,4,3,0
    """)
    assert solve(input) == 117440


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
