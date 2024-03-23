
fn main() {
    let input = include_str!("./input.txt");
    let output = part2(input);
    println!("Part 2 answer: {}", output);
}

fn part2(input: &str) -> i32 {
    let sums: Vec<i32> = input.lines()
        .map(|n| n.parse().unwrap())
        .collect::<Vec<i32>>()
        .windows(3)
        .map(|w| w.iter().sum()).collect();

    sums.windows(2)
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
        let result = part2(input);
        assert_eq!(result, 5);
    }
}