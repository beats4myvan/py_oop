class Section:
    def __init__(self, name):
        self.name = name
        self.task = []

    def add_task(self, new_task):
        if new_task not in self.task:
            self.task.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for current_task in self.task:
            if current_task.name == task_name:
                current_task.completed = True
                return f'Completed task {task_name}'
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = [task for task in self.task if task.completed == True]
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        return f"Section {self.name}:\n" + '\n'.join([task.details() for task in self.task])

