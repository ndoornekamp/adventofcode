from dataclasses import dataclass
import re
from tqdm import tqdm

input_file_path = "day19/test_input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

@dataclass
class Blueprint:
    blueprint_id: int
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost_ore: int
    obsidian_robot_cost_clay: int
    geode_robot_cost_ore: int
    geode_robot_cost_obsidian: int

@dataclass
class State:
    ore_stored: int
    clay_stored: int
    obsidian_stored: int
    geodes_cracked: int
    nof_ore_robots: int
    nof_clay_robots: int
    nof_obsidian_robots: int
    nof_geode_robots: int
    minutes_left: int

blueprints = []
for blueprint in input.split("\n"):
    match = re.match(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", blueprint)
    blueprints.append(Blueprint(
        blueprint_id=int(match.group(1)),
        ore_robot_cost=int(match.group(2)),
        clay_robot_cost=int(match.group(3)),
        obsidian_robot_cost_ore=int(match.group(4)),
        obsidian_robot_cost_clay=int(match.group(5)),
        geode_robot_cost_ore=int(match.group(6)),
        geode_robot_cost_obsidian=int(match.group(7)),
    ))

def solve(state: State):
    return 

initial_state = State(
    ore_stored=0,
    clay_stored=0,
    obsidian_stored=0,
    nof_ore_robots=0,
    nof_clay_robots=0,
    nof_obsidian_robots=0,
    nof_geode_robots=0,
    minutes_left=24
)
solve(state=initial_state)