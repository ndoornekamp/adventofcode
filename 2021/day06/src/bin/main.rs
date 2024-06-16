use std::collections::HashMap;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input, 80);
    println!("Part 1 answer: {}", output);

    let output = solve(input, 256);
    println!("Part 2 answer: {}", output);
}

fn solve(input: &str, range: u16) -> usize {
    let initial_state: Vec<u8> = input.split(",").map(|s| s.parse().unwrap()).collect();

    let mut lifecycle_7: HashMap<u8, usize> = HashMap::new();
    for i in 0..7 {
        lifecycle_7.insert(
            i,
            initial_state.iter().filter(|&&j| j == i).count()
        );
    }

    let mut lifecycle_9: HashMap<u8, usize> = HashMap::new();
    for i in 0..9 {
        lifecycle_9.insert(i, 0);
    }

    for _day in 1..=range {
        // First take note of the number of resetting and new fish today
        let nof_lifecycle_resets = lifecycle_7[&0] + lifecycle_9[&0];

        // Then update the number of new fish per internal timer
        for i in 0..6 {
            *lifecycle_7.get_mut(&i).unwrap() = lifecycle_7[&(i+1)]
        }
        for i in 0..8 {
            *lifecycle_9.get_mut(&i).unwrap() = lifecycle_9[&(i+1)]
        }

        // New fish have lifecycle 9, resets move to lifecycle 7
        // So: for every reset, a fish is added to both lifecycles
        *lifecycle_7.get_mut(&6).unwrap() = nof_lifecycle_resets;
        *lifecycle_9.get_mut(&8).unwrap() = nof_lifecycle_resets;

    }

    return lifecycle_7.values().sum::<usize>() + lifecycle_9.values().sum::<usize>();
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_1() {
        let input = indoc! {"3,4,3,1,2"};
        let result = solve(input, 80);
        assert_eq!(result, 5934);
    }

    #[test]
    fn example_part_2() {
        let input = indoc! {"3,4,3,1,2"};
        let result = solve(input, 256);
        assert_eq!(result, 26984457539);
    }
}
