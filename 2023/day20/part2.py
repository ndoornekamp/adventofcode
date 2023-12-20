
from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


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
    # -- Hardcoded assumptions --
    # rx has one conjunction module as input: nr. rx is low if nr is low
    # nr has four modules as input: ff, mm, fk, lh --> nr is low if all of these four are high

    first_high_signals = {}
    cycle_lengths = {}

    def process_pulse(self, signal, source):
        global n_button_presses

        if signal == "high" and source in ("ff", "mm", "fk", "lh"):
            print(f"Output {self.name} received high signal from {source} at {n_button_presses} button presses")

            if source in self.first_high_signals:
                self.cycle_lengths[source] = n_button_presses - self.first_high_signals[source]
            else:
                self.first_high_signals[source] = n_button_presses

        if all(source in self.cycle_lengths for source in ("ff", "mm", "fk", "lh")):
            print(f"Cycle lengths: {self.cycle_lengths}")
            print(math.lcm(*self.cycle_lengths.values()))
            raise StopIteration


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

    modules["nr"] = Output("nr", [])

    for conjunction_module in [m for m in modules.values() if isinstance(m, Conjunction)]:
        conjunction_module_inputs = [m for m in modules.values() if conjunction_module.name in m.destinations]
        conjunction_module.previous_inputs = {m.name: "low" for m in conjunction_module_inputs}

    return modules


modules = parse_input()

n_button_presses = 0
while True:
    n_button_presses += 1

    if n_button_presses % 1_000_000 == 0:
        print(f"{n_button_presses // 1_000_000}m button presses")

    try:
        q = [("broadcaster", "low", "button")]
        while q:
            destination, signal, source = q.pop(0)
            send_pulse(destination, signal, source)
    except StopIteration:
        break

print(n_button_presses)

# 814_934_624 is too low
