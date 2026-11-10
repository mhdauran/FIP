tasks = []


def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("your to-do list is empty.")
    else:
        print("\n--- YOUR TASKS ---")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")


def mark_task_done():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            print("Task marked as completed!")
    except ValueError:
        print("Please enter a valid task number.")


def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number. ")
    except ValueError:
        print("Please enter a valid task number.")
