use std::cmp;

use regex::Regex;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let numbers_1 = input.lines();
    let mut ans = 0;

    for (i, number1) in numbers_1.enumerate() {
        let numbers_2 = input.lines();
        for (j, number2) in numbers_2.enumerate() {
            if i == j {
                continue;
            }

            let magnitude = magnitude(&add(number1, number2));
            if magnitude > ans {
                ans = magnitude;
                println!(
                    "Found new best magnitude: {} by adding numbers {} and {}",
                    &ans,
                    i + 1,
                    j + 1
                );
            }
        }
    }

    ans
}

fn add(n1: &str, n2: &str) -> String {
    let added = format!("[{},{}]", n1, n2);
    // dbg!(format!("after addition: {}", &added));
    reduce(&added)
}

fn reduce(number: &str) -> String {
    let mut reduced_number = number.to_string();
    loop {
        let (exploded, exploded_number) = explode(&reduced_number);
        reduced_number = exploded_number.to_string();
        if exploded {
            // dbg!(format!("after explode:  {}", &reduced_number));
            continue;
        }

        let (split, split_number) = split(&reduced_number);
        reduced_number = split_number.to_string();
        if split {
            // dbg!(format!("after split:    {}", &reduced_number));
            continue;
        }
        break;
    }
    reduced_number.to_string()
}

fn explode(number: &str) -> (bool, String) {
    let mut n_nested_pairs = 0;
    let mut nested_pair_start_idx: Option<usize> = None;
    for (i, c) in number.char_indices() {
        if c == '[' {
            n_nested_pairs += 1
        } else if c == ']' {
            n_nested_pairs -= 1
        }

        if n_nested_pairs > 4 {
            nested_pair_start_idx = Some(i);
            break;
        }
    }

    match nested_pair_start_idx {
        Some(idx) => {
            let re = Regex::new(r"\[(\d+),(\d+)\]").unwrap();
            let haystack = &number[idx..cmp::min(idx + 10, number.len())];
            let caps = re.captures(haystack).unwrap();

            let left_digit = &caps[1].parse::<usize>().unwrap();
            let right_digit = &caps[2].parse::<usize>().unwrap();

            // If the addition of `left_digit` to the last number left of it increases the number of digits in that
            // number, the index where the pair currently being exploded starts, changes.
            let mut split_offset = 0;

            // add left digit to last digit to the left of left digit
            let mut new_number = number.to_string();
            let mut len = 1;
            for (i, c) in number.char_indices().rev() {
                if i > idx {
                    continue;
                }

                if c.is_ascii_digit() {
                    let mut val = c.to_digit(10).unwrap() as usize;
                    if i > 0 && number.chars().nth(i - 1).unwrap().is_ascii_digit() {
                        val = number[i - 1..=i].parse().unwrap();
                        len = 2;
                    }

                    let (s, mut e) = number.split_at(i - len + 1);
                    e = &e[len..e.len()];
                    new_number = format!("{}{}{}", s, val + left_digit, e);

                    if val <= 9 && val + left_digit > 9 {
                        split_offset = 1;
                        len = 2;
                    }

                    break;
                }
            }

            // add right digit to first digit to the right of right digit
            let mut new_new_number = new_number.to_string();
            for (i, c) in new_number.char_indices() {
                if i <= (idx + 3 + len + split_offset) {
                    continue;
                }

                if c.is_ascii_digit() {
                    let mut val = c.to_digit(10).unwrap() as usize;
                    let mut len = 1;
                    if i + 1 < new_number.len()
                        && new_number.chars().nth(i + 1).unwrap().is_ascii_digit()
                    {
                        val = new_number[i..=i + 1].parse().unwrap();
                        len = 2;
                    }

                    let (s, mut e) = new_number.split_at(i);
                    e = &e[len..e.len()];
                    new_new_number = format!("{}{}{}", s, val + right_digit, e);

                    break;
                }
            }

            // update `number`: replace the (first occurence of) `pair` with 0
            let (s, mut e) = new_new_number.split_at(idx + split_offset);
            e = &e[caps[0].len()..e.len()];
            new_new_number = format!("{}{}{}", s, 0, e);

            (true, new_new_number)
        }
        None => (false, number.to_string()),
    }
}

fn split(number: &str) -> (bool, String) {
    let re = Regex::new(r"\d{2}").unwrap();
    let mut numbers_to_split = re.find_iter(number);
    let leftmost_match = numbers_to_split.next();

    match leftmost_match {
        Some(m) => {
            let value = m.as_str().parse::<usize>().unwrap();
            let (s, _) = number.split_at(m.start());
            let (_, e) = number.split_at(m.end());
            (
                true,
                format!("{}[{},{}]{}", s, value / 2, value - (value / 2), e),
            )
        }
        None => (false, number.to_string()),
    }
}

fn magnitude(number: &str) -> usize {
    let re = Regex::new(r"\[(\d+),(\d+)\]").unwrap();

    let mut new_number = number.to_string();
    loop {
        let caps = re.captures(&new_number);
        match caps {
            Some(c) => {
                let left_digit = &c[1].parse::<usize>().unwrap();
                let right_digit = &c[2].parse::<usize>().unwrap();
                let pair_value = (3 * left_digit + 2 * right_digit).to_string();
                new_number = re.replace(&new_number, pair_value).to_string();
            }
            None => {
                break;
            }
        }
    }
    new_number.parse::<usize>().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_2() {
        let input = indoc! {"
            [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
            [[[5,[2,8]],4],[5,[[9,9],0]]]
            [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
            [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
            [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
            [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
            [[[[5,4],[7,7]],8],[[8,3],8]]
            [[9,3],[[9,9],[6,[4,9]]]]
            [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
            [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
        "};
        let result = solve(input);
        assert_eq!(result, 3993);
    }
}
