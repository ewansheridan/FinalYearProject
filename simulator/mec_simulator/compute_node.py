import simpy

class ComputeNode:
    def __init__(self, env, name, speed_per_core_ipms, num_of_cores, rtt_ms):
        self.env = env
        self.name = name
        self.speed_per_core_ipms = speed_per_core_ipms # instructions per millisecond
        self.num_of_cores = num_of_cores
        self.rtt_ms = rtt_ms

        self.cpu = simpy.Resource(env, capacity=num_of_cores)
