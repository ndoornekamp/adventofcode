# Advent of Code

## Setup

Store your AoC session cookie:

```bash
mkdir ~/.config/aocd
nano ~/.config/aocd/token
```

You can find your session cookie in your browser's developer tools under the "Cookies" section for the Advent of Code website.

Set up a project for a new day by using the setup script:

```bash
uv run typer setup/setup.py run --day <day> --year <year> --language <language>
```

Puzzle input and example input/output will be downloaded and inserted into the project using [aocd](https://github.com/wimglenn/advent-of-code-data).

## Running using Rust

To run tests for a specific day, run `cargo test` from the `/<year>/day<xx>` directory, optionally using the `-- --nocapture` flag to show the output of `dbg!` macros.

To execute the code for a specific day, run `cargo run --bin part<x>` from the `/<year>/day<xx>` directory.
