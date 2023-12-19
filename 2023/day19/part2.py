
from copy import deepcopy
from dataclasses import dataclass
import math
import re
from typing import Literal


input_file_path = '2023/day19/input.txt'

with open(input_file_path, 'r') as f:
    input = f.read()


@dataclass
class WorkflowStep:
    variable: str
    operator: Literal[">", "<"]
    threshold: int
    next_workflow_if_true: str


workflows, parts = input.split("\n\n")

workflows_parsed = {}
for workflow in workflows.split("\n"):
    m = re.match("([a-z]+){(.*)}", workflow)
    name = m.group(1)
    steps = m.group(2).split(",")

    steps_parsed = []
    for step in steps:
        if "<" in step:
            steps_parsed.append(WorkflowStep(step.split("<")[0], "<", int(step.split("<")[1].split(":")[0]), step.split(":")[1]))
        elif ">" in step:
            steps_parsed.append(WorkflowStep(step.split(">")[0], ">", int(step.split(">")[1].split(":")[0]), step.split(":")[1]))
        else:
            steps_parsed.append(step)

    workflows_parsed[name] = steps_parsed


def n_accepted_ratings(ratings, workflow, step) -> int:
    if isinstance(workflow[step], str):
        if workflow[step] == "A":
            return math.prod([len(ratings[rating]) for rating in ratings])
        elif workflow[step] == "R":
            return 0
        elif isinstance(workflow, str) and workflow in workflows_parsed:
            return n_accepted_ratings(ratings, workflows_parsed[workflow], 0)
        elif workflow[step] in workflows_parsed:
            return n_accepted_ratings(ratings, workflows_parsed[workflow[step]], 0)
        else:
            raise
    else:
        for workflow_step in workflow[step:]:
            if workflow_step.operator == "<":
                ratings_if_true = deepcopy(ratings)
                ratings_if_true[workflow_step.variable] = [r for r in ratings[workflow_step.variable] if r < workflow_step.threshold]
                ratings_if_false = deepcopy(ratings)
                ratings_if_false[workflow_step.variable] = [r for r in ratings[workflow_step.variable] if r >= workflow_step.threshold]

                return sum([
                    n_accepted_ratings(ratings=ratings_if_true, workflow=workflow_step.next_workflow_if_true, step=0),
                    n_accepted_ratings(ratings=ratings_if_false, workflow=workflow, step=step + 1)
                ])

            elif workflow_step.operator == ">":
                ratings_if_true = deepcopy(ratings)
                ratings_if_true[workflow_step.variable] = [r for r in ratings[workflow_step.variable] if r > workflow_step.threshold]
                ratings_if_false = deepcopy(ratings)
                ratings_if_false[workflow_step.variable] = [r for r in ratings[workflow_step.variable] if r <= workflow_step.threshold]

                return sum([
                    n_accepted_ratings(ratings=ratings_if_true, workflow=workflow_step.next_workflow_if_true, step=0),
                    n_accepted_ratings(ratings=ratings_if_false, workflow=workflow, step=step + 1)
                ])
            else:
                raise


ratings = {"x": list(range(1, 4001)), "m": list(range(1, 4001)), "a": list(range(1, 4001)), "s": list(range(1, 4001))}
ans = n_accepted_ratings(ratings, workflows_parsed["in"], 0)
print(ans)
