fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    println!("Part 1 answer: {}", output);
}

fn part1(input: &str) -> i32 {
    let starting_locations: Vec<i32> = input.split(",").map(|s| s.parse().unwrap()).collect();

    let min = starting_locations.iter().min().unwrap();
    let max = starting_locations.iter().max().unwrap();

    let mut best_fuel_cost = 1000000;
    let mut best_h_pos: Option<i32> = None;

    for h_pos in *min..*max {
        let fuel_cost: i32 = starting_locations.iter().map(|l| (l - h_pos).abs()).sum();
        if fuel_cost < best_fuel_cost {
            best_fuel_cost = fuel_cost;
            best_h_pos = Some(h_pos);
        }
    }
    dbg!(best_h_pos, best_fuel_cost);
    best_fuel_cost
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        let input = "16,1,2,0,4,2,7,1,2,14";
        let result = part1(input);
        assert_eq!(result, 37);
    }
}
