
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Module(ABC):
    name: str
    destinations: list

    def queue_output_pulse(self, signal):
        for destination in self.destinations:
            q.append((destination, signal, self.name))

    @abstractmethod
    def process_pulse(self, signal, source):
        pass


class Broadcaster(Module):
    def process_pulse(self, signal, source):
        self.queue_output_pulse(signal)


class Output(Module):
    def process_pulse(self, signal, source):
        pass


class FlipFlop(Module):
    on: bool = False

    def process_pulse(self, signal, source):
        if signal == "low":
            self.on = not self.on
            if self.on:
                self.queue_output_pulse("high")
            else:
                self.queue_output_pulse("low")
        elif signal == "high":
            pass


class Conjunction(Module):
    previous_inputs = {}

    def process_pulse(self, signal, source):
        self.previous_inputs[source] = signal
        if all(v == "high" for v in self.previous_inputs.values()):
            self.queue_output_pulse("low")
        else:
            self.queue_output_pulse("high")


def send_pulse(destination, signal, source):
    global n_pulses_high
    global n_pulses_low

    if signal == "high":
        n_pulses_high += 1
    elif signal == "low":
        n_pulses_low += 1
    else:
        raise

    if destination in modules:
        destination_module: Module = modules[destination]
        destination_module.process_pulse(signal, source)
        # print(f"{source} -{signal}-> {destination}")


def parse_input():
    input_file_path = '2023/day20/input.txt'

    with open(input_file_path, 'r') as f:
        input = f.read().splitlines()

    modules = {}
    for line in input:
        module, destinations = line.split(" -> ")
        destinations = destinations.split(", ")

        if module == "broadcaster":
            modules[module] = Broadcaster(module, destinations)
        elif module.startswith("%"):
            modules[module[1:]] = FlipFlop(module[1:], destinations)
        elif module.startswith("&"):
            modules[module[1:]] = Conjunction(module[1:], destinations)
        else:
            raise

    modules["output"] = Output("output", [])

    for conjunction_module in [m for m in modules.values() if isinstance(m, Conjunction)]:
        conjunction_module_inputs = [m for m in modules.values() if conjunction_module.name in m.destinations]
        conjunction_module.previous_inputs = {m.name: "low" for m in conjunction_module_inputs}

    return modules


modules = parse_input()
broadcaster = modules["broadcaster"]

n_pulses_high, n_pulses_low = 0, 0
for _ in range(1000):
    q = [("broadcaster", "low", "button")]
    while q:
        destination, signal, source = q.pop(0)
        send_pulse(destination, signal, source)

print(n_pulses_high * n_pulses_low)
