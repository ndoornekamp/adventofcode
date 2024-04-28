fn main() {
    let input = include_str!("./input.txt");
    let output = part2(input);
    println!("Part 1 answer: {}", output);
}

#[derive(Clone)]
struct Board {
    bingo: bool,
    rows_and_columns: Vec<Vec<i32>>
}

fn calculate_ans(board: Vec<Vec<i32>>, number_drawn: i32) -> i32 {
    let mut unmarked_numbers = board.concat();
    unmarked_numbers.sort();
    unmarked_numbers.dedup();
    let sum_of_unmarked_numbers: i32 = unmarked_numbers.iter().sum::<i32>();

    dbg!(sum_of_unmarked_numbers, number_drawn);

    println!("Answer {}", sum_of_unmarked_numbers * number_drawn);
    sum_of_unmarked_numbers * number_drawn
}

fn part2(input: &str) -> i32 {
    let mut input_parts = input.split("\n\n");
    let bingo_balls = input_parts
        .next()
        .unwrap()
        .split(",")
        .map(|s| -> i32 { s.parse().unwrap() });

    let mut boards: Vec<Board> = vec![];
    for board in input_parts {
        let mut rows_and_columns: Vec<Vec<i32>> = vec![[].to_vec(); 5];
        for row in board.split("\n") {
            let row_numbers: Vec<i32> = row
                .split_whitespace()
                .map(|s| -> i32 { s.parse().unwrap() })
                .collect();

            for (j, number) in row_numbers.clone().into_iter().enumerate() {
                rows_and_columns[j].push(number);
            }

            rows_and_columns.push(row_numbers.clone());
        }
        let board_struct = Board {
            bingo: false,
            rows_and_columns: rows_and_columns.clone(),
        };
        boards.push(board_struct);
    }

    let mut parsed_boards = boards.clone();
    for number_drawn in bingo_balls {
        for i in 0..parsed_boards.len() {
            let mut board = parsed_boards[i].clone();

            if board.bingo {
                continue
            }

            for row_or_column in &mut board.rows_and_columns {
                row_or_column.retain(|number| number != &number_drawn);
            }

            for row_or_column in board.rows_and_columns.clone() {
                if row_or_column.len() == 0 {
                    println!("Bingo on board {}!", i + 1);
                    board.bingo = true;
                }
            }
            parsed_boards[i] = board.clone();

            if parsed_boards.iter().all(|b| b.bingo) {
                println!("Board {} was the final board to bingo", i + 1);
                return calculate_ans(board.rows_and_columns.clone(), number_drawn)
            }
        }

    }
    0
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example() {
        let input = indoc! {"
            7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

            22 13 17 11  0
            8  2 23  4 24
            21  9 14 16  7
            6 10  3 18  5
            1 12 20 15 19

            3 15  0  2 22
            9 18 13 17  5
            19  8  7 25 23
            20 11 10 24  4
            14 21 16 12  6

            14 21 17 24  4
            10 16 15  9 19
            18  8 23 26 20
            22 11 13  6  5
            2  0 12  3  7"};
        let result = part2(input);
        assert_eq!(result, 1924);
    }
}
