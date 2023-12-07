from tqdm import tqdm

input_file_path = '2023/day05/test_input.txt'

with open(input_file_path, 'r') as f:
    input = f.read()

n_max = 2 * max([int(s) for s in input.split(" ") if s.isdigit()])

mappings_raw = [m.split("\n") for m in input.split("\n\n")]
seeds = [int(d) for d in mappings_raw[0][0].split(" ") if d.isdigit()]

mappings = []
for mapping_raw in mappings_raw[1:]:
    mapping = []
    for line in mapping_raw[1:-1]:
        mapping.append((int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2])))
    mappings.append(mapping)

starts = seeds[::2]
lengths = seeds[1::2]

closest_seed = 0
closest_seed_location = 1_000_000_000

for start, length in zip(starts, lengths):
    for seed in tqdm(range(start, start + length)):
        prev = seed
        for map in mappings:
            mapped = None
            for line in map:
                destination_range_start = line[0]
                source_range_start = line[1]
                range_length = line[2]
                if source_range_start <= prev < (source_range_start + range_length):
                    mapped = destination_range_start + (prev - source_range_start)
                    break
            if not mapped:
                mapped = prev
            prev = mapped

        if mapped < closest_seed_location:
            closest_seed = seed
            closest_seed_location = mapped

print(closest_seed_location)
