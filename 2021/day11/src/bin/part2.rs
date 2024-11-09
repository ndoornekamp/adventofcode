mod grid;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 2 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let mut grid = grid::Grid::from_txt(input);

    let mut all_flashed: bool = false;
    let mut steps = 0;
    while !all_flashed {
        for row in grid.rows.iter_mut() {
            for c in row.iter_mut() {
                *c += 1;
            }
        }

        let mut going: bool = true;
        let mut nof_flashes_this_step = 0;
        while going {
            going = false;
            for r in 0..grid.nof_rows() {
                for c in 0..grid.nof_cols() {
                        if grid.rows[r][c] > 9 {
                            nof_flashes_this_step += 1;
                            grid.rows[r][c] = 0;

                            for n in grid.neighbors((r, c)) {
                                if grid.rows[n.0][n.1] > 0 {
                                    grid.rows[n.0][n.1] += 1;
                                    going = true;
                                }
                            }
                        }
                    }
                }
        }
        all_flashed = nof_flashes_this_step == 100;
        steps += 1;
    }
    steps
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_2() {
        let input = indoc! {"
            5483143223
            2745854711
            5264556173
            6141336146
            6357385478
            4167524645
            2176841721
            6882881134
            4846848554
            5283751526
        "};
        let result = solve(input);
        assert_eq!(result, 195);
    }
}
