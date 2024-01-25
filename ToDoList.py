class ToDoList:
    def __init__(self):
        self.tasks = []

    def displayTasks(self):
        if not self.tasks:
            print("No tasks is present here.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = ' [X]' if task['completed'] else ' [ ]'
                print(f"{index}. {task['description']}{status}") 

    def addTask(self, description):
        task = {'description': description, 'completed': False}
        self.tasks.append(task)
        print(f"'{description}' added.")

    def deleteTask(self, index):
        if 1<=index<=len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"'{deleted_task['description']}' deleted.")
        else:
            print("Please input valid index.")

    def markCompleted(self, index):
        if 1<=index<=len(self.tasks):
            self.tasks[index - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Please input valid index.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print('\n---To Do List---')
        todo_list.displayTasks()
        print('Enter your choice:\n1.ADD TASKS\n2.DELETE TASK\n3.MARKED THE COMPLETED TASK\n4.EXIT')
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.addTask(description)
        elif choice == '2':
            index = int(input("Enter task index to delete: "))
            todo_list.deleteTask(index)
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            todo_list.markCompleted(index)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")