from textwrap import dedent


def solve(input: str) -> int:
    grid, moves = input.strip().split("\n\n")

    n_rows = len(grid.split("\n"))
    n_cols = len(grid.split("\n")[0])

    walls = set()
    boxes = set()
    pos = (-1, -1)
    for i, row in enumerate(grid.split("\n")):
        for j, cell in enumerate(row):
            if cell == "#":
                walls.add((i, j))
            elif cell == "O":
                boxes.add((i, j))
            elif cell == "@":
                pos = (i, j)

    moves = [char for char in moves.replace("\n", "")]

    for move in moves:
        move_map = {
            "<": (0, -1),
            ">": (0, 1),
            "^": (-1, 0),
            "v": (1, 0)
        }
        d = move_map[move]
        new_pos = (pos[0] + d[0], pos[1] + d[1])

        # Easy: robot would move into a wall
        if new_pos in walls:
            continue  # Nothing happens

        # Easy: Robot would move into an empty cell
        if new_pos not in boxes:
            pos = new_pos
            continue

        # Hard: Robot would push one or more boxes
        boxes_that_would_be_pushed = {new_pos}
        i = 1
        while (new_pos[0] + i * d[0], new_pos[1] + i * d[1]) in boxes:
            boxes_that_would_be_pushed.add((new_pos[0] + i * d[0], new_pos[1] + i * d[1]))
            i += 1

        if (new_pos[0] + i * d[0], new_pos[1] + i * d[1]) in walls:
            # Robot is pushing against the wall through a stack of boxes -> nothing happens
            continue
        else:
            # Whole stack of boxes moves
            pos = new_pos
            boxes.remove(pos)
            boxes.add((new_pos[0] + i * d[0], new_pos[1] + i * d[1]))

    dbg_grid = print_grid(n_rows, n_cols, walls, boxes, pos)

    ans = 0
    for box in boxes:
        ans += 100 * box[0] + box[1]

    return ans


def print_grid(n_rows, n_cols, walls, boxes, pos):
    rows = []
    for i in range(n_rows):
        row = ""
        for j in range(n_cols):
            if (i, j) in walls:
                row += "#"
            elif (i, j) in boxes:
                row += "O"
            elif (i, j) == pos:
                row += "@"
            else:
                row += "."
        rows.append(row)
    return rows


def test_solve_small():
    input = dedent("""
        ########
        #..O.O.#
        ##@.O..#
        #...O..#
        #.#.O..#
        #...O..#
        #......#
        ########

        <^^>>>vv<v>>v<<
    """)
    assert solve(input) == 2028


def test_solve():
    input = dedent("""
        ##########
        #..O..O.O#
        #......O.#
        #.OO..O.O#
        #..O@..O.#
        #O#..O...#
        #O..O..O.#
        #.OO.O.OO#
        #....O...#
        ##########

        <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
        vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
        ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
        <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
        ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
        ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
        >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
        <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
        ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
        v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
    """)
    assert solve(input) == 10092


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
