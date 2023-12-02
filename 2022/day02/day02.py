input_file_path = "day02/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.readlines()

scores = []
for line in input:
    opponent_play = line.split(" ")[0]
    strategy = line.split(" ")[1].strip()

    if opponent_play == "A":  # Rock
        your_play = {
            "X": "Z",  # Should lose -> play scissors -> Z
            "Y": "X",  # Should draw -> play rock -> X
            "Z": "Y"   # Should win -> play paper -> Y
        }.get(strategy)
        outcome_score = ["Z", "X", "Y"].index(your_play)*3
    elif opponent_play == "B":  # Paper
        your_play = {
            "X": "X",  # Should lose -> play rock -> X
            "Y": "Y",  # Should draw -> play paper -> Y
            "Z": "Z"   # Should win -> play scissors -> Z
        }.get(strategy)
        outcome_score = ["X", "Y", "Z"].index(your_play)*3
    else:  # Scissors
        your_play = {
            "X": "Y",  # Should lose -> play paper -> Y
            "Y": "Z",  # Should draw -> play scissors -> Z
            "Z": "X"   # Should win -> play rock -> X
        }.get(strategy)
        outcome_score = ["Y", "Z", "X"].index(your_play)*3

    shape_score = ["X", "Y", "Z"].index(your_play) + 1

    scores.append(shape_score + outcome_score)

print(scores)
print(sum(scores))
