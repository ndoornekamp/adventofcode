import math
import re


input_file_path = "day02/input.txt"

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()


def power(hands) -> int:
    min_cubes = {"red": 0, "blue": 0, "green": 0}

    for hand in hands:
        for color in min_cubes:
            if n_cubes := re.search(f"(\d+) {color}", hand):
                if int(n_cubes.group(1)) > min_cubes[color]:
                    min_cubes[color] = int(n_cubes.group(1))

    return math.prod(min_cubes.values())


ans = 0
for game in input:
    game_id = int(game.split(":")[0][5:])

    hands = game.split(":")[1]
    ans += power(hands.split(";"))

print(ans)
