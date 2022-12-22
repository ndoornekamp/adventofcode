from sympy import var
from sympy.solvers import solve

input_file_path = "day21/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

substitutions = {}
symbol_strings = []
for line in input.split("\n"):
    name, expression = line.split(": ")
    symbol_strings.append(name)

    if not name == "humn":
        substitutions[name] = expression

var(symbol_strings)

lhs, rhs = eval(substitutions["root"]).free_symbols

simplified_expressions = []
for expression in [lhs, rhs]:
    i = 0
    while True:
        i += 1

        expression_new = expression
        for variable, substitution in substitutions.items():
            expression_new = expression_new.subs(eval(variable), eval(substitution))

        if expression_new == expression:
            break
        else:
            expression = expression_new
        print(expression)
        print(i)

    simplified_expressions.append(expression)
    print(expression)

print(solve(simplified_expressions[0] - simplified_expressions[1], humn)[0])
