class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        if task in self.tasks:
            print(f"Task '{task}' completed!")
            self.tasks.remove(task)
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def display_tasks(self):
        print("To-Do List:")
        for task in self.tasks:
            print(task)

# Example usage:
my_todo_list = ToDoList()
my_todo_list.add_task("Go for a run")
my_todo_list.add_task("Read a book")
my_todo_list.display_tasks()
my_todo_list.complete_task("Go for a run")
my_todo_list.display_tasks()
