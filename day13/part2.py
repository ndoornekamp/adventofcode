import functools

input_file_path = "day13/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()


def is_in_correct_order(left, right) -> int:
    if type(left) not in [int, list]:
        left = eval(left)

    if type(right) not in [int, list]:
        right = eval(right)

    if type(left) == type(right) == int:
        if left < right:
            return -1
        elif right < left:
            return 1
        else:
            return "continue"
    elif type(left) == type(right) == list:
        for j in range(max(len(left), len(right))):
            if j >= len(left):
                return -1
            elif j >= len(right):
                return 1

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


packets = [line for line in input.split("\n") if line]
packets.append([[6]])
packets.append([[2]])
sorted_packets = sorted(packets, key=functools.cmp_to_key(is_in_correct_order))

first_packet_idx = sorted_packets.index([[2]]) + 1
second_packet_idx = sorted_packets.index([[6]]) + 1
print(first_packet_idx * second_packet_idx)