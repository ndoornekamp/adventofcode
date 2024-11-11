fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> i32 {
    let mut input_parts = input.split("\n\n");
    let points: Vec<(i32, i32)> = input_parts
        .next()
        .unwrap()
        .lines()
        .map(|l| {
            (
                l.split(",").next().unwrap().parse().unwrap(),
                l.split(",").nth(1).unwrap().parse().unwrap(),
            )
        })
        .collect();
    let folds: Vec<(char, i32)> = input_parts
        .next()
        .unwrap()
        .lines()
        .map(|l| {
            (
                l.split("=").next().unwrap().parse::<String>().unwrap().chars().last().unwrap(),
                l.split("=").nth(1).unwrap().parse().unwrap(),
            )
        })
        .collect();

    let fold = folds[0];

    let mut ans = 0;

    for point in &points {
        if point.0 < fold.1 {
            ans += 1
        } else if point.0 > fold.1 {
            let new_point = (2*fold.1 - point.0, point.1);
            if !points.contains(&new_point) {
                ans += 1;
            }
        } else {
            panic!("Point is exactly on the fold")
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
            6,10
            0,14
            9,10
            0,3
            10,4
            4,11
            6,0
            6,12
            4,1
            0,13
            10,12
            3,4
            3,0
            8,4
            1,10
            2,14
            8,10
            9,0

            fold along y=7
            fold along x=5
        "};
        let result = solve(input);
        assert_eq!(result, 17);
    }
}
