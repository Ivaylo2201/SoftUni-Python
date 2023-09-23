from typing import List
from Classes_and_Objects_Exercise.Tasks.project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:
        for current_task in self.tasks:
            if current_task.name == task_name:
                current_task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        cleared_tasks = 0
        for current_task in self.tasks:
            if current_task.completed:
                self.tasks.remove(current_task)
                cleared_tasks += 1

        return f"Cleared {cleared_tasks} tasks."

    def view_section(self) -> str:
        ordered_tasks = '\n'.join([n_task.details() for n_task in self.tasks])
        return f"Section {self.name}:\n{ordered_tasks}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
