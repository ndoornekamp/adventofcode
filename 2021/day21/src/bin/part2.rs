use std::collections::HashMap;

fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    // With three throws of the Dirac die, there's one universe where the
    let n_universes_per_roll_total: HashMap<usize, usize> = HashMap::from([
        (3, 1),
        (4, 3),
        (5, 6),
        (6, 7),
        (7, 6),
        (8, 3),
        (9, 1)
    ]);
    let digits: Vec<char> = input.chars().filter(|c| c.is_digit(10)).collect::<Vec<_>>();
    let player1_start: usize = digits[1].to_digit(10).unwrap() as usize;
    let player2_start: usize = digits[3].to_digit(10).unwrap() as usize;
    let players: [Player; 2] = [Player::new(player1_start), Player::new(player2_start)];

    let mut wins = [0, 0];
    let mut games = HashMap::from([(Game { players }, 1usize)]);

    for player in (0..=1).cycle() {
        let mut next = HashMap::new();
        for (&roll_total, n_universes_for_roll_total) in n_universes_per_roll_total.iter() {
            for (game, universes) in games.iter() {
                let advanced = game.advance(player, roll_total);
                if advanced.players[player].score  >= 21 {
                    wins[player] += universes * n_universes_for_roll_total;
                } else {
                    *next.entry(advanced).or_default() += universes * n_universes_for_roll_total;
                }
            }
        }
        games = next;
        if games.is_empty() {
            break;
        }
    }
    let [p1_wins, p2_wins] = wins;
    std::cmp::max(p1_wins, p2_wins)
}

#[derive(Copy, Clone, Eq, PartialEq, Hash, Debug)]
struct Game {
    players: [Player; 2],
}

impl Game {
    fn advance(&self, player: usize, roll: usize) -> Self {
        let mut next = *self;
        next.players[player].advance(roll);
        next
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
    fn example_part_2() {
        let input = indoc! {"
            Player 1 starting position: 4
            Player 2 starting position: 8
        "};
        let result = solve(input);
        assert_eq!(result, 444356092776315);
    }
}
