import simpy
from mec_simulator.compute_node import ComputeNode

env = simpy.Environment

user = ComputeNode(env, "User Device", 10, 4, 0)
edge = ComputeNode(env, "Edge Cluster", 1_000, 8, 5)
cloud = ComputeNode(env, "The Cloud", 10_000, 16, 30)

print(edge.name)
print(edge.cpu.capacity)