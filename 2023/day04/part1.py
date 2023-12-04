
input_file_path = '2023/day04/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

ans = 0
n_scratchcards = {n+1: 1 for n in range(len(input))}
for card_number, card in enumerate(input, start=1):
    numbers = card.split(":")[1]
    my_numbers = {number for number in numbers.split("|")[0].split(" ") if number}
    winning_numbers = {number for number in numbers.split("|")[1].split(" ") if number}

    n_winning_numbers = len(winning_numbers.intersection(my_numbers))

    for m in range(n_scratchcards[card_number]):
        for n in range(card_number + 1, card_number + n_winning_numbers + 1):
            n_scratchcards[n] += 1

print(sum(n_scratchcards.values()))
