input_file_path = "day08/input.txt"

with open(input_file_path, 'r') as infile:
    input = infile.read()

# trees, visible = [], []
# for row in input.split("\n"):
#     trees.append([tree for tree in row])
#     visible.append([0 for _ in row])

# for i, row in enumerate(trees):
#     # left to right
#     h = row[0]
#     visible[i][0] = 1

#     for j, tree in enumerate(row):
#         if tree > h:
#             h = tree
#             visible[i][j] = 1

#     # right to left
#     h = row[-1]
#     visible[i][-1] = 1

#     for j, tree in enumerate(row[::-1]):
#         if tree > h:
#             h = tree
#             visible[i][-j-1] = 1

# nof_columns = len(trees[0])
# for j in range(nof_columns):
#     # top to bottom
#     column = [row[j] for row in trees]

#     h = column[0]
#     visible[0][j] = 1
#     for i, tree in enumerate(column):
#         if tree > h:
#             h = tree
#             visible[i][j] = 1

#     # bottom to top
#     h = column[-1]
#     visible[-1][j] = 1

#     for i, tree in enumerate(column[::-1]):
#         if tree > h:
#             h = tree

#             if not visible[-i-1][j]:
#                 visible[-i-1][j] = 1

# print(sum([sum(row) for row in visible]))

trees = []
for row in input.split("\n"):
    trees.append([tree for tree in row])

scores = []
for tree_i, row in enumerate(trees):
    for tree_j, tree in enumerate(row):
        score = [0, 0, 0, 0]

        # up
        for j in range(tree_j-1, -1, -1):
            score[0] += 1
            if trees[tree_i][j] >= tree:
                break

        for i in range(tree_i - 1, -1, -1):
            score[1] += 1
            if trees[i][tree_j] >= tree:
                break

        for j in range(tree_j + 1, len(row)):
            score[2] += 1
            if trees[tree_i][j] >= tree:
                break

        for i in range(tree_i + 1, len(trees)):
            score[3] += 1
            if trees[i][tree_j] >= tree:
                break

        scores.append(score[0] * score[1] * score[2] * score[3])

print(max(scores))
