use std::cmp::{max, min};

use ndarray::Array3;
use regex::Regex;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let re =
        Regex::new(r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)").unwrap();
    let mut instructions: Vec<Instruction> = vec![];

    for line in input.lines() {
        let captures = re.captures(line).unwrap();

        // Shift the whole cube so (x_min, y_min, z_min) = (0, 0, 0)
        let x_min = captures[2].parse::<isize>().unwrap() + 50;
        let x_max = captures[3].parse::<isize>().unwrap() + 50;
        let y_min = captures[4].parse::<isize>().unwrap() + 50;
        let y_max = captures[5].parse::<isize>().unwrap() + 50;
        let z_min = captures[6].parse::<isize>().unwrap() + 50;
        let z_max = captures[7].parse::<isize>().unwrap() + 50;

        if x_min > 101 || x_max < 0 || y_min > 101 || y_max < 0 || z_min > 101 || z_max < 0 {
            continue;  // Ignore instructions outside our area of interest
        }

        let instruction = Instruction {
            on_off: captures[1].to_string(),
            x_min: max(x_min, 0) as usize,
            x_max: min(x_max, 100) as usize,
            y_min: max(y_min, 0) as usize,
            y_max: min(y_max, 100) as usize,
            z_min: max(z_min, 0) as usize,
            z_max: min(z_max, 100) as usize,
        };

        instructions.push(instruction);
    }

    let mut grid = Array3::<usize>::zeros((101, 101, 101));

    for instruction in instructions {
        let mut val = 0;
        if instruction.on_off == "on" {
            val = 1;
        }
        for x in instruction.x_min..=instruction.x_max {
            for y in instruction.y_min..=instruction.y_max {
                for z in instruction.z_min..=instruction.z_max {
                    grid[[x as usize, y as usize, z as usize]] = val;
                }
            }
        }
    }

    grid.sum()
}

#[derive(Debug)]
struct Instruction {
    on_off: String,
    x_min: usize,
    x_max: usize,
    y_min: usize,
    y_max: usize,
    z_min: usize,
    z_max: usize,
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_1() {
        let input = indoc! {"
            on x=10..12,y=10..12,z=10..12
            on x=11..13,y=11..13,z=11..13
            off x=9..11,y=9..11,z=9..11
            on x=10..10,y=10..10,z=10..10
        "};
        let result = solve(input);
        assert_eq!(result, 39);
    }

    #[test]
    fn example_part_1_large() {
        let input = indoc! {"
            on x=-20..26,y=-36..17,z=-47..7
            on x=-20..33,y=-21..23,z=-26..28
            on x=-22..28,y=-29..23,z=-38..16
            on x=-46..7,y=-6..46,z=-50..-1
            on x=-49..1,y=-3..46,z=-24..28
            on x=2..47,y=-22..22,z=-23..27
            on x=-27..23,y=-28..26,z=-21..29
            on x=-39..5,y=-6..47,z=-3..44
            on x=-30..21,y=-8..43,z=-13..34
            on x=-22..26,y=-27..20,z=-29..19
            off x=-48..-32,y=26..41,z=-47..-37
            on x=-12..35,y=6..50,z=-50..-2
            off x=-48..-32,y=-32..-16,z=-15..-5
            on x=-18..26,y=-33..15,z=-7..46
            off x=-40..-22,y=-38..-28,z=23..41
            on x=-16..35,y=-41..10,z=-47..6
            off x=-32..-23,y=11..30,z=-14..3
            on x=-49..-5,y=-3..45,z=-29..18
            off x=18..30,y=-20..-8,z=-3..13
            on x=-41..9,y=-7..43,z=-33..15
            on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
            on x=967..23432,y=45373..81175,z=27513..53682
        "};
        let result = solve(input);
        assert_eq!(result, 590784);
    }
}
