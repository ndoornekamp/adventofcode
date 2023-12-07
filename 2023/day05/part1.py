
input_file_path = '2023/day05/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read()

n_max = 2 * max([int(s) for s in input.split(" ") if s.isdigit()])

mappings = [m.split("\n") for m in input.split("\n\n")]
print(mappings)

seeds = [int(d) for d in mappings[0][0].split(" ") if d.isdigit()]

closest_seed = 0
closest_seed_location = 1_000_000_000

for seed in seeds:
    prev = seed
    for map in mappings[1:]:
        mapped = None
        for line in map[1:]:
            destination_range_start = int(line.split(" ")[0])
            source_range_start = int(line.split(" ")[1])
            range_length = int(line.split(" ")[2])
            if source_range_start <= prev < (source_range_start + range_length):
                mapped = destination_range_start + (prev - source_range_start)
                print(f"{mapped=} since {source_range_start} <= {prev} < {source_range_start + range_length}")
                break
        if not mapped:
            mapped = prev
        prev = mapped

    if mapped < closest_seed_location:
        closest_seed = seed
        closest_seed_location = mapped

print(closest_seed_location)
