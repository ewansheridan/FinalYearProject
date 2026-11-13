import simpy

class ComputeNode:
    def __init__(self, env, name, mips_per_core, num_of_cores, rtt):
        self.env = env
        self.name = name
        self.mips_per_core = mips_per_core
        self.num_of_cores = num_of_cores
        self.rtt = rtt

        self.cpu = simpy.Resource(env, capacity=num_of_cores)
