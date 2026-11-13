from itertools import count

class Task:
    def __init__(self, total_mi, num_of_subtasks, id):
        if not isinstance(num_of_subtasks, int) or num_of_subtasks <= 0:
            raise ValueError(f"The number of subtasks must be a positive integer")

        if total_mi % num_of_subtasks != 0:
            raise ValueError(f"Task of {total_mi} mi cannot be evenly \
            divided into {num_of_subtasks} homogenous subtasks")

        self.total_mi = total_mi
        self.subtasks = []
        self.id = id
        self.subtask_id_generator = count()

        for i in range(num_of_subtasks):
            st = Subtask(total_mi / num_of_subtasks, next(self.subtask_id_generator), self)
            self.subtasks.append(st)

class Subtask:
    def __init__(self, mi, id, task: Task):
        self.mi = mi
        self.id = id
        self.task = task

        self.idStr = f"⟨{self.task.id}:{self.id}⟩"

# do subtasks really need to exist as objects? instead of a
# list of them could you not just store how many there are and what the mi per subtask is?