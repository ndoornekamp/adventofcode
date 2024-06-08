use std::{cmp, collections::HashMap};

fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    println!("Part 1 answer: {}", output);
}

#[derive(Clone, Debug)]
struct Line {
    x1: u16,
    y1: u16,
    x2: u16,
    y2: u16,
}

fn parse_lines(input: &str) -> Vec<Line> {
    let mut lines: Vec<Line> = [].to_vec();

    for line in input.lines() {
        let mut start_end = line.split(" -> ");
        let mut start_coordinate = start_end.next().unwrap().split(',');
        let mut end_coordinate = start_end.next().unwrap().split(',');

        lines.push(Line {
            x1: start_coordinate.next().unwrap().parse().unwrap(),
            y1: start_coordinate.next().unwrap().parse().unwrap(),
            x2: end_coordinate.next().unwrap().parse().unwrap(),
            y2: end_coordinate.next().unwrap().parse().unwrap(),
        });
    }

    lines
}

fn part1(input: &str) -> usize {
    let lines = parse_lines(input);
    let mut coordinates_hit: Vec<(u16, u16)> = [].to_vec();

    for line in lines.iter() {
        if line.x1 == line.x2 {  // Vertical line
            for y in cmp::min(line.y1, line.y2)..=cmp::max(line.y2, line.y1) {
                coordinates_hit.push((line.x1, y));
            }
        } else if line.y1 == line.y2 {  // Horizontal line
            for x in cmp::min(line.x1, line.x2)..=cmp::max(line.x1, line.x2) {
                coordinates_hit.push((x, line.y1));
            }
        } else {
            // dbg!("Ignoring line as it is not horizontal or vertical", line);
            continue;
        }
    }

    let mut count_per_coordinate: HashMap<(u16, u16), u16> = HashMap::new();
    for coordinate in coordinates_hit {
        *count_per_coordinate.entry(coordinate).or_default() += 1;
    }

    count_per_coordinate.retain(|_, count| count > &mut 1);
    count_per_coordinate.len()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example() {
        let input = indoc! {"
            0,9 -> 5,9
            8,0 -> 0,8
            9,4 -> 3,4
            2,2 -> 2,1
            7,0 -> 7,4
            6,4 -> 2,0
            0,9 -> 2,9
            3,4 -> 1,4
            0,0 -> 8,8
            5,5 -> 8,2"};
        let result = part1(input);
        assert_eq!(result, 5);
    }
}
