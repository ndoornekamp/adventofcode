import re
import time

from dataclasses import dataclass

input_file_path = "day19/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()


@dataclass
class Blueprint:
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost_ore: int
    obsidian_robot_cost_clay: int
    geode_robot_cost_ore: int
    geode_robot_cost_obsidian: int


blueprints = []
for blueprint in input.split("\n"):
    match = re.match(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", blueprint)
    blueprints.append(Blueprint(
        ore_robot_cost=int(match.group(2)),
        clay_robot_cost=int(match.group(3)),
        obsidian_robot_cost_ore=int(match.group(4)),
        obsidian_robot_cost_clay=int(match.group(5)),
        geode_robot_cost_ore=int(match.group(6)),
        geode_robot_cost_obsidian=int(match.group(7)),
    ))


def solve(blueprint: Blueprint, ore_stored, clay_stored, obsidian_stored, nof_ore_robots, nof_clay_robots, nof_obsidian_robots, nof_geode_robots, minutes_left, geodes_cracked, skipped_building_ore_robot, skipped_building_clay_robot, skipped_building_obsidian_robot) -> int:
    if minutes_left <= 0:
        mem[0] = max(geodes_cracked, mem[0])
        return geodes_cracked

    if geodes_cracked + sum([nof_geode_robots + i for i in range(minutes_left)]) <= mem[0]:
        # print(f"With {geodes_cracked} geodes cracked, {nof_geode_robots} geode robots and {minutes_left} minutes left, this solution can result in at most {geodes_cracked + sum([(nof_geode_robots + i) for i in range(minutes_left)])} geodes cracked, which is not better than {mem[0]} (the best we've seen so far)")
        return 0

    options = []
    # Option: do nothing
    state = {
        "ore_stored": ore_stored + nof_ore_robots,
        "clay_stored": clay_stored + nof_clay_robots,
        "obsidian_stored": obsidian_stored + nof_obsidian_robots,
        "nof_ore_robots": nof_ore_robots,
        "nof_clay_robots": nof_clay_robots,
        "nof_obsidian_robots": nof_obsidian_robots,
        "nof_geode_robots": nof_geode_robots,
        "geodes_cracked": geodes_cracked + nof_geode_robots,
        "minutes_left": minutes_left - 1,
        "skipped_building_ore_robot": ore_stored >= blueprint.ore_robot_cost,
        "skipped_building_clay_robot": ore_stored >= blueprint.clay_robot_cost,
        "skipped_building_obsidian_robot": ore_stored >= blueprint.obsidian_robot_cost_ore and clay_stored >= blueprint.obsidian_robot_cost_clay
    }
    options.append(solve(blueprint=blueprint, **state))

    # Option: build ore robot (if possible)
    if all([
        ore_stored >= blueprint.ore_robot_cost,
        not skipped_building_ore_robot,
        nof_ore_robots <= max(blueprint.ore_robot_cost, blueprint.clay_robot_cost, blueprint.geode_robot_cost_ore, blueprint.obsidian_robot_cost_ore)
    ]):
        state = {
            "ore_stored": ore_stored + nof_ore_robots - blueprint.ore_robot_cost,
            "clay_stored": clay_stored + nof_clay_robots,
            "obsidian_stored": obsidian_stored + nof_obsidian_robots,
            "nof_ore_robots": nof_ore_robots + 1,
            "nof_clay_robots": nof_clay_robots,
            "nof_obsidian_robots": nof_obsidian_robots,
            "nof_geode_robots": nof_geode_robots,
            "geodes_cracked": geodes_cracked + nof_geode_robots,
            "minutes_left": minutes_left - 1,
            "skipped_building_ore_robot": False,
            "skipped_building_clay_robot": False,
            "skipped_building_obsidian_robot": False
        }
        options.append(solve(blueprint=blueprint, **state))

    # Option: build clay robot (if possible)
    if all([
        ore_stored >= blueprint.clay_robot_cost,
        not skipped_building_clay_robot,
        nof_clay_robots <= blueprint.obsidian_robot_cost_clay
    ]):
        state = {
            "ore_stored": ore_stored + nof_ore_robots - blueprint.clay_robot_cost,
            "clay_stored": clay_stored + nof_clay_robots,
            "obsidian_stored": obsidian_stored + nof_obsidian_robots,
            "nof_ore_robots": nof_ore_robots,
            "nof_clay_robots": nof_clay_robots + 1,
            "nof_obsidian_robots": nof_obsidian_robots,
            "nof_geode_robots": nof_geode_robots,
            "geodes_cracked": geodes_cracked + nof_geode_robots,
            "minutes_left": minutes_left - 1,
            "skipped_building_ore_robot": False,
            "skipped_building_clay_robot": False,
            "skipped_building_obsidian_robot": False
        }
        options.append(solve(blueprint=blueprint, **state))

    # Option: build obsidian robot (if possible)
    if all([
        ore_stored >= blueprint.obsidian_robot_cost_ore,
        clay_stored >= blueprint.obsidian_robot_cost_clay,
        not skipped_building_obsidian_robot,
        nof_obsidian_robots <= blueprint.geode_robot_cost_obsidian
    ]):
        state = {
            "ore_stored": ore_stored + nof_ore_robots - blueprint.obsidian_robot_cost_ore,
            "clay_stored": clay_stored + nof_clay_robots - blueprint.obsidian_robot_cost_clay,
            "obsidian_stored": obsidian_stored + nof_obsidian_robots,
            "nof_ore_robots": nof_ore_robots,
            "nof_clay_robots": nof_clay_robots,
            "nof_obsidian_robots": nof_obsidian_robots + 1,
            "nof_geode_robots": nof_geode_robots,
            "geodes_cracked": geodes_cracked + nof_geode_robots,
            "minutes_left": minutes_left - 1,
            "skipped_building_ore_robot": False,
            "skipped_building_clay_robot": False,
            "skipped_building_obsidian_robot": False
        }
        options.append(solve(blueprint=blueprint, **state))

    if ore_stored >= blueprint.geode_robot_cost_ore and obsidian_stored >= blueprint.geode_robot_cost_obsidian:
        state = {
            "ore_stored": ore_stored + nof_ore_robots - blueprint.geode_robot_cost_ore,
            "clay_stored": clay_stored + nof_clay_robots,
            "obsidian_stored": obsidian_stored + nof_obsidian_robots - blueprint.geode_robot_cost_obsidian,
            "nof_ore_robots": nof_ore_robots,
            "nof_clay_robots": nof_clay_robots,
            "nof_obsidian_robots": nof_obsidian_robots,
            "nof_geode_robots": nof_geode_robots + 1,
            "geodes_cracked": geodes_cracked + nof_geode_robots,
            "minutes_left": minutes_left - 1,
            "skipped_building_ore_robot": False,
            "skipped_building_clay_robot": False,
            "skipped_building_obsidian_robot": False
        }
        options.append(solve(blueprint=blueprint, **state))

    return max(options)


if __name__ == '__main__':
    blueprint_quality_levels = []
    global mem
    mins = 24

    for i, blueprint in enumerate(blueprints, 1):
        tic = time.perf_counter()
        print(f"Evaluating blueprint {i}")
        mem = [0]
        geodes_cracked = solve(
            blueprint=blueprint,
            ore_stored=0,
            clay_stored=0,
            obsidian_stored=0,
            nof_ore_robots=1,
            nof_clay_robots=0,
            nof_obsidian_robots=0,
            nof_geode_robots=0,
            minutes_left=mins,
            geodes_cracked=0,
            skipped_building_ore_robot=False,
            skipped_building_clay_robot=False,
            skipped_building_obsidian_robot=False
        )
        tac = time.perf_counter()

        print(f"Blueprint {i} cracked {geodes_cracked} geodes after {mins} minutes - took {tac - tic:0.4f}s")
        blueprint_quality_levels.append(geodes_cracked * i)

    print(f"Answer: {sum(blueprint_quality_levels)}")
