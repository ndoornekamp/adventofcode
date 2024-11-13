from enum import Enum
from aocd.models import Puzzle
from datetime import datetime
import os
import subprocess
from string import Template


class Languages(str, Enum):
    PYTHON = "python"
    RUST = "rust"


def main(day: int | None = None, year: int | None = None, language: Languages = Languages.RUST):
    if not day:
        day = datetime.now().day

    if not year:
        year = datetime.now().year

    puzzle = Puzzle(day=day, year=year)

    if language == Languages.PYTHON:
        setup_python(day, year, puzzle)
    elif language == Languages.RUST:
        setup_rust(day, year, puzzle)
    else:
        raise


def setup_python(day: int, year: int, puzzle: Puzzle):
    raise NotImplementedError()


def setup_rust(day: int, year: int, puzzle: Puzzle):
    # Create the Rust project
    project_path = os.path.join(str(year), f"day{day:02d}")
    subprocess.run(["cargo", "new", project_path, "--bin"], check=True)
    subprocess.run(["cargo", "add", "indoc"], check=True, cwd=project_path)

    # Remove the default main.rs file,
    rs_file = os.path.join(project_path, "src", "main.rs")
    os.remove(rs_file)

    # Create a /src/bin directory instead so we can have separate binaries for part1 and part2
    bin_dir = os.path.join(project_path, "src", "bin")
    os.makedirs(bin_dir, exist_ok=True)

    with open(os.path.join(bin_dir, "input.txt"), "w") as f:
        f.write(puzzle.input_data)

    # Populate the part1.rs file with the default.rs template, filling in the example input and output
    with open(os.path.join("setup", "default.rs"), "r") as f:
        default_rs_file_content = f.read()

    answer_example_part_1 = puzzle.examples[0].answer_a or "None"

    example_input = "\t\t\t" + "\n\t\t\t".join(puzzle.examples[0].input_data.split("\n"))
    template = Template(default_rs_file_content).substitute(
        output=answer_example_part_1,
        input=example_input,
    )

    with open(os.path.join(bin_dir, "part1.rs"), "w") as f:
        f.write(template)

    # Create an empty part2.rs file - most likely we'll end up copying part 1 into it and modifying it for part 2
    open(os.path.join(bin_dir, "part2.rs"), "w").close()
