fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    println!("Part 1 answer: {}", output);
}

fn part1(input: &str) -> i32 {
    let mut horizontal: i32 = 0;
    let mut vertical: i32 = 0;

    for line in input.lines() {
        let mut split = line.split_whitespace();
        let direction: &str = split.next().expect("");
        let distance: i32 = split.next().expect("").parse().unwrap();

        if direction == "forward" {
            horizontal += distance;
        } else if direction == "down" {
            vertical += distance;
        } else {
            vertical -= distance;
        }
    }
    vertical * horizontal
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example() {
        let input = indoc! {"
            forward 5
            down 5
            forward 8
            up 3
            down 8
            forward 2
        "};
        let result = part1(input);
        assert_eq!(result, 150);
    }
}
