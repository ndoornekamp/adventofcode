from collections import namedtuple
import heapq
from textwrap import dedent
from itertools import combinations
import math
import networkx as nx

Box = namedtuple("Box", ["x", "y", "z"])


def solve(input: str) -> int:
    boxes: list[tuple[int, int, int]] = []
    for line in input.strip().split("\n"):
        x, y, z = line.split(",")
        boxes.append((int(x), int(y), int(z)))

    all_possible_connections = sorted(list(combinations(boxes, 2)), key=lambda x: math.dist(x[0], x[1]))
    connections, connected = set(), set()
    for connection in all_possible_connections:
        connections.add(connection)
        connected.add(connection[0])
        connected.add(connection[1])
        if len(connected) == len(boxes):  # Only start checking the circuits once all boxes are connected at least once
            G = nx.Graph()
            G.add_edges_from([(str(tuple(c)[0]), str(tuple(c)[1])) for c in all_possible_connections])
            n_components = len(list(nx.connected_components(G)))

            if n_components == 1:
                # It could be that all boxes have a connection, but there are still multiple circuits. In that case,
                # keep adding connections until we have only one component
                return connection[0][0] * connection[1][0]


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
    assert solve(input) == 25272


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
