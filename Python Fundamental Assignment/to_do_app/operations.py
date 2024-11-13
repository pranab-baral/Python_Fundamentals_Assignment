tasks = []  

def add_task(task):
    tasks.append(task)

def view_tasks():
    return tasks

def delete_task(index):
    if 0 <= index < len(tasks):
        return tasks.pop(index)
    else:
        return None