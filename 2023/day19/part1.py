
from dataclasses import dataclass
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

ans = 0
for part in parts.split("\n"):
    accepted = False
    rejected = False

    print(part)
    part = {k: int(v) for k, v in (item.split('=') for item in part.strip("\{\}").split(','))}

    current_workflow = workflows_parsed["in"]
    while not accepted and not rejected:
        for step in current_workflow:
            if isinstance(step, str):
                if step == "A":
                    accepted = True
                elif step == "R":
                    rejected = True
                else:
                    current_workflow = workflows_parsed[step]
                break
            elif step.operator in ("<", ">"):
                if eval(f"{part[step.variable]} {step.operator} {step.threshold}"):
                    if step.next_workflow_if_true == "A":
                        accepted = True
                    elif step.next_workflow_if_true == "R":
                        rejected = True
                    else:
                        current_workflow = workflows_parsed[step.next_workflow_if_true]
                    break
            else:
                raise

    if accepted:
        print("accepted")
        ans += sum(part.values())
    elif rejected:
        print("rejected")
    else:
        raise

print(ans)
