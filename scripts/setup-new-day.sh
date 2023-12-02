#!/bin/bash

day="$(date +%d)"
year="$(date +%Y)"
folder_name="$year/day$day"

mkdir "$folder_name" -p

touch "$folder_name"/input.txt
aocd "$year" "$day" > "$folder_name"/input.txt

touch "$folder_name"/test_input.txt

standard_code="
input_file_path = '$folder_name/test_input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()"

echo "$standard_code" > "$folder_name"/part1.py
echo "$standard_code" > "$folder_name"/part2.py
