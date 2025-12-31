tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("No tasks available")
    for task in tasks:
        print(task)

