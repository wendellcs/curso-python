class Task_manager:
    __task_list = []
    def __init__(self, task):
        if task:
            self.task = task
            self.done = False
            self.task_id = len(Task_manager.__task_list)

    def __str__(self):
        return f'value {self.task}'

    def toggle_done(self):
        self.done = not self.done

    @classmethod
    def add_task(cls, task):
        for t in Task_manager.__task_list:
            if t.task == task.task:
                return 'Essa tarefa já existe'

        Task_manager.__task_list.append(task)

    @classmethod
    def delete_task(cls, id):
        for t in Task_manager.__task_list:
            if t.task_id == id:
                Task_manager.__task_list.pop(Task_manager.get_task_index(t))

    @classmethod
    def edit_task(cls, id, new_task):
        for t in Task_manager.__task_list:
            if t.task_id == id:
                Task_manager.__task_list[Task_manager.get_task_index(t)].task = new_task
                
    def get_task_index(t):
        return Task_manager.__task_list.index(t)

    def get_task_list():
        return Task_manager.__task_list