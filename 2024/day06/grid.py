
from dataclasses import dataclass
from textwrap import dedent
from typing import Self


@dataclass
class Grid:
    rows: list[list[str]]

    @classmethod
    def from_txt(cls, input: str) -> Self:
        rows = [list(line) for line in input.strip().split("\n")]

        return cls(rows=rows)


def test_grid_from_txt():
    input = dedent("""
        ..
        ##
    """)

    grid = Grid.from_txt(input)

    assert grid.rows == [
        ['.', '.'],
        ['#', '#']
    ]
