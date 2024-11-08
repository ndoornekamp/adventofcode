use std::collections::HashMap;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 2 answer: {}", output);
}

fn solve(input: &str) -> i64 {
    let mut line_scores: Vec<i64> = Vec::new();
    let opening_brackets = ['(', '[', '{', '<'];
    let score = HashMap::from([('(', 1), ('[', 2), ('{', 3), ('<', 4)]);

    for line in input.lines() {
        let mut stack: Vec<char> = Vec::new();
        let mut is_corrupt: bool = false;
        for char in line.chars() {
            if opening_brackets.contains(&char) {
                stack.push(char.clone());
            } else {
                let top_char = stack.pop();
                match top_char {
                    Some(v) => match v {
                        '(' => {
                            if char != ')' {
                                is_corrupt = true;
                                break;
                            }
                        }
                        '[' => {
                            if char != ']' {
                                is_corrupt = true;
                                break;
                            }
                        }
                        '{' => {
                            if char != '}' {
                                is_corrupt = true;
                                break;
                            }
                        }
                        '<' => {
                            if char != '>' {
                                is_corrupt = true;
                                break;
                            }
                        }
                        _ => panic!("Unhandled exception"),
                    },
                    None => {
                        println!("There are no more characters in the stack --> This string is OK");
                    }
                }
            }
        }
        if !is_corrupt {
            let mut line_score: i64 = 0;
            stack.reverse();
            for char in stack {
                line_score = line_score * 5;
                line_score += score[&char];
            }
            line_scores.push(line_score);
        }
    }
    line_scores.sort();
    let median_idx = line_scores.len() / 2;
    line_scores[median_idx]
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_1() {
        let input = indoc! {"
            [({(<(())[]>[[{[]{<()<>>
            [(()[<>])]({[<{<<[]>>(
            {([(<{}[<>[]}>{[]{[(<()>
            (((({<>}<{<{<>}{[]{[]{}
            [[<[([]))<([[{}[[()]]]
            [{[{({}]{}}([{[{{{}}([]
            {<[[]]>}<{[{[{[]{()[[[]
            [<(<(<(<{}))><([]([]()
            <{([([[(<>()){}]>(<<{{
            <{([{{}}[<[[[<>{}]]]>[]]
        "};
        let result = solve(input);
        assert_eq!(result, 288957);
    }
}
