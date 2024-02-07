import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task index.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\n1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            to_do_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == '3':
            task_index = int(input("Enter the task index to remove: "))
            to_do_list.remove_task(task_index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
