input_file_path = "2023/day23/input.txt"

with open(input_file_path, "r") as f:
    input = f.read().splitlines()


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Node:
    def __init__(self):
        self.edges: dict[tuple[int, int], int] = {}

    def __repr__(self):
        return f"Node(edges={self.edges})"

    def add_edge(self, dest: tuple[int, int], length: int):
        self.edges[dest] = length


class Graph:
    def __init__(self):
        self.nodes: dict[tuple[int, int], Node] = {}

    def __repr__(self):
        return f"Graph(nodes={self.nodes})"

    def contract_edges(self):
        print(f"Contracting edges - starting with {len(self.nodes)} nodes")

        old_nodes = self.nodes.copy()
        for node in old_nodes:
            neighbors = old_nodes[node].edges

            if len(neighbors) == 2:
                neighbor_1, neighbor_2 = neighbors.keys()
                length_1, length_2 = neighbors.values()

                self.nodes[neighbor_1].add_edge(neighbor_2, length_1 + length_2)
                self.nodes[neighbor_2].add_edge(neighbor_1, length_1 + length_2)

                del self.nodes[neighbor_1].edges[node]
                del self.nodes[neighbor_2].edges[node]
                del self.nodes[node]

        print(f"Contracted edges - {len(self.nodes)} nodes remaining")


grid = {}
for i, line in enumerate(input):
    for j, val in enumerate(line):
        grid[(i, j)] = val

graph = Graph()
for p in grid:
    if grid[p] == "#":
        continue

    node = Node()
    for d in directions:
        neighbor = (p[0] + d[0], p[1] + d[1])

        if grid.get(neighbor, None) and grid[neighbor] in ".><v^":
            node.add_edge(neighbor, 1)

    graph.nodes[p] = node

n_rows = len(input)
n_cols = len(input[0])
start = (0, 1)
end = (n_rows - 1, n_cols - 2)

q: list[tuple[tuple[int, int], int, set]] = [(start, 0, set())]
hike_lengths = []

graph.contract_edges()

ans = 0
while q:
    p, length, seen = q.pop()

    if p == end:
        if length > ans:
            ans = length
            print(f"Found new longest length: {length}")

    for neighbor, edge_length in graph.nodes[p].edges.items():
        if neighbor not in seen:
            q.append((neighbor, length + edge_length, seen | set([neighbor])))

print(f"Longest hike: {ans}")
