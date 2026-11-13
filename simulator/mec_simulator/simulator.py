import simpy

from . import compute_node
from .compute_node import ComputeNode
from .task import Task, _Subtask


class MecSimulator:
    def __init__(self):
        self.env = simpy.Environment()
        self.compute_nodes = []

    def add_node(self, name, mips_per_core, num_of_cores, rtt_ms):
        self.compute_nodes.append(
            ComputeNode(self.env, name, mips_per_core, num_of_cores, rtt_ms)
        )

    def run_subtask(self, subtask: _Subtask, compute_node: ComputeNode):
        print(f"Subtask leaves at t={self.env.now}")
        yield self.env.timeout(compute_node.rtt_ms / 2)

        with compute_node.cpu.request() as request:
            print(f"Subtask requests access to a core in {compute_node.name} at t={self.env.now}")
            yield request

            print(f"Subtask starts executing at t={self.env.now}")
            yield self.env.timeout(
                1000 * subtask.mi / compute_node.mips_per_core
            )
            print(f"Subtask finishes executing at t={self.env.now}")

        yield self.env.timeout(compute_node.rtt_ms / 2)
        print(f"Subtask done at t={self.env.now}")

    def run(self):
        self.env.run()