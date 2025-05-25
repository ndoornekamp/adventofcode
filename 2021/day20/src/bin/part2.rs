use std::collections::HashSet;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 2 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let mut lines = input.lines();
    let algorithm = lines.next().unwrap();

    lines.next().unwrap(); // empty line

    let mut light_pixels: HashSet<(i32, i32)> = HashSet::new();
    for (row_idx, line) in lines.enumerate() {
        for (col_idx, char) in line.char_indices() {
            if char == '#' {
                light_pixels.insert((row_idx as i32, col_idx as i32));
            }
        }
    }

    // The infinite background starts as dark, but if the algorithm maps 9 dark pixels to light, that will change.
    let mut background = '.';

    for _ in 0..50 {
        let (new_pixels, new_background) = apply_algorithm(&algorithm, &light_pixels, background);
        light_pixels = new_pixels;
        background = new_background;
    }

    light_pixels.len()
}

fn apply_algorithm(
    algorithm: &str,
    light_pixels: &HashSet<(i32, i32)>,
    background: char,
) -> (HashSet<(i32, i32)>, char) {
    let min_row = light_pixels.iter().map(|&(r, _)| r).min().unwrap();
    let max_row = light_pixels.iter().map(|&(r, _)| r).max().unwrap();
    let min_col = light_pixels.iter().map(|&(_, c)| c).min().unwrap();
    let max_col = light_pixels.iter().map(|&(_, c)| c).max().unwrap();

    let mut new_light_pixels = HashSet::new();
    for row in (min_row - 1)..=(max_row + 1) {
        for col in (min_col - 1)..=(max_col + 1) {
            let mut index = 0;
            let mut binary_string = String::new();
            for dr in -1..=1 {
                for dc in -1..=1 {
                    index <<= 1;
                    let pos = (row + dr, col + dc);
                    let bit = if row + dr < min_row
                        || row + dr > max_row
                        || col + dc < min_col
                        || col + dc > max_col
                    {
                        background
                    } else if light_pixels.contains(&pos) {
                        '#'
                    } else {
                        '.'
                    };

                    if bit == '#' {
                        binary_string.push('1');
                    } else {
                        binary_string.push('0');
                    }
                }
            }
            index = usize::from_str_radix(&binary_string, 2).unwrap();

            if algorithm.chars().nth(index).unwrap() == '#' {
                new_light_pixels.insert((row, col));
            }
        }
    }

    // Update background: if it was dark, it becomes light if the algorithm maps 9 dark pixels to light; dark otherwise
    let new_background: char = if background == '.' {
        if algorithm.chars().nth(0).unwrap() == '#' {
            '#'
        } else {
            '.'
        }
    } else {
        // If the background was light, it remains light if the algorithm maps 9 light pixels to light; dark otherwise
        if algorithm.chars().last().unwrap() == '#' {
            '#'
        } else {
            '.'
        }
    };

    (new_light_pixels, new_background)
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_2() {
        let input = indoc! {"
            ..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

            #..#.
            #....
            ##..#
            ..#..
            ..###
        "};
        let result = solve(input);
        assert_eq!(result, 3351);
    }
}
