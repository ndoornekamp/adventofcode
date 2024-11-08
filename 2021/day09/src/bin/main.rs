use std::collections::{HashSet, VecDeque};

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input, true);
    println!("Part 1 answer: {}", output);

    let output = solve(input, false);
    println!("Part 2 answer: {}", output);
}

fn solve(input: &str, part1: bool) -> usize {
    let mut ans = 0;

    let grid: Vec<Vec<u32>> = input
        .lines()
        .map(|line| line.chars().map(|c| c.to_digit(10).unwrap()).collect())
        .collect();

    let nof_rows = grid.len();
    let nof_cols = grid[0].len();

    // i = row index
    // j = col index
    let mut low_points: Vec<(usize, usize)> = Vec::new();
    for i in 0..nof_rows {
        for j in 0..nof_cols {
            let height = grid[i][j];

            let mut neighbor_coordinates = Vec::new();
            if j > 0 {
                neighbor_coordinates.push((i, j - 1));
            }
            if i > 0 {
                neighbor_coordinates.push((i - 1, j));
            }
            if j < (nof_cols - 1) {
                neighbor_coordinates.push((i, j + 1));
            }
            if i < (nof_rows - 1) {
                neighbor_coordinates.push((i + 1, j));
            }

            let mut is_low_point: bool = true;
            for c in neighbor_coordinates {
                if grid[c.0][c.1] <= height {
                    is_low_point = false;
                    break;
                }
            }

            if is_low_point {
                low_points.push((i, j));
                ans += height + 1;
            }
        }
    }
    if part1 {
        return ans.try_into().unwrap();
    };

    let mut basin_sizes: Vec<usize> = Vec::new();
    let mut checked: HashSet<(usize, usize)> = HashSet::new();
    let directions: Vec<(isize, isize)> = Vec::from([(1, 0), (-1, 0), (0, 1), (0, -1)]);

    for low_point in low_points {
        let mut basin_size: usize = 0;
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
        queue.push_front(low_point);
        while !queue.is_empty() {
            let p = queue.pop_front().unwrap();

            if checked.contains(&p) {
                continue;
            } else {
                checked.insert(p);
                basin_size += 1;
            }

            for d in directions.iter() {
                let mut c: (isize, isize) = (0, 0);
                c.0 = (p.0 as isize) + d.0;
                c.1 = (p.1 as isize) + d.1;
                if 0 <= c.0
                    && c.0 < (nof_rows as isize)
                    && 0 <= c.1
                    && c.1 < (nof_cols as isize)
                    && grid[c.0 as usize][c.1 as usize] < 9
                {
                    queue.push_back((c.0 as usize, c.1 as usize));
                }
            }
            checked.insert(p);
        }
        basin_sizes.push(basin_size);
    }
    basin_sizes.sort();
    basin_sizes.pop().unwrap() * basin_sizes.pop().unwrap() * basin_sizes.pop().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_1() {
        let input = indoc! {"
            2199943210
            3987894921
            9856789892
            8767896789
            9899965678
        "};
        let result = solve(input, true);
        assert_eq!(result, 15);
    }

    #[test]
    fn example_part_2() {
        let input = indoc! {"
            2199943210
            3987894921
            9856789892
            8767896789
            9899965678
        "};
        let result = solve(input, false);
        assert_eq!(result, 1134);
    }
}
