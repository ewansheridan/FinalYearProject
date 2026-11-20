from mec_simulator.simulator import MecSimulator
'''
simulator = MecSimulator()

simulator.add_node("The Cloud", 70, 32, 40)
simulator.add_node("Edge Cluster", 14, 2, 16)
simulator.add_node("User Device", 7, 1, 0)
simulator.submit_task(700, 10)
simulator.submit_task(700, 10)
simulator.submit_task(700, 10)

simulator.run()
'''


simulator = MecSimulator()

simulator.add_node("The Cloud", 60, 100, 50)
simulator.add_node("Edge Cluster", 6, 2, 30)
simulator.add_node("User Device", 3, 1, 0)

simulator.submit_task(300, 5)
simulator.submit_task(360, 6)

simulator.run()



