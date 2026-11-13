from mec_simulator.task import Task
from mec_simulator.simulator import MecSimulator

simulator = MecSimulator()

simulator.add_node("The Cloud", 10_000, 32, 50)
simulator.add_node("Edge Cluster", 1000, 8, 10)
simulator.add_node("User Device", 100, 4, 0)

simulator.submit_task(Task(100, 5))
simulator.run()

