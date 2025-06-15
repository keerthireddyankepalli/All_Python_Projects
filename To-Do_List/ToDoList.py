import json

class Task:
    def __init__(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def _str_(self):
        status = "✅ Done" if self.completed else "❌ Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"

class TaskManager:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, title):
        original_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.title != title]
        if len(self.tasks) < original_len:
            print("Task removed successfully!")
        else:
            print("Task not found!")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print("Task marked as completed!")
                return
        print("Task not found!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        for task in self.tasks:
            print(task)

    def save_tasks(self, filename='tasks.json'):
        data = [{
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date,
            'completed': task.completed
        } for task in self.tasks]

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task(**item) for item in data]
        except FileNotFoundError:
            self.tasks = []

# Sample run with menu
def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("\n---- TO-DO LIST MENU ----")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Show All Tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title,description,due_date)
            manager.add_task(task)

        elif choice == '2':
            title = input("Enter the title of the task to remove: ")
            manager.remove_task(title)

        elif choice == '3':
            title = input("Enter the title of the task to mark as completed: ")
            manager.mark_task_completed(title)

        elif choice == '4':
            manager.show_tasks()

        elif choice == '5':
            manager.save_tasks()
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()