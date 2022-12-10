input_file_path = "day10/input.txt"

with open(input_file_path, 'r') as infile:
    instructions = infile.readlines()

X = 1
cycle = 0
instruction_no = 0
finished_at_end_of_cycle = 0
signal_strengths = []
crt_row = []
crt_rows = []

# print(f"During cycle {cycle}, X={X}")
while True:
    if instruction_no >= len(instructions):
        break

    sprite_position_overlaps_with_pixel_index = abs((cycle % 40) - X) <= 1
    current_pixel = "#" if sprite_position_overlaps_with_pixel_index else "."
    crt_row.append(current_pixel)
    print(crt_row)

    if cycle == finished_at_end_of_cycle + 1:  # Previous instruction finished at the end of the previous cycle
        instruction = instructions[instruction_no].strip("\n")
        if instruction == "noop":
            finished_at_end_of_cycle = cycle
            amount = 0
        elif instruction.startswith("addx"):
            _, amount = instruction.split(" ")
            finished_at_end_of_cycle = cycle + 1
        else:
            raise

        instruction_no += 1
        X = X + int(amount)

    # print(f"After cycle {cycle}, X={X}")
    cycle += 1
    # print()
    # print(f"During cycle {cycle}, X={X}")

    if cycle % 40 == 0:
        print(f"During cycle {cycle}, X={X}")
        signal_strengths.append((cycle+1)*X)
        crt_rows.append(crt_row)
        crt_row = []

for row in crt_rows:
    print("".join(row))
