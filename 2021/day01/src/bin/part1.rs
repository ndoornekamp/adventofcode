
fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    println!("Part 1 answer: {}", output);
}

fn part1(input: &str) -> i32 {
    input.lines()
        .map(|n| n.parse().unwrap())
        .collect::<Vec<u32>>()
        .windows(2)
        .filter(|w| w[0] < w[1])
        .count().try_into().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example() {
        let input = indoc!{"
            199
            200
            208
            210
            200
            207
            240
            269
            260
            263
        "};
        let result = part1(input);
        assert_eq!(result, 7);
    }
}