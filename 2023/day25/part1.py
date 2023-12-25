import networkx as nx

input_file_path = '2023/day25/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

graph = nx.Graph()
for line in input:
    source, targets = line.split(": ")
    graph.add_node(source)

    for target in targets.split(" "):
        graph.add_edge(source, target, capacity=1)

wires_to_disconnect = nx.minimum_edge_cut(graph)
graph.remove_edges_from(wires_to_disconnect)
partitions = list(nx.connected_components(graph))

print(len(partitions[0]) * len(partitions[1]))
