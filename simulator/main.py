from mec_simulator.task import Task
from mec_simulator.simulator import MecSimulator

simulator = MecSimulator()

simulator.add_node("The Cloud", 70, 32, 40)
simulator.add_node("Edge Cluster", 14, 2, 16)
simulator.add_node("User Device", 7, 1, 0)

simulator.submit_task(700, 10)
simulator.run()

