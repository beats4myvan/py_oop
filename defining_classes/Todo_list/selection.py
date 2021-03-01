from defining_classes.Todo_list.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.task = []

    def add_task(self, new_task: Task):
        for i in self.task:
            if i == new_task:
                self.task.append(i)
                return f"Task {new_task} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        pass

    def clean_section(self):
        pass

    def view_section(self):
        pass
