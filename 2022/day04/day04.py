input_file_path = "day04/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.readlines()

fully_contained_ranges = []
overlapping_ranges = []
for i, pair in enumerate(input):
    range1, range2 = pair.strip('\n').split(",")

    range1_start, range1_end = range1.split("-")
    range2_start, range2_end = range2.split("-")

    range1_start = int(range1_start)
    range1_end = int(range1_end)
    range2_start = int(range2_start)
    range2_end = int(range2_end)

    if range1_start >= range2_start and range1_end <= range2_end:
        # Range 1 is fully contained in range 2
        fully_contained_ranges.append(i)
    elif range2_start >= range1_start and range2_end <= range1_end:
        # Range 2 is fully contained in range 1
        fully_contained_ranges.append(i)
    else:
        pass

    if range1_start > range2_end:
        # Range 1 is entirely to the right of range 2 => Not entirely overlapping
        pass
    elif range2_start > range1_end:
        # Range 2 is entirely to the right of range 1 => Not entirely overlapping
        pass
    else:
        overlapping_ranges.append(i)

print(len(fully_contained_ranges))
print(len(overlapping_ranges))