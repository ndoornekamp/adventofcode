fn main() {
    let input = include_str!("./input.txt");
    let output = part2(input);
    println!("Part 2 answer: {}", output);
}

fn calculate_rating(
    input: &str,
    filter_if_1_is_more_common: char,
    filter_if_0_is_most_common: char,
) -> &str {
    let mut nof_lines: usize = input.lines().count();
    let mut lines: Vec<&str> = input.lines().collect();  // .collect() for Lines<> to Vec<>
    let mut going = true;
    let mut idx = 0;

    while going {
        let nof_ones = lines
            .iter()
            .filter(|l| l.chars().nth(idx).unwrap() == '1')
            .count();

        if nof_ones >= nof_lines - nof_ones {
            // .retain() filters in-place
            lines.retain(|l| l.chars().nth(idx).unwrap() == filter_if_1_is_more_common);
        } else {
            lines.retain(|l| l.chars().nth(idx).unwrap() == filter_if_0_is_most_common);
        }

        if lines.len() == 1 {
            going = false;
        }
        idx += 1;
        nof_lines = lines.len();
    }

    lines.into_iter().next().unwrap()
}

fn part2(input: &str) -> usize {
    let oxygen_bin = calculate_rating(input, '1', '0');
    let co2_bin = calculate_rating(input, '0', '1');

    let oxygen_system_rating = usize::from_str_radix(oxygen_bin, 2).unwrap();
    let co2_scrubber_rating = usize::from_str_radix(co2_bin, 2).unwrap();

    dbg!(oxygen_system_rating, co2_scrubber_rating);

    co2_scrubber_rating * oxygen_system_rating
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example() {
        let input = indoc! {"
            00100
            11110
            10110
            10111
            10101
            01111
            00111
            11100
            10000
            11001
            00010
            01010
        "};
        let result = part2(input);
        assert_eq!(result, 230);
    }
}
