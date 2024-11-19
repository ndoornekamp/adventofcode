use regex::Regex;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 2 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let re = Regex::new(r"target area: x=(\d+)..(\d+), y=(-?\d+)..(-?\d+)").unwrap();
    let result = re.captures(input).unwrap();

    let x_min = result[1].parse::<isize>().unwrap();
    let x_max = result[2].parse::<isize>().unwrap();
    let y_min = result[3].parse::<isize>().unwrap();
    let y_max = result[4].parse::<isize>().unwrap();

    let mut ans = 0;

    for initial_dx in 0..200 {
        for initial_dy in -200..200 {
            let mut x = 0;
            let mut y = 0;

            let mut dx = initial_dx;
            let mut dy = initial_dy;

            loop {
                x += dx;
                y += dy;

                if dx > 0 {
                    dx -= 1
                }

                if dx < 0 {
                    dx += 1
                }

                dy -= 1;

                if x >= x_min && x <= x_max && y >= y_min && y <= y_max {
                    ans += 1;
                    break;
                }

                if y < y_min {
                    break;
                }

                if x > x_max {
                    break;
                }
            }
        }
    }
    ans as usize
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_2() {
        let input = indoc! {"
            target area: x=20..30, y=-10..-5
        "};
        let result = solve(input);
        assert_eq!(result, 112);
    }
}
