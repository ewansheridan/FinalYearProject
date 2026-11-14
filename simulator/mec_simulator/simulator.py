import simpy

from .compute_node import ComputeNode
from .task import Task, Subtask
from itertools import count


class MecSimulator:
    def __init__(self):
        """
        * Sets up a SimPy environment to simulate everything on
        * Initialises an empty array of nodes for things like edge / cloud servers
        * Uses an itertools count() to generate task IDs
        """
        self.env = simpy.Environment()
        self.compute_nodes = []
        self.task_id_generator = count()



    def add_node(self, name, speed_per_core_ipms, num_of_cores, rtt_ms):
        """
        * Creates a ComputeNode with the given parameters
        * Binds it to the SimPy environment associated with this simulator instance
        * Appends that node to the "compute_nodes" list
        """
        self.compute_nodes.append(
            ComputeNode(self.env, name, speed_per_core_ipms, num_of_cores, rtt_ms)
        )



    def print_elapsed_ms(self, message):
        """
        * Prints the given message after a timestamp
        * Creates a timestamp string exactly 15 characters wide
        * Gives the current elapsed time (in ms) of the SimPy clock from the ".now" method
        * Example, print_elapsed_ms("Hello")
            "t = 0 ms       Hello"
             0123456789ABCDE
        """
        t = f"{self.env.now:.2f}".rstrip("0").rstrip(".")
        print(f"{f't = {t} ms':<15}", message)



    def _run_subtask(self, subtask: Subtask, compute_node: ComputeNode):
        """
        * Internal generator method for the execution of a subtask
        * Waits half the RTT (one-way latency)
        * Then requests access to a core in the ComputeNode
        * Waits until that request gets granted by the ComputeNode (by its Simpy Resource)
        * Execution time = (subtask size) / (core speed)
        * Waits for that amount of time before freeing the Resource (leaving the "with" block)
        * Waits the other half of the RTT (one-way latency)
        """
        self.print_elapsed_ms(f"{subtask} leaves")
        yield self.env.timeout(compute_node.rtt_ms / 2)

        with compute_node.cpu.request() as request:
            self.print_elapsed_ms(f"{subtask} requests access to a core in {compute_node}")
            yield request

            self.print_elapsed_ms(f"{subtask} starts executing in {compute_node}")
            yield self.env.timeout(subtask.num_of_instructions / compute_node.speed_per_core_ipms)
            self.print_elapsed_ms(f"{subtask} finishes executing in {compute_node}")

        yield self.env.timeout(compute_node.rtt_ms / 2)
        self.print_elapsed_ms(f"{subtask} complete!")



    def _run_task(self, task: Task):
        """
        for now, we assume that compute_nodes contains exactly three things, in
        this exact order: [cloud, edge, local]. then this hard-codes the decision
        to be first 50% of the subtasks execute on cloud, next 30% on the edge,
        and last 20% on the local device. all of this can be replaced by a smarter
        scheduling function later
        """
        self.print_elapsed_ms(f"{task} started")

        halfway_point = len(task.subtasks) * 50 // 100
        other_breakpoint = len(task.subtasks) * 80 // 100
        subtask_processes = []

        for i, subtask in enumerate(task.subtasks):
            compute_node = (
                self.compute_nodes[0] if i < halfway_point else
                self.compute_nodes[1] if i < other_breakpoint else
                self.compute_nodes[2]
            )
            p = self.env.process(self._run_subtask(subtask, compute_node))
            subtask_processes.append(p)

        yield self.env.all_of(subtask_processes) # Wait for every subtask
        self.print_elapsed_ms(f"{task} completed!!!!!")



    def submit_task(self, total_num_of_instructions, num_of_subtasks):
        """
        * Creates a new Task with the given parameters and gives it an ID
        * Calls the internal "run_task" generator method on it
        * This creates a generator object for the execution of that Task
        * Passes that generator to a SimPy Process
        """
        self.env.process(self._run_task(
            Task(total_num_of_instructions, num_of_subtasks, next(self.task_id_generator))
        ))



    def run(self):
        """
        * Calls the SimPy "run" method on the Environment
        * This keeps executing until the Environment's queue of Events is empty
        * In this simulator such Events are only queued by executing Tasks and Subtasks
        * So when "run" terminates, all Tasks are finished
        """
        self.env.run()