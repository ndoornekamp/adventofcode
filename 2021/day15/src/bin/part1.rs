use std::collections::{HashMap, HashSet};

mod grid;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let grid = grid::Grid::from_txt(input);

    let mut nodes: HashSet<(usize, usize)> = HashSet::new();
    for r in 0..grid.nof_rows() {
        for c in 0..grid.nof_cols() {
            nodes.insert((r, c));
        }
    }

    let mut unvisited_nodes = nodes.clone();
    let mut distances: HashMap<(usize, usize), usize> = unvisited_nodes
        .iter()
        .map(|n| ((n.0, n.1), usize::MAX))
        .collect();

    let mut current_node: (usize, usize) = (0, 0);
    distances.insert(current_node, 0);

    loop {
        unvisited_nodes.remove(&current_node);

        if unvisited_nodes.is_empty() {
            break;
        }

        for neighbor in grid.manhattan_neighbors(current_node) {
            let d =
                distances.get(&current_node).unwrap() + grid.rows[neighbor.0][neighbor.1] as usize;

            if d < *distances.get(&neighbor).unwrap() {
                distances.insert(neighbor, d);
            }
        }

        let mut next_node_distance = usize::MAX;
        for node in &unvisited_nodes {
            if distances.get(node).unwrap() < &next_node_distance {
                current_node = *node;
                next_node_distance = *distances.get(node).unwrap();
            }
        }
    }
    *distances.get(&(grid.nof_rows() - 1, grid.nof_cols() - 1)).unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_1() {
        let input = indoc! {"
            1163751742
            1381373672
            2136511328
            3694931569
            7463417111
            1319128137
            1359912421
            3125421639
            1293138521
            2311944581
        "};
        let result = solve(input);
        assert_eq!(result, 40);
    }
}
