# Simulation & Scheduling of Parallelisable Tasks Across Local Devices and MEC Infrastructure

The computational power of laptops, smartphones and other user devices has improved dramatically in recent years. The cloud computing paradigm was first introduced to allow users to execute large computations by performing said computations on servers in datacentres. This meant that large problems could be computed in an acceptable time, but for smaller problems, the network overhead of offloading to the cloud was non-negligible. Multi-access edge computing brought slightly less powerful machines geographically closer to users, which decreased RTTs considerably and improved the overall latency of task completion. 

This project poses the question: _What if some of the computation could be done on the local device itself?_ To completely eliminate edge and cloud offloading would be impractical for large tasks, so in this project tasks are divided into subtasks that can run in parallel. A scheduling algorithm divides these subtasks into three groups to run on the cloud, the edge cluster, and the local device itself.

To facilitate the development and testing of this algorithm, a simulator is also developed using the _SimPy_ Python framework. The creation of this simulator and the implementation of the local-device-aware parallel scheduling algorithm form the main body of work for this project.

This project is a work-in-progress and is the basis of a thesis for a BSc in Computer Science at UCD, which won't be complete until summer 2027.
