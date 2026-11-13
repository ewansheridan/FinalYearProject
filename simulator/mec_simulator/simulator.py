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