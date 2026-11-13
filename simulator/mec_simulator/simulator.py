import simpy

from . import compute_node
from .compute_node import ComputeNode
from .task import Task, Subtask
from itertools import count


class MecSimulator:
    def __init__(self):
        self.env = simpy.Environment()
        self.compute_nodes = []
        self.task_id_generator = count()

    def add_node(self, name, mips_per_core, num_of_cores, rtt_ms):
        self.compute_nodes.append(
            ComputeNode(self.env, name, mips_per_core, num_of_cores, rtt_ms)
        )

    @property
    def wallclock_ms(self):
        t = f"{self.env.now:.2f}".rstrip("0").rstrip(".")
        return f"{f't = {t} ms':<15}"

    def submit_task(self, total_mi, num_of_subtasks):
        self.env.process(self.run_task(Task(total_mi, num_of_subtasks, next(self.task_id_generator))))

    def run_task(self, task: Task):
        """
        for now, we assume that compute_nodes contains exactly three things, in
        this exact order: [cloud, edge, local]. then this hard-codes the decision
        to be first 50% of the subtasks execute on cloud, next 30% on the edge,
        and last 20% on the local device. all of this can be replaced by a smarter
        scheduling function later
        """
        print(f"{self.wallclock_ms}Overall task {task.id} started")

        halfway_point = len(task.subtasks) * 50 // 100
        other_breakpoint = len(task.subtasks) * 80 // 100
        subtask_processes = []

        for i, subtask in enumerate(task.subtasks):
            if i < halfway_point:
                compute_node = self.compute_nodes[0]
            elif i < other_breakpoint:
                compute_node = self.compute_nodes[1]
            else:
                compute_node = self.compute_nodes[2]

            p = self.env.process(self.run_subtask(subtask, compute_node))
            subtask_processes.append(p)

        yield self.env.all_of(subtask_processes)
        print(f"{self.wallclock_ms}Overall task {task.id} completed")


    def run_subtask(self, subtask: Subtask, compute_node: ComputeNode):
        print(f"{self.wallclock_ms}Subtask {subtask.idStr} leaves")
        yield self.env.timeout(compute_node.rtt_ms / 2)

        with compute_node.cpu.request() as request:
            print(f"{self.wallclock_ms}Subtask {subtask.idStr} requests access to a core in {compute_node.name}")
            yield request

            print(f"{self.wallclock_ms}Subtask {subtask.idStr} starts executing in {compute_node.name}")
            yield self.env.timeout(
                1000 * subtask.mi / compute_node.mips_per_core
            )
            print(f"{self.wallclock_ms}Subtask {subtask.idStr} finishes executing")

        yield self.env.timeout(compute_node.rtt_ms / 2)
        print(f"{self.wallclock_ms}Subtask {subtask.idStr} complete")

    def run(self):
        self.env.run()