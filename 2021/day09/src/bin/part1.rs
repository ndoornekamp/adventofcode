fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let mut ans = 0;

    let grid: Vec<Vec<u32>> = input.lines().map(
        |line| line.chars().map(|c| c.to_digit(10).unwrap()).collect()
    ).collect();

    let nof_rows = grid.len();
    let nof_cols = grid[0].len();


    // i = row index
    // j = col index
    for i in 0 .. nof_rows {
        for j in 0 .. nof_cols {
            let height = grid[i][j];

            let mut neighbor_coordinates = Vec::new();
            if j > 0 {
                neighbor_coordinates.push((i, j-1));
            }
            if i > 0 {
                neighbor_coordinates.push((i-1, j));
            }
            if j < (nof_cols - 1) {
                neighbor_coordinates.push((i, j+1));
            }
            if i < (nof_rows - 1) {
                neighbor_coordinates.push((i+1, j));
            }

            let mut is_low_point: bool = true;
            for c in neighbor_coordinates {
                if grid[c.0][c.1] <= height {
                    is_low_point = false;
                    break;
                }
            }

            if is_low_point {
                ans += height + 1;
            }
        }
    }

    ans.try_into().unwrap()
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
        let result = solve(input);
        assert_eq!(result, 15);
    }
}
