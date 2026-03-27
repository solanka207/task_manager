from .models import Task

def add_task(tasks: list,
             title: str) -> list:
    new_id = len(tasks) + 1
    new_task = Task(new_id, title)
    return tasks + [new_task]


def get_tasks_by_status(tasks: list,
                        status: str = "new") -> list:
    result = []
    for task in tasks:
        if task.status == status:
            result.append(task)
    return  result


def sort_tasks(tasks:list, reverse: bool = False) -> list:
    tasks_copy = tasks[:]

    for i in range(len(tasks_copy)):
        for j in range(i + 1, len(tasks_copy)):
            if reverse:
                if tasks_copy[i].id < tasks_copy[j].id:
                    tasks_copy[i], tasks_copy[j] = tasks_copy[j], tasks_copy[i]
            else:
                if tasks_copy[i].id > tasks_copy[j].id:
                    tasks_copy[i], tasks_copy[j] = tasks_copy[j], tasks_copy[i]
    return  tasks_copy
