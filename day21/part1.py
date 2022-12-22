import re

input_file_path = "day21/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

substitutions = {}
for line in input.split("\n"):
    name, expression = line.split(": ")
    substitutions[name] = expression


def substitute(expression, substitutions):
    if not any([char in expression for char in ["+", "-", "/", "*"]]):
        return int(expression)
    else:
        m = re.match(r"(\w{4}) ([+-/*]) (\w{4})", expression)
        lhs = substitute(substitutions[m.group(1)], substitutions)
        operation = m.group(2)
        rhs = substitute(substitutions[m.group(3)], substitutions)
        return eval(f"{lhs} {operation} {rhs}")

root_expression = substitutions["root"]
ans = substitute(root_expression, substitutions)
print(int(ans))
