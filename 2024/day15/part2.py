from textwrap import dedent
from unittest.mock import ANY
from tqdm import tqdm


def solve(input: str) -> int:
    grid, moves = input.strip().split("\n\n")

    grid = expand_grid(grid)

    n_rows = len(grid)
    n_cols = len(grid[0])

    walls = set()
    boxes = set()
    pos = (-1, -1)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "#":
                walls.add((i, j))
            elif cell == "[":
                boxes.add((i, (j, j + 1)))
            elif cell == "@":
                pos = (i, j)

    moves = [char for char in moves.replace("\n", "")]

    for move in tqdm(moves):
        dbg_grid = print_grid(n_rows, n_cols, walls, boxes, pos)

        move_map = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
        d = move_map[move]
        new_pos = (pos[0] + d[0], pos[1] + d[1])

        # Easy: robot would move into a wall
        if new_pos in walls:
            continue  # Nothing happens

        # Easy: Robot would move into an empty cell
        robot_pushes_left_side_of_box = (new_pos[0], (new_pos[1], new_pos[1] + 1)) in boxes
        robot_pushes_right_side_of_box = (new_pos[0], (new_pos[1] - 1, new_pos[1])) in boxes
        if not robot_pushes_left_side_of_box and not robot_pushes_right_side_of_box:
            pos = new_pos
            continue

        # Hard: Robot would push one or more boxes
        boxes_that_would_be_pushed = {
            box
            for box in boxes
            if any(
                [
                    (new_pos[0], (new_pos[1] - 1, new_pos[1])) == box,
                    (new_pos[0], (new_pos[1], new_pos[1] + 1)) == box,
                ]
            )
        }
        assert len(boxes_that_would_be_pushed) == 1

        while True:
            additional_boxes_that_would_be_pushed = set()
            for box in boxes:
                for b in boxes_that_would_be_pushed:
                    box_location_after_push = (b[0] + d[0], (b[1][0] + d[1], b[1][1] + d[1]))
                    if any(
                        [
                            box_location_after_push == box,
                            box_location_after_push == (box[0], (box[1][0] - 1, box[1][1] - 1)),
                            box_location_after_push == (box[0], (box[1][0] + 1, box[1][1] + 1)),
                        ]
                    ):
                        if box not in boxes_that_would_be_pushed:
                            additional_boxes_that_would_be_pushed.add(box)

            if not additional_boxes_that_would_be_pushed:
                break
            else:
                boxes_that_would_be_pushed = boxes_that_would_be_pushed.union(additional_boxes_that_would_be_pushed)

        pushing_against_wall = False
        for box in boxes_that_would_be_pushed:
            if any([(box[0] + d[0], box[1][0] + d[1]) in walls, (box[0] + d[0], box[1][1] + d[1]) in walls]):
                pushing_against_wall = True
                break

        if pushing_against_wall:
            continue  # Nothing happens
        else:
            # Whole stack of boxes moves
            pos = new_pos
            moved_boxes = set()
            for box in boxes_that_would_be_pushed:
                boxes.remove(box)
                moved_boxes.add((box[0] + d[0], (box[1][0] + d[1], box[1][1] + d[1])))

            boxes = boxes.union(moved_boxes)

    dbg_grid = print_grid(n_rows, n_cols, walls, boxes, pos)

    ans = 0
    for box in boxes:
        ans += 100 * box[0] + box[1][0]

    return ans


def expand_grid(grid) -> list[str]:
    expanded = []
    for row in grid.split("\n"):
        expanded_row = ""
        for char in row:
            if char == "#":
                expanded_row += "##"
            elif char == "O":
                expanded_row += "[]"
            elif char == "@":
                expanded_row += "@."
            else:
                expanded_row += ".."
        expanded.append(expanded_row)
    return expanded


def print_grid(n_rows, n_cols, walls, boxes, pos):
    rows = []
    for i in range(n_rows):
        row = ""
        for j in range(n_cols):
            if (i, j) in walls:
                row += "#"
            elif (i, (j, j + 1)) in boxes:
                row += "["
            elif (i, (j - 1, j)) in boxes:
                row += "]"
            elif (i, j) == pos:
                row += "@"
            else:
                row += "."
        rows.append(row)
    return rows


def test_expand_grid():
    grid = dedent("""
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
    """)

    expanded_grid = expand_grid(grid)
    assert expanded_grid == dedent("""
        ####################
        ##....[]....[]..[]##
        ##............[]..##
        ##..[][]....[]..[]##
        ##....[]@.....[]..##
        ##[]##....[]......##
        ##[]....[]....[]..##
        ##..[][]..[]..[][]##
        ##........[]......##
        ####################
    """).split("\n")


def test_solve_small():
    input = dedent("""
        #######
        #...#.#
        #.....#
        #..OO@#
        #..O..#
        #.....#
        #######

        <vv<<^^<<^^
    """)
    assert solve(input) == ANY


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
    assert solve(input) == 9021


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    ans = solve(input)
    print(ans)
