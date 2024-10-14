class TaskManager:
    def _init_(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:

            with open("tasks.txt", "r") as file:
                return [line.strip().split(":") for line in file.readlines()]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task[0]}:{task[1]}\n")

    def add_task(self):
        task_name = input("Enter task name: ")
        self.tasks.append([task_name, "Incomplete"])
        self.save_tasks()

    def edit_task(self):
        task_name = input("Enter task name to edit: ")
        for task in self.tasks:
            if task[0] == task_name:
                task[0] = input("Enter new task name: ")
                self.save_tasks()
                break

    def delete_task(self):
        task_name = input("Enter task name to delete: ")
        self.tasks = [task for task in self.tasks if task[0] != task_name]
        self.save_tasks()

    def mark_task_complete(self):
        task_name = input("Enter task name to mark complete: ")
        for task in self.tasks:
            if task[0] == task_name:
                task[1] = "Complete"
                self.save_tasks()
                break

    def display_tasks(self):
        print("Task List:")
        for task in self.tasks:
            print(f"{task[0]} - {task[1]}")

    def run(self):
        while True:
            print("\n1. Add Task")
            print("2. Edit Task")
            print("3. Delete Task")
            print("4. Mark Task Complete")
            print("5. Display Tasks")
            print("6. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.edit_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.mark_task_complete()
            elif choice == "5":
                self.display_tasks()
            elif choice == "6":
                break

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()


    o/p:-C:\Users\LENOVO\Desktop\PythonProject intern>py To-DoListApplication.py

1. Add Task
2. Edit Task
3. Delete Task
4. Mark Task Complete
5. Display Tasks
6. Exit
Enter choice: