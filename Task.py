class Task:
    def _init_(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

# Create a list to store tasks
tasks = []

# Function to add a new task
def add_task():
    # Prompt user for task details
    description = input("Enter task description: ")
    priority = input("Enter task priority (high, medium, low): ")
    due_date = input("Enter task due date: ")

    # Create a new task object
    task = Task(description, priority, due_date)

    # Add task to the list
    tasks.append(task)

# Function to remove a task
def remove_task():
    # Prompt user for task index
    index = int(input("Enter task index to remove: "))

    # Remove task from the list
    if index >= 0 and index < len(tasks):
        tasks.pop(index)
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

# Function to mark a task as completed
def mark_completed():
    # Prompt user for task index
    index = int(input("Enter task index to mark as completed: "))

    # Mark task as completed
    if index >= 0 and index < len(tasks):
        tasks[index].completed = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

# Function to display all tasks
def display_tasks():
    # Check if there are any tasks
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        # Iterate over tasks and display details
        for index, task in enumerate(tasks):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index}. {task.description} - Priority: {task.priority} - Due Date: {task.due_date} - Status: {status}")

# Main program loop
while True:
    # Display menu options
    print("Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. Display Tasks")
    print("5. Exit")

    # Prompt user for