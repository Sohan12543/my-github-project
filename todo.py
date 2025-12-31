tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    for task in tasks:
        print(task)

