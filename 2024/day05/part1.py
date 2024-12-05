import math
from textwrap import dedent


def solve(input: str) -> int:
    rules_str, update_str = input.strip().split("\n\n")

    rules = []
    for line in rules_str.split("\n"):
        d1, d2 = line.split("|")
        rules.append((int(d1), int(d2)))

    updates = []
    for line in update_str.split("\n"):
        updates.append([int(d) for d in line.split(",")])

    ans = 0
    for update in updates:
        is_correct = True
        for rule in rules:
            try:
                i1 = update.index(rule[0])
                i2 = update.index(rule[1])
            except ValueError:
                continue

            if i1 > i2:
                is_correct = False
                break

        if is_correct:
            middle_idx = math.ceil(len(update) / 2) - 1
            ans += update[middle_idx]

    return ans


def test_solve():
    input = dedent("""
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13

        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47
    """)
    assert solve(input) == 143


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
