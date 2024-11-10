use std::collections::HashSet;

mod graph;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> i32 {
    let mut graph = graph::Graph {
        nodes: HashSet::new(),
        edges: HashSet::new(),
    };
    for line in input.lines() {
        let start = line.split('-').next().unwrap();
        let end = line.split('-').nth(1).unwrap();

        graph.nodes.insert(start.to_string());
        graph.nodes.insert(end.to_string());
        graph.edges.insert((start.to_string(), end.to_string()));
        graph.edges.insert((end.to_string(), start.to_string()));
    }

    nof_paths_from_node("start".to_string(), &graph, 0, [].to_vec())
}

fn nof_paths_from_node(
    node: String,
    graph: &graph::Graph,
    _nof_paths: i32,
    path: Vec<String>,
) -> i32 {
    if node == "end" {
        let mut new_path = path.clone();
        new_path.push("end".to_string());
        return 1;
    } else if node == "start" && !path.is_empty() {
        return 0;
    } else if node.to_lowercase() == node && path.contains(&node) && path != ["start"].to_vec() {
        // dbg!(&node, &path);
        return 0;
    } else {
        let mut new_path = path.clone();
        new_path.push(node.clone());
        return graph
            .clone()
            .neighbors(node)
            .into_iter()
            .map(|n| nof_paths_from_node(n, graph, _nof_paths, new_path.clone()))
            .sum();
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_1_small() {
        let input = indoc! {"
            start-A
            start-b
            A-c
            A-b
            b-d
            A-end
            b-end
        "};
        let result = solve(input);
        assert_eq!(result, 10);
    }

    #[test]
    fn example_part_1_med() {
        let input = indoc! {"
            dc-end
            HN-start
            start-kj
            dc-start
            dc-HN
            LN-dc
            HN-end
            kj-sa
            kj-HN
            kj-dc
        "};
        let result = solve(input);
        assert_eq!(result, 19);
    }

    #[test]
    fn example_part_1_large() {
        let input = indoc! {"
            fs-end
            he-DX
            fs-he
            start-DX
            pj-DX
            end-zg
            zg-sl
            zg-pj
            pj-he
            RW-he
            fs-DX
            pj-RW
            zg-RW
            start-pj
            he-WI
            zg-he
            pj-fs
            start-RW
        "};
        let result = solve(input);
        assert_eq!(result, 226);
    }
}
