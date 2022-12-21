import re
import time

from dataclasses import dataclass

input_file_path = "day19/test_input.txt"

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


def get_from_cache_or_solve(blueprint, state, memoize=False):
    if not memoize:
        return solve(
            blueprint=blueprint,
            **state
        )

    state_tuple = (v for v in state.values())
    if state_tuple in mem:
        return mem[state_tuple]
    else:
        ans = solve(
            blueprint=blueprint,
            **state
        )
        mem[(v for v in state.values())] = ans
        return ans


def solve(blueprint: Blueprint, ore_stored, clay_stored, obsidian_stored, nof_ore_robots, nof_clay_robots, nof_obsidian_robots, nof_geode_robots, minutes_left, geodes_cracked) -> int:
    if minutes_left <= 0:
        return geodes_cracked

    # Assumption: if it is possible to build a geode robot, we should build it
    if ore_stored >= blueprint.geode_robot_cost_ore and obsidian_stored >= blueprint.geode_robot_cost_obsidian:
        state = {
            "ore_stored": nof_ore_robots - blueprint.geode_robot_cost_ore,
            "clay_stored": clay_stored + nof_clay_robots,
            "obsidian_stored": obsidian_stored + nof_obsidian_robots - blueprint.geode_robot_cost_obsidian,
            "nof_ore_robots": nof_ore_robots,
            "nof_clay_robots": nof_clay_robots,
            "nof_obsidian_robots": nof_obsidian_robots,
            "nof_geode_robots": nof_geode_robots + 1,
            "geodes_cracked": geodes_cracked + nof_geode_robots,
            "minutes_left": minutes_left - 1
        }
        return get_from_cache_or_solve(blueprint, state)

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
        "minutes_left": minutes_left - 1
    }
    options.append(get_from_cache_or_solve(blueprint, state))

    # Option: build ore robot (if possible)
    if ore_stored >= blueprint.ore_robot_cost:
        state = {
            "ore_stored": ore_stored + nof_ore_robots - blueprint.ore_robot_cost,
            "clay_stored": clay_stored + nof_clay_robots,
            "obsidian_stored": obsidian_stored + nof_obsidian_robots,
            "nof_ore_robots": nof_ore_robots + 1,
            "nof_clay_robots": nof_clay_robots,
            "nof_obsidian_robots": nof_obsidian_robots,
            "nof_geode_robots": nof_geode_robots,
            "geodes_cracked": geodes_cracked + nof_geode_robots,
            "minutes_left": minutes_left - 1
        }
        options.append(get_from_cache_or_solve(blueprint, state))

    # Option: build clay robot (if possible)
    if ore_stored >= blueprint.clay_robot_cost:
        state = {
            "ore_stored": ore_stored + nof_ore_robots - blueprint.clay_robot_cost,
            "clay_stored": clay_stored + nof_clay_robots,
            "obsidian_stored": obsidian_stored + nof_obsidian_robots,
            "nof_ore_robots": nof_ore_robots,
            "nof_clay_robots": nof_clay_robots + 1,
            "nof_obsidian_robots": nof_obsidian_robots,
            "nof_geode_robots": nof_geode_robots,
            "geodes_cracked": geodes_cracked + nof_geode_robots,
            "minutes_left": minutes_left - 1
        }

        options.append(get_from_cache_or_solve(blueprint, state))

    # Option: build obsidian robot (if possible)
    if ore_stored >= blueprint.obsidian_robot_cost_ore and clay_stored >= blueprint.obsidian_robot_cost_clay:
        state = {
            "ore_stored": ore_stored + nof_ore_robots - blueprint.obsidian_robot_cost_ore,
            "clay_stored": clay_stored + nof_clay_robots - blueprint.obsidian_robot_cost_clay,
            "obsidian_stored": obsidian_stored + nof_obsidian_robots,
            "nof_ore_robots": nof_ore_robots,
            "nof_clay_robots": nof_clay_robots,
            "nof_obsidian_robots": nof_obsidian_robots + 1,
            "nof_geode_robots": nof_geode_robots,
            "geodes_cracked": geodes_cracked + nof_geode_robots,
            "minutes_left": minutes_left - 1
        }

        options.append(get_from_cache_or_solve(blueprint, state))

    return max(options)


if __name__ == '__main__':
    blueprint_quality_levels = []
    global mem

    for i, blueprint in enumerate(blueprints[:1], 1):
        tic = time.perf_counter()
        print(f"Evaluating blueprint {i}")
        mem = {}
        geodes_cracked = solve(
            blueprint=blueprint,
            ore_stored=0,
            clay_stored=0,
            obsidian_stored=0,
            nof_ore_robots=1,
            nof_clay_robots=0,
            nof_obsidian_robots=0,
            nof_geode_robots=0,
            minutes_left=19,
            geodes_cracked=0
        )
        tac = time.perf_counter()

        print(f"Blueprint {i} cracked {geodes_cracked} geodes - took {tac - tic:0.4f}s")
        blueprint_quality_levels.append(geodes_cracked * i)

    print(f"Answer: {sum(blueprint_quality_levels)}")
