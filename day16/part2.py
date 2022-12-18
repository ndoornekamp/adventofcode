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


def solve(current_valve_you, current_valve_elephant, minutes_left_you, minutes_left_elephant, closed_valves, total_flow):
    flows = [total_flow]

    if not closed_valves:
        return total_flow

    if minutes_left_you <= 0 or minutes_left_elephant <= 0:
        return total_flow

    if len(closed_valves) > 1:
        for closed_valve_id_you in closed_valves:
            minutes_to_get_to_valve_you = current_valve_you["shortest_paths"][valves[closed_valve_id_you]["int_id"]]

            if (minutes_left_you - minutes_to_get_to_valve_you - 1) <= 0:
                continue

            for closed_valve_id_elephant in [i for i in closed_valves if i != closed_valve_id_you]:
                minutes_to_get_to_valve_elephant = current_valve_elephant["shortest_paths"][valves[closed_valve_id_elephant]["int_id"]]

                tf = sum([
                    total_flow,
                    (minutes_left_you - minutes_to_get_to_valve_you - 1) * valves[closed_valve_id_you]["flow"],
                ])

                if (minutes_left_elephant - minutes_to_get_to_valve_elephant - 1) > 0:
                    tf += (minutes_left_elephant - minutes_to_get_to_valve_elephant - 1) * valves[closed_valve_id_elephant]["flow"]

                flows.append(
                    solve(
                        current_valve_you=valves[closed_valve_id_you],
                        current_valve_elephant=valves[closed_valve_id_elephant],
                        minutes_left_you=minutes_left_you - minutes_to_get_to_valve_you - 1,
                        minutes_left_elephant=minutes_left_elephant - minutes_to_get_to_valve_elephant - 1,
                        closed_valves=[i for i in closed_valves if i not in [closed_valve_id_you, closed_valve_id_elephant]],
                        total_flow=tf
                    )
                )
    else:  # Either you or the elephant opens the last valve
        remaining_valve_id = closed_valves[0]
        minutes_to_get_to_valve_you = current_valve_you["shortest_paths"][valves[remaining_valve_id]["int_id"]]
        minutes_to_get_to_valve_elephant = current_valve_elephant["shortest_paths"][valves[remaining_valve_id]["int_id"]]

        flows.append(total_flow + (minutes_left_you - minutes_to_get_to_valve_you - 1)
                     * valves[remaining_valve_id]["flow"])
        flows.append(total_flow + (minutes_left_elephant - minutes_to_get_to_valve_elephant - 1)
                     * valves[remaining_valve_id]["flow"])

    return max(flows)


tic = time.perf_counter()
ans = solve(
    current_valve_you=valves["AA"],
    current_valve_elephant=valves["AA"],
    minutes_left_you=26,
    minutes_left_elephant=26,
    # Can safely ignore valves with zero flow
    closed_valves=[valve_id for valve_id, valve in valves.items() if valve["flow"] > 0],
    total_flow=0
)
toc = time.perf_counter()

print(ans)

print(f"Found the answer in {toc - tic:0.4f}s")
