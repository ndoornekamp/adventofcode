use itertools::Itertools;
use std::collections::HashMap;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let mut input_parts = input.split("\n\n");

    let template = input_parts.next().unwrap().to_string();
    let rules: HashMap<String, String> = HashMap::from_iter(
        input_parts
            .next()
            .unwrap()
            .lines()
            .map(|l| {
                (
                    l.split(" -> ").next().unwrap().to_string(),
                    l.split(" -> ").nth(1).unwrap().to_string(),
                )
            })
            .collect::<Vec<(String, String)>>(),
    );

    let mut polymer = template;
    for _step in 1..=10 {
        let mut new_polymer: String = "".to_string();
        new_polymer.push_str(&polymer[0..=0]);
        for idx in 0..polymer.len() - 1 {
            let pair = &polymer[idx..=idx + 1];
            new_polymer.push_str(&rules[pair]);
            new_polymer.push_str(&polymer[idx + 1..=idx + 1]);
        }
        polymer = new_polymer.clone();
    }
    let character_counts = polymer.chars().counts();
    let minmax = &character_counts
        .into_iter()
        .minmax_by(|a, b| a.1.cmp(&b.1))
        .into_option()
        .unwrap();

    minmax.1.1 - minmax.0.1
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_1() {
        let input = indoc! {"
            NNCB

            CH -> B
            HH -> N
            CB -> H
            NH -> C
            HB -> C
            HC -> B
            HN -> C
            NN -> C
            BH -> H
            NC -> B
            NB -> B
            BN -> B
            BB -> N
            BC -> B
            CC -> N
            CN -> C
        "};
        let result = solve(input);
        assert_eq!(result, 1588);
    }
}
