priorities = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

input_file_path = "day03/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.readlines()

priority_sum = 0
for i, rucksack in enumerate(input):
    if i % 3 != 0:
        continue

    items_in_first_rucksack = set(rucksack.strip("\n"))
    items_in_second_rucksack = set(input[i+1].strip("\n"))
    items_in_third_rucksack = set(input[i+2].strip("\n"))

    shared_items = items_in_first_rucksack.intersection(items_in_second_rucksack).intersection(items_in_third_rucksack)
    assert len(shared_items) == 1
    shared_item = list(shared_items)[0]

    priority_of_shared_item = priorities.index(shared_item) + 1
    priority_sum += priority_of_shared_item

print(priority_sum)
