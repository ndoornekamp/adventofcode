fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let digits: Vec<char> = input.chars().filter(|c| c.is_digit(10)).collect::<Vec<_>>();
    let player1_start: usize = digits[1].to_digit(10).unwrap() as usize;
    let player2_start: usize = digits[3].to_digit(10).unwrap() as usize;
    let mut players: Vec<Player> = vec![Player::new(player1_start), Player::new(player2_start)];

    let mut die = Die::new();

    for idx in (0..players.len()).cycle() {
        let player = &mut players[idx];
        player.advance(die.roll());
        if player.score >= 1000 {
            break;
        }
    }

    let loser = players.into_iter().map(|p| p.score).min().unwrap();

    loser * die.n_rolls()
}

struct Die {
    n_rolls: usize,
    rolls: std::iter::Cycle<std::ops::RangeInclusive<usize>>,
}

impl Die {
    fn new() -> Self {
        Self {
            n_rolls: 0,
            rolls: (1..=100).cycle(),
        }
    }

    fn roll(&mut self) -> usize {
        self.n_rolls += 3;
        self.rolls.by_ref().take(3).sum()
    }

    fn n_rolls(&self) -> usize {
        self.n_rolls
    }
}

#[derive(Copy, Clone, Eq, PartialEq, Hash, Debug)]
struct Player {
    pos: usize,
    score: usize,
}

impl Player {
    fn new(pos: usize) -> Self {
        Self {
            pos: pos - 1,  // Store pos-1 so modulus operation works (but ensure to return pos+1 in Player.position())
            score: 0,
        }
    }

    fn position(&self) -> usize {
        self.pos + 1
    }

    fn advance(&mut self, roll: usize) {
        self.pos = (self.pos + roll) % 10;
        self.score += self.position();
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_1() {
        let input = indoc! {"
            Player 1 starting position: 4
            Player 2 starting position: 8
        "};
        let result = solve(input);
        assert_eq!(result, 739785);
    }
}
