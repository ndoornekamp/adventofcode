use std::collections::HashSet;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 2 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let mut ans: usize = 0;
    for line in input.lines() {
        let mut out = String::new();
        let mut line_splits = line.split(" | ");
        let patterns: Vec<&str> = line_splits.next().unwrap().split_whitespace().collect();
        let output_values: Vec<&str> = line_splits.next().unwrap().split_whitespace().collect();

        let chars_one: HashSet<char> = get_char_set(&patterns, 2);
        let chars_seven: HashSet<char> = get_char_set(&patterns, 3);
        let chars_four: HashSet<char> = get_char_set(&patterns, 4);

        for v in output_values.iter() {
            if v.len() == 2 {
                out.push_str("1");
            } else if v.len() == 3 {
                out.push_str("7");
            } else if v.len() == 4 {
                out.push_str("4");
            } else if v.len() == 5 {
                let v_chars: HashSet<char> = v.chars().collect();
                if chars_one.is_subset(&v_chars) {
                    out.push_str("3");
                } else if chars_four.intersection(&v_chars).count() == 2 {
                    out.push_str("2");
                } else {
                    out.push_str("5");
                }
            } else if v.len() == 6 {
                let v_chars: HashSet<char> = v.chars().collect();
                if chars_four.is_subset(&v_chars) {
                    out.push_str("9");
                } else if chars_seven.is_subset(&v_chars) {
                    out.push_str("0");
                } else {
                    out.push_str("6");
                }
            } else {
                out.push_str("8");
            }
        }
        ans += out.parse::<usize>().unwrap();
    }

    return ans;
}

fn get_char_set(strings: &Vec<&str>, length: usize) -> HashSet<char> {
    strings
        .iter()
        .filter(|p| p.len() == length)
        .next()
        .unwrap()
        .chars()
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_2() {
        let input = indoc! {"
            be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
            edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
            fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
            fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
            aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
            fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
            dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
            bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
            egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
            gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
        "};
        let result = solve(input);
        assert_eq!(result, 61229);
    }
}
