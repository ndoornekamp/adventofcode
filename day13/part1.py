input_file_path = "day13/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()


def is_in_correct_order(left, right) -> bool:
    if type(left) not in [int, list]:
        left = eval(left)

    if type(right) not in [int, list]:
        right = eval(right)

    if type(left) == type(right) == int:
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return "continue"
    elif type(left) == type(right) == list:
        for j in range(max(len(left), len(right))):
            if j >= len(left):
                return True
            elif j >= len(right):
                return False

            a = is_in_correct_order(left[j], right[j])
            if a == "continue":
                continue
            else:
                return a
        return "continue"
    elif type(left) == int and type(right) == list:
        a = is_in_correct_order([left], right)
        return a
    elif type(right) == int and type(left) == list:
        a = is_in_correct_order(left, [right])
        return a
    else:
        raise

ans = 0
for i, pair in enumerate(input.split("\n\n")):
    left, right = pair.split("\n")

    a = is_in_correct_order(left, right)
    ans = ans + i + 1 if a else ans

print(ans)
