def solve(input_lines: str) -> int:
    return $output


def test_solve():
    input = """
$input
    """
    assert solve(input) == $output


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    ans = solve(input)
    print(ans)
