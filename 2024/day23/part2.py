from collections import defaultdict
from itertools import combinations
from textwrap import dedent


def solve(input: str) -> str:
    edges = set()
    for connection in input.strip().split("\n"):
        edges.add((connection[:2], connection[3:]))

    connected_to = defaultdict(set)
    for edge in edges:
        connected_to[edge[0]].add(edge[1])
        connected_to[edge[1]].add(edge[0])

    n_connections_per_node = len(connected_to[edge[0]])
    # Turns out all nodes have the same number of connections. Therefore, the biggest group of interconnected nodes
    # can be at most this big
    assert all(len(connections) == n_connections_per_node for connections in connected_to.values())

    # Pick a node and check if all <max_group_size> nodes are interconnected
    for max_group_size in range(n_connections_per_node, 1, -1):
        for node, neighbors in connected_to.items():
            for neighbor_subset in combinations(neighbors, max_group_size):
                interconnected = True
                for n1, n2 in combinations(neighbor_subset, 2):
                    if n1 not in connected_to[n2]:
                        interconnected = False
                        break

                if interconnected:
                    return ",".join(sorted(list(neighbor_subset) + [node]))

    raise Exception("Did not terminate")


def test_solve():
    input = dedent("""
        kh-tc
        qp-kh
        de-cg
        ka-co
        yn-aq
        qp-ub
        cg-tb
        vc-aq
        tb-ka
        wh-tc
        yn-cg
        kh-ub
        ta-co
        de-co
        tc-td
        tb-wq
        wh-td
        ta-ka
        td-qp
        aq-cg
        wq-ub
        ub-vc
        de-ta
        wq-aq
        wq-vc
        wh-yn
        ka-de
        kh-ta
        co-tc
        wh-qp
        tb-vc
        td-yn
    """)
    assert solve(input) == "co,de,ka,ta"


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
