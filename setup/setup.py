from enum import Enum
import shutil
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
    project_path = os.path.join(str(year), f"day{day:02d}")
    assert not os.path.isdir(project_path), f"Project directory {project_path} already exists"

    try:
        if language == Languages.PYTHON:
            setup_python(project_path, puzzle)
        elif language == Languages.RUST:
            setup_rust(project_path, puzzle)
        else:
            raise NotImplementedError()
    except Exception as e:
        print(f"Failed to setup project: {e}")
        shutil.rmtree(project_path)


def setup_python(project_path: str, puzzle: Puzzle):

    os.makedirs(project_path, exist_ok=True)

    subprocess.run(["uv", "init", "-n", "--no-readme"], check=True, cwd=project_path)
    subprocess.run(["uv", "add", "pytest"], check=True, cwd=project_path)

    # Remove the default hello.py file,
    hello_file = os.path.join(project_path, "hello.py")
    os.remove(hello_file)

    # Append line with pytest option to pyproject.toml so it checks for tests in any .py file instead of
    # just test_*.py files
    with open(os.path.join(project_path, "pyproject.toml"), "a") as f:
        f.write('\n[tool.pytest.ini_options]\npython_files = "*.py"')

    # Add settings.json with pytest option for running tests from VSCode
    os.makedirs(os.path.join(project_path, ".vscode"), exist_ok=True)
    with open(os.path.join(project_path, ".vscode", "settings.json"), "w") as f:
        f.write('{"python.testing.pytestEnabled": true}')

    # Puzzle input to input.txt
    with open(os.path.join(project_path, "input.txt"), "w") as f:
        f.write(puzzle.input_data)

    # Populate the part1.py file with the default.py template, filling in the example input and output
    with open(os.path.join("setup", "default.py"), "r") as f:
        default_py_file_content = f.read()

    template = Template(default_py_file_content)
    if puzzle.examples:
        answer_example_part_1 = puzzle.examples[0].answer_a or "None" if puzzle.examples else "None"

        example_input = "        " + "\n        ".join(puzzle.examples[0].input_data.split("\n"))
        template = template.substitute(output=answer_example_part_1, input=example_input)
    else:
        template = template.substitute(output="None", input="None")

    with open(os.path.join(project_path, "part1.py"), "w") as f:
        f.write(template)

    # Create an empty part2.py file - most likely we'll end up copying part 1 into it and modifying it for part 2
    open(os.path.join(project_path, "part2.py"), "w").close()


def setup_rust(project_path: str, puzzle: Puzzle):
    # Create the Rust project
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

    template = Template(default_rs_file_content)
    if puzzle.examples:
        answer_example_part_1 = puzzle.examples[0].answer_a or "None" if puzzle.examples else "None"

        example_input = "            " + "\n            ".join(puzzle.examples[0].input_data.split("\n"))
        template = template.substitute(output=answer_example_part_1, input=example_input)
    else:
        template = template.substitute(output="None", input="None")

    with open(os.path.join(bin_dir, "part1.rs"), "w") as f:
        f.write(template)

    # Create an empty part2.rs file - most likely we'll end up copying part 1 into it and modifying it for part 2
    open(os.path.join(bin_dir, "part2.rs"), "w").close()
