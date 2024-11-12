use std::collections::HashMap;

use itertools::Itertools;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input, 40);
    println!("Part 2 answer: {}", output);
}

fn solve(input: &str, nof_steps: usize) -> u64 {
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

    let mut pairs: HashMap<String, u64> = HashMap::new();
    for idx in 0..template.len() - 1 {
        pairs
            .entry(template[idx..=idx + 1].to_string())
            .and_modify(|count| *count += 1)
            .or_insert(1);
    }

    for _step in 1..=nof_steps {
        let mut new_pairs: HashMap<String, u64> = HashMap::new();
        for p in pairs {
            let first_new_pair = format!("{}{}", &p.0[0..=0], &rules[&p.0]);
            new_pairs
                .entry(first_new_pair)
                .and_modify(|count| *count += p.1)
                .or_insert(p.1);

            let second_new_pair = format!("{}{}", &rules[&p.0], &p.0[1..=1]);
            new_pairs
                .entry(second_new_pair)
                .and_modify(|count| *count += p.1)
                .or_insert(p.1);
        }
        pairs = new_pairs;
    }

    let mut character_counts: HashMap<char, u64> = HashMap::new();
    for pair in pairs {
        for c in pair.0.chars() {
            character_counts
                .entry(c)
                .and_modify(|count| *count += pair.1)
                .or_insert(pair.1);
        }
    }
    character_counts
        .entry(template.chars().next().unwrap())
        .and_modify(|count| *count += 1);
    character_counts
        .entry(template.chars().last().unwrap())
        .and_modify(|count| *count += 1);

    let minmax = &character_counts
        .iter()
        .minmax_by(|a, b| a.1.cmp(b.1))
        .into_option()
        .unwrap();
    minmax.1.1 / 2 - minmax.0.1 / 2
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
        let result = solve(input, 10);
        assert_eq!(result, 1588);
    }

    #[test]
    fn example_part_2() {
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
        let result = solve(input, 40);
        assert_eq!(result, 2188189693529);
    }
}
