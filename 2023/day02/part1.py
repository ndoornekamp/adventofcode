import re


input_file_path = "day02/input.txt"

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

actual_cubes = {"red": 12, "green": 13, "blue": 14}


def is_possible(hand):
    for color in actual_cubes:
        if n_cubes := re.search(f"(\d+) {color}", hand):
            if int(n_cubes.group(1)) > actual_cubes[color]:
                return False
    return True


ans = 0
for game in input:
    game_id = int(game.split(":")[0][5:])

    hands = game.split(":")[1]

    if all(is_possible(hand) for hand in hands.split(";")):
        ans += game_id

print(ans)
