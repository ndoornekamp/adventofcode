fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    println!("Part 1 answer: {}", output);
}

fn part1(input: &str) -> usize {
    let number_of_characters_per_string: usize = input.lines().next().unwrap().len();
    let number_of_lines: usize = input.lines().count();
    let mut number_of_ones: Vec<usize> = vec![0; number_of_characters_per_string];

    for line in input.lines() {
        for (i, char) in line.chars().enumerate() {
            if char == '1' {
                number_of_ones[i] += 1;
            }
        }
    }

    let mut epsilon_bin = "".to_owned();
    let mut gamma_bin = "".to_owned();
    for count in number_of_ones {
        if count > number_of_lines - count {
            // 1 is the most common bit
            gamma_bin.push('1');
            epsilon_bin.push('0');
        } else {
            gamma_bin.push('0');
            epsilon_bin.push('1');
        }
    }

    let epsilon = usize::from_str_radix(&epsilon_bin, 2).unwrap();
    let gamma = usize::from_str_radix(&gamma_bin, 2).unwrap();

    epsilon * gamma
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
        let result = part1(input);
        assert_eq!(result, 198);
    }
}
