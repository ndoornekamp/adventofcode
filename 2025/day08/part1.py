from collections import namedtuple
import heapq
from textwrap import dedent
from itertools import combinations
import math
import networkx as nx

Box = namedtuple("Box", ["x", "y", "z"])


def solve(input: str, n_connections: int) -> int:
    boxes: list[tuple[int, int, int]] = []
    for line in input.strip().split("\n"):
        x, y, z = line.split(",")
        boxes.append((int(x), int(y), int(z)))

    connections = sorted(list(combinations(boxes, 2)), key=lambda x: math.dist(x[0], x[1]))[:n_connections]

    G = nx.Graph()
    G.add_edges_from([(str(c[0]), str(c[1])) for c in connections])

    circuit_lengths = [len(c) for c in nx.connected_components(G)]
    top_3_sizes = heapq.nlargest(3, circuit_lengths)

    return math.prod(top_3_sizes)


def test_solve():
    input = dedent("""
        162,817,812
        57,618,57
        906,360,560
        592,479,940
        352,342,300
        466,668,158
        542,29,236
        431,825,988
        739,650,466
        52,470,668
        216,146,977
        819,987,18
        117,168,530
        805,96,715
        346,949,466
        970,615,88
        941,993,340
        862,61,35
        984,92,344
        425,690,689
    """)
    assert solve(input, 10) == 40


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input, 1000)
    print(ans)
