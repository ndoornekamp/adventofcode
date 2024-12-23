from collections import defaultdict
from itertools import combinations
from textwrap import dedent


def solve(input: str) -> int:
    edges = set()
    for connection in input.strip().split("\n"):
        edges.add((connection[:2], connection[3:]))

    connected_to = defaultdict(set)
    for edge in edges:
        connected_to[edge[0]].add(edge[1])
        connected_to[edge[1]].add(edge[0])

    ans = set()
    for node, neighbors in connected_to.items():
        if node.startswith("t") and len(neighbors) > 1:
            # Found node starting with t that has at least 2 neighbors, now we just need to know which of these
            # neighbors are interconnected
            for (n1, n2) in combinations(neighbors, 2):
                if n1 in connected_to[n2]:
                    print(node, n1, n2)
                    ans.add(frozenset((node, n1, n2)))  # TODO: smarter way to not add group of three twice?

    return len(ans)


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
    assert solve(input) == 7


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
