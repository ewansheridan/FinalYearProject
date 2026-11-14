from itertools import count

class Task:
    def __init__(self, total_num_of_instructions, num_of_subtasks, task_id):
        """
        * Error checks the parameters
        * Creates a "subtasks" list of size "num_of_subtasks"
        """
        if not isinstance(num_of_subtasks, int) or num_of_subtasks <= 0:
            raise ValueError(f"The number of subtasks must be a positive integer")
        if total_num_of_instructions % num_of_subtasks != 0:
            raise ValueError(f"Task of {total_num_of_instructions} instructions cannot be evenly \
            divided into {num_of_subtasks} homogenous subtasks")

        self.total_num_of_instructions = total_num_of_instructions
        self.subtasks = []
        self.task_id = task_id
        self.subtask_id_generator = count()

        for i in range(num_of_subtasks):
            st = Subtask(total_num_of_instructions / num_of_subtasks, next(self.subtask_id_generator), self)
            self.subtasks.append(st)

    def __str__(self):
        return f"Task ⟨{self.task_id}⟩"


class Subtask:
    def __init__(self, num_of_instructions, subtask_id, task: Task):
        self.num_of_instructions = num_of_instructions
        self.subtask_id = subtask_id
        self.task = task

    def __str__(self):
        return f"Subtask ⟨{self.task.task_id}:{self.subtask_id}⟩"
