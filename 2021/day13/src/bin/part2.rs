fn main() {
    let input = include_str!("./input.txt");
    solve(input);
}

fn solve(input: &str) {
    let mut input_parts = input.split("\n\n");
    let mut points: Vec<(i32, i32)> = input_parts
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
                l.split("=")
                    .next()
                    .unwrap()
                    .parse::<String>()
                    .unwrap()
                    .chars()
                    .last()
                    .unwrap(),
                l.split("=").nth(1).unwrap().parse().unwrap(),
            )
        })
        .collect();

    for fold in folds {
        let mut new_points: Vec<(i32, i32)> = [].to_vec();
        for point in &points {

            if fold.0 == 'x' {
                if point.0 < fold.1 {
                    new_points.push((point.0, point.1));
                } else if point.0 > fold.1 {
                    let new_point = (2 * fold.1 - point.0, point.1);
                    if !new_points.contains(&new_point) {
                        new_points.push(new_point);
                    }
                } else {
                    panic!("Point is exactly on the fold")
                }
            } else if fold.0 == 'y' {
                if point.1 < fold.1 {
                    new_points.push((point.0, point.1));
                } else if point.1 > fold.1 {
                    let new_point = (point.0, 2*fold.1 - point.1);
                    if !new_points.contains(&new_point) {
                        new_points.push(new_point);
                    }
                }
            } else {
                panic!("fold.0 is expected to be either x or y")
            }
        }
        points = new_points;
    }
    let max_row = points.iter().max_by(|x, y| x.0.cmp(&y.0)).unwrap().0;
    let max_col = points.iter().max_by(|x, y| x.1.cmp(&y.1)).unwrap().1;

    for j in 0..=max_col {
        let mut row: String = "".to_string();
        for i in 0..=max_row {
            if points.contains(&(i, j)) {
                row.push('x');
            } else {
                row.push(' ');
            }
        }
        println!("{}", row);
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_2() {
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
        solve(input);
    }
}
