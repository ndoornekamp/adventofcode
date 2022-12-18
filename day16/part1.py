import re
import time

from dijkstra import Graph, dijkstra

input_file_path = "day16/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

valves = {}

for i, valve in enumerate(input.split("\n")):
    match = re.search(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)$", valve)

    valves[match.group(1)] = {
        "int_id": i,
        "flow": int(match.group(2)),
        "tunnels": [valve.strip() for valve in match.group(3).split(",")],
        "open": False
    }

valve_int_id_to_valve_id = {valve["int_id"]: valve_id for valve_id, valve in valves.items()}

# How many minutes does it take to get from a given valve to any other?
for valve_id, valve in valves.items():
    graph = Graph(len(input.split("\n")))
    for _, valve_info in valves.items():
        for dest in valve_info["tunnels"]:
            dest_id = valves[dest]["int_id"]
            graph.add_edge(valve_info["int_id"], dest_id, 1)

    valve["shortest_paths"] = dijkstra(graph, valve["int_id"])


def solve(current_valve, minutes_left, closed_valves, total_flow):
    flows = []

    if not closed_valves:
        return total_flow

    if minutes_left <= 0:
        return total_flow

    for closed_valve_id in closed_valves:
        minutes_to_get_to_valve = current_valve["shortest_paths"][valves[closed_valve_id]["int_id"]]
        flows.append(
            solve(
                current_valve=valves[closed_valve_id],
                minutes_left=minutes_left - minutes_to_get_to_valve - 1,
                closed_valves=[i for i in closed_valves if i != closed_valve_id],
                total_flow=(minutes_left - minutes_to_get_to_valve - 1) * valves[closed_valve_id]["flow"] + total_flow
            )
        )
    return max(flows)


tic = time.perf_counter()
ans = solve(
    current_valve=valves["AA"],
    minutes_left=30,
    closed_valves=[valve_id for valve_id, valve in valves.items() if valve["flow"] > 0],
    total_flow=0
)
toc = time.perf_counter()

print(ans)

print(f"Found the answer in {toc - tic:0.4f}s")
