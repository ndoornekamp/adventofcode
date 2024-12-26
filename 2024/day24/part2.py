import networkx
from ipysigma import Sigma


def solve(input: str) -> str:
    _, gates_str = input.strip().split("\n\n")

    graph = networkx.DiGraph()
    for line in gates_str.split("\n"):
        rule, out = line.split(" -> ")
        in1, operand, in2 = rule.split(" ")

        color = "blue" if operand == "AND" else "green" if operand == "OR" else "red"
        graph.add_node(out, label=out, color=color)
        graph.add_edge(in1, out, label=operand)
        graph.add_edge(in2, out, label=operand)

    # Things get a bit hand-wavy here: make a plot of the graph and look for deviations from the pattern
    Sigma(
        graph,
        height=1000,
        default_edge_type="arrow",
        start_layout=True,
        default_edge_size=3,
        default_node_size=3,
    ).to_html("graph.html")

    # Per deviation from the pattern (which are somewhat obvious from looking at the graph), the two nodes
    # added to the list below are the two nodes that should be swapped to conform to the pattern
    nodes_deviating_from_pattern = ["grm", "z32", "ndw", "jcb", "twr", "z39", "ggn", "z10"]
    return ",".join(list(sorted(nodes_deviating_from_pattern)))


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
