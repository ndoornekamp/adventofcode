use std::collections::HashMap;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let mut ans = 0;
    let opening_brackets = ['(', '[', '{', '<'];
    let score = HashMap::from([(')', 3), (']', 57), ('}', 1197), ('>', 25137)]);

    for line in input.lines() {
        let mut stack: Vec<char> = Vec::new();
        for char in line.chars() {
            if opening_brackets.contains(&char) {
                stack.push(char.clone());
            } else {
                let top_char = stack.pop();
                match top_char {
                    Some(v) => {
                        match v {
                            '(' => {
                                if char != ')' {
                                    println!("Expected ), got {}", char);
                                    ans += score[&char];
                                }
                            }
                            '[' => {
                                if char != ']' {
                                    println!("Expected ], got {}", char);
                                    ans += score[&char];
                                }
                            }
                            '{' => {
                                if char != '}' {
                                    println!("Expected curly, got {}", char);
                                    ans += score[&char];
                                }
                            }
                            '<' => {
                                if char != '>' {
                                    println!("Expected >, got {}", char);
                                    ans += score[&char];
                                }
                            }
                            _ => panic!("Unhandled exception"),
                        }
                    }
                    None => {
                        println!("There are no more characters in the stack --> This string is OK");
                    }
                }
            }
        }
    }
    ans
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
        assert_eq!(result, 26397);
    }
}
