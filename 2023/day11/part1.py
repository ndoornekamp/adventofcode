import pandas as pd
import numpy as np

input_file_path = '2023/day11/test_input.txt'

with open(input_file_path, 'r') as f:
    input = f.read().splitlines()

df = pd.DataFrame.from_records(input)
df = df.replace(".", None)

empty_rows = df.isnull().all(axis=1)
empty_cols = df.isnull().all(axis=0)

# Insert empty row after empty rows
n_cols = len(empty_rows)
for i, row_is_empty in enumerate(empty_rows):
    if row_is_empty:
        df.loc[i + 0.5] = [None for _ in range(n_cols)]
df = df.sort_index()

# Insert empty column after empty columns
# Loop over columns in reverse so the index of empty columns we found doesn't change when we insert
n_rows = len(df)
for i, col_is_empty in enumerate(empty_cols[::-1]):
    if col_is_empty:
        df.insert(n_cols - i - 1, f"{n_cols - i - 1.5}", None)

galaxy_coordinates = []
for i, row in enumerate(df.values.tolist()):
    for j, value in enumerate(row):
        if value == "#":
            galaxy_coordinates.append(np.array((i, j)))

ans = 0
for c1 in galaxy_coordinates:
    for c2 in galaxy_coordinates:
        ans += np.abs(c1 - c2).sum()

print(int(ans/2))  # Every pair is counted twice in the above