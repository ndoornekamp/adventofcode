fn main() {
    let input = include_str!("./input.txt");

    let output = solve(input);
    println!("Part 1 answer: {}", output);
}

fn solve(input: &str) -> usize {
    let binary_strings: Vec<String> = input
        .chars()
        .map(|c| {
            format!(
                "{:0>4}",
                format!("{:b}", usize::from_str_radix(&c.to_string(), 16).unwrap())
            )
        })
        .collect();

    let raw_packet = binary_strings.join("");
    let bits: Vec<usize> = raw_packet.chars().map(|c| c.to_digit(2).unwrap() as usize).collect();

    let mut packet = Packet { bits, pos: 0 };
    parse_packet(&mut packet)
}

struct Packet {
    bits: Vec<usize>,
    pos: usize,
}

impl Packet {
    fn pop_bits(&mut self, num_bits: usize) -> Vec<usize> {
        self.pos += num_bits;
        self.bits[self.pos - num_bits..self.pos].to_vec()
    }
}

fn bits_to_decimal(bits: Vec<usize>) -> usize {
    bits.iter().fold(0, |a, b| a << 1 | b)
}

fn parse_packet(packet: &mut Packet) -> usize {
    // Heavily inspired by
    let version = bits_to_decimal(packet.pop_bits(3));
    let type_id = bits_to_decimal(packet.pop_bits(3));

    let mut ans = version;

    if type_id == 4 {
        // Literal value
        loop {
            let literal_value = packet.pop_bits(5);
            if literal_value[0] == 0 {
                return ans;
            }
        }
    }

    if packet.pop_bits(1)[0] == 0 {
        // Length type ID 0
        let subpackets_bits_end_pos = bits_to_decimal(packet.pop_bits(15)) + packet.pos;
        while packet.pos < subpackets_bits_end_pos {
            let version = parse_packet(packet);
            ans += version;
        }
    } else {
        let n_subpackets = bits_to_decimal(packet.pop_bits(11));
        for _ in 0..n_subpackets {
            let version = parse_packet(packet);
            ans += version;
        }
    }

    ans
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn example_part_1_literal() {
        let input = indoc! {"D2FE28"};
        let result = solve(input);
        assert_eq!(result, 6);
    }

    #[test]
    fn example_part_1_operator_operator_literal() {
        let input = indoc! {"8A004A801A8002F478"};
        let result = solve(input);
        assert_eq!(result, 16);
    }

    #[test]
    fn example_part_1_operator_two_literal_subpackets() {
        let input = indoc! {"620080001611562C8802118E34"};
        let result = solve(input);
        assert_eq!(result, 12);
    }

    #[test]
    fn example_part_1_operator_two_literal_subpackets_2() {
        let input = indoc! {"C0015000016115A2E0802F182340"};
        let result = solve(input);
        assert_eq!(result, 23);
    }

    #[test]
    fn example_part_1_operator_operator_five_literal() {
        let input = indoc! {"A0016C880162017C3686B18A3D4780"};
        let result = solve(input);
        assert_eq!(result, 31);
    }
}
