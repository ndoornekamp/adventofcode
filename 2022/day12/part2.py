from dijkstra import Graph, dijkstra

input_file_path = "day12/test_input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

heights = [[height for height in row] for row in input.split("\n")]

nof_nodes = len(heights)*len(heights[0])
graph = Graph(nof_nodes)

start_nodes = set()
for i, row in enumerate(heights):
    for j, height in enumerate(row):
        node_number = i*len(heights[0]) + j

        if height in ["a", "S"]:
            height = "a"
            start_nodes.add(node_number)
        elif height == "E":
            height = "z"

        for id in [1, 0, -1]:
            if not (0 <= i + id < len(heights)):
                continue
            id = i + id

            for jd in [1, 0, -1]:
                if abs(id - i) > 0 and jd != 0:
                    continue

                if not (0 <= j + jd < len(row)):
                    continue

                if i == id and jd == 0:
                    continue

                jd = j + jd

                target_height = heights[id][jd]

                if target_height == "S":
                    target_height = "a"
                elif target_height == "E":
                    target_height = "z"
                    target_node = id*len(heights[0]) + jd

                if ord(height) - ord(target_height) <= 1:
                    neighbor_number = id*len(heights[0]) + jd
                    # print(f"Adding node from {node_number} to {neighbor_number}")
                    graph.add_edge(node_number, neighbor_number, 1)
                else:
                    # print(f"Not possible to go from node {node_number} to {neighbor_number}")
                    pass

paths = dijkstra(graph, target_node)
distances_to_start_nodes = [paths[start_node] for start_node in start_nodes]
print(min(distances_to_start_nodes))
