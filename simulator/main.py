import simpy
from mec_simulator.compute_node import *

env = simpy.Environment

user = ComputeNode(
    env=env,
    name="User Device",
    mips_per_core=10,
    num_of_cores=4,
    rtt=0
)

edge = ComputeNode(
    env = env,
    name = "Edge Cluster",
    mips_per_core = 1_000,
    num_of_cores = 8,
    rtt = 5 # milliseconds
)

cloud = ComputeNode(
    env = env,
    name = "The Cloud",
    mips_per_core = 10000,
    num_of_cores = 16,
    rtt = 30
)

print(edge.name)
print(edge.cpu.capacity)