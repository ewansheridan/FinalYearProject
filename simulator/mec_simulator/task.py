class Task:
    def __init__(self, total_mi, num_of_subtasks):
        if not isinstance(num_of_subtasks, int) or num_of_subtasks <= 0:
            raise ValueError(f"The number of subtasks must be a positive integer")

        if total_mi % num_of_subtasks != 0:
            raise ValueError(f"Task of {total_mi} mi cannot be evenly \
            divided into {num_of_subtasks} homogenous subtasks")

        self.total_mi = total_mi
        self.num_of_subtasks = num_of_subtasks
        self.subtasks = []

        for i in range(num_of_subtasks):
            self.subtasks.append(_Subtask(total_mi / num_of_subtasks))

class _Subtask:
    def __init__(self, mi):
        self.mi = mi