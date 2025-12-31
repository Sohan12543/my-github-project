tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("Task list is empty")
        return
    for task in tasks:
        print(task)

