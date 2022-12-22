from sympy import var
from sympy.core.numbers import Integer

input_file_path = "day21/test_input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

substitutions = {}
symbol_strings = []
for line in input.split("\n"):
    name, expression = line.split(": ")
    symbol_strings.append(name)
    substitutions[name] = expression

var(symbol_strings)

expression = eval(substitutions["root"])

while not isinstance(expression, Integer):
    for variable, substitution in substitutions.items():
        expression = expression.subs(eval(variable), eval(substitution))

print(expression)
