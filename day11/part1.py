import math
import re

from pprint import pprint

input_file_path = "day11/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

monkeys = [{
        "items": [int(item) for item in monkey.split("\n")[1].split(": ")[1].split(", ")],
        "operation": monkey.split("\n")[2].split(": ")[1].split("new = ")[-1],
        "test_divisible_by": int(re.search("divisible by (\d+)", monkey.split("\n")[3])[1]),
        "true": int(re.search("throw to monkey (\d+)", monkey.split("\n")[4])[1]),
        "false": int(re.search("throw to monkey (\d+)", monkey.split("\n")[5])[1]),
        "nof_inspections": 0
    } for monkey in input.split("\n\n")
]

pprint(monkeys)

for round in range(20):
    for monkey in monkeys:
        # print(monkey["items"])
        for i, _ in enumerate(monkey["items"]):
            # Inspect: increase worry level
            old = monkey["items"][0]
            monkey["items"] = monkey["items"][1:]
            # print(f"Monkey 0 inspects an item of worry level {old}")

            new = eval(monkey["operation"])
            # print(f"Worry level is multiply to {new}")

            monkey["nof_inspections"] += 1

            # Relief: divide by three; round down
            new = math.floor(new/3)
            # print(f"Worry level is divided to {new}")

            # Test: throw to different monkey
            if new % monkey["test_divisible_by"] == 0:
                throw_to_monkey = monkey["true"]
            else:
                throw_to_monkey = monkey["false"]
            # print(f"Item with worry level {new} is thrown to monkey {throw_to_monkey}")
            monkeys[throw_to_monkey]["items"].append(new)

print([monkey["nof_inspections"] for monkey in monkeys])
sorted_nof_inspections = sorted([monkey["nof_inspections"] for monkey in monkeys])
print(sorted_nof_inspections)
monkey_business = sorted_nof_inspections[-1] * sorted_nof_inspections[-2]
print(monkey_business)