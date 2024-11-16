use std::{cmp::Reverse, collections::BinaryHeap};

mod grid;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let one_by_one_grid = grid::Grid::from_txt(input);

    // 1x1 --> 1x5
    let mut new_rows: Vec<Vec<u32>> = Vec::new();
    for row in &one_by_one_grid.rows {
        let mut new_row = row.clone();
        for i in 1..=4 {
            for v in row.iter() {
                if v + i > 9 {
                    new_row.push(v + i - 9);
                } else {
                    new_row.push(v + i);
                }
            }
        }
        new_rows.push(new_row.clone());
    }

    // 1x5 --> 5x5
    let mut new_new_rows: Vec<Vec<u32>> = new_rows.clone();
    for i in 1..=4 {
        for row in new_rows.iter() {
            let mut new_new_row: Vec<u32> = Vec::new();
            for v in row.iter() {
                if v + i > 9 {
                    new_new_row.push(v + i - 9);
                } else {
                    new_new_row.push(v + i);
                }
            }
            new_new_rows.push(new_new_row);
        }
    }

    let grid = grid::Grid { rows: new_new_rows };

    // Dijkstra starting at top left (0, 0) ending at bottom right
    let mut visited = vec![vec![false; grid.nof_cols()]; grid.nof_rows()];
    let mut distances = vec![vec![usize::MAX; grid.nof_cols()]; grid.nof_rows()];
    let mut heap = BinaryHeap::new();

    distances[0][0] = 0;
    heap.push((Reverse(0), (0, 0)));

    while let Some((Reverse(distance_to_current_node), current_node)) = heap.pop() {
        if visited[current_node.0][current_node.1] {
            continue;
        }
        visited[current_node.0][current_node.1] = true;

        for neighbor in grid.manhattan_neighbors((current_node.0, current_node.1)) {
            let d = distance_to_current_node + grid.rows[neighbor.0][neighbor.1] as usize;

            if d < distances[neighbor.0][neighbor.1] {
                distances[neighbor.0][neighbor.1] = d;
                heap.push((Reverse(d), neighbor));
            }
        }
    }
    distances[grid.nof_rows() - 1][grid.nof_cols() - 1]
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_2() {
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
        assert_eq!(result, 315);
    }
}
