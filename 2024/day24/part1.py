from textwrap import dedent


def solve(input: str) -> int:
    initial_str, gates_str = input.strip().split('\n\n')

    initial = {}
    for line in initial_str.split("\n"):
        gate, value = line.split(": ")
        initial[gate] = int(value)

    formulas = {}
    output_gates = []
    for line in gates_str.split("\n"):
        rule, out = line.split(" -> ")
        in1, operand, in2 = rule.split(" ")
        formulas[out] = ((in1, in2), operand)

        if out.startswith("z"):
            output_gates.append(out)

    # By nesting function inside solve(), we have access to all variables of the outer function without having to
    # pass them in. This makes it a lot easier to memoize.
    known = initial

    def output(gate):
        if gate in known:
            return known[gate]

        assert gate in formulas

        input_gates, operand = formulas[gate]

        match operand:
            case "AND":
                out = output(input_gates[0]) & output(input_gates[1])
            case "XOR":
                out = output(input_gates[0]) ^ output(input_gates[1])
            case "OR":
                out = output(input_gates[0]) | output(input_gates[1])

        known[gate] = out
        return out

    bin_ans = ""
    for gate in sorted(output_gates, reverse=True):
        bin_ans += str(output(gate))

    return int(bin_ans, 2)


def test_solve():
    input = dedent("""
        x00: 1
        x01: 1
        x02: 1
        y00: 0
        y01: 1
        y02: 0

        x00 AND y00 -> z00
        x01 XOR y01 -> z01
        x02 OR y02 -> z02
    """)
    assert solve(input) == 4


def test_solve_larger():
    input = dedent("""
        x00: 1
        x01: 0
        x02: 1
        x03: 1
        x04: 0
        y00: 1
        y01: 1
        y02: 1
        y03: 1
        y04: 1

        ntg XOR fgs -> mjb
        y02 OR x01 -> tnw
        kwq OR kpj -> z05
        x00 OR x03 -> fst
        tgd XOR rvg -> z01
        vdt OR tnw -> bfw
        bfw AND frj -> z10
        ffh OR nrd -> bqk
        y00 AND y03 -> djm
        y03 OR y00 -> psh
        bqk OR frj -> z08
        tnw OR fst -> frj
        gnj AND tgd -> z11
        bfw XOR mjb -> z00
        x03 OR x00 -> vdt
        gnj AND wpb -> z02
        x04 AND y00 -> kjc
        djm OR pbm -> qhw
        nrd AND vdt -> hwm
        kjc AND fst -> rvg
        y04 OR y02 -> fgs
        y01 AND x02 -> pbm
        ntg OR kjc -> kwq
        psh XOR fgs -> tgd
        qhw XOR tgd -> z09
        pbm OR djm -> kpj
        x03 XOR y03 -> ffh
        x00 XOR y04 -> ntg
        bfw OR bqk -> z06
        nrd XOR fgs -> wpb
        frj XOR qhw -> z04
        bqk OR frj -> z07
        y03 OR x01 -> nrd
        hwm AND bqk -> z03
        tgd XOR rvg -> z12
        tnw OR pbm -> gnj
    """)
    assert solve(input) == 2024


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
