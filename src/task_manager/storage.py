import json
import os
from .models import Task


def save_tasks(tasks: list, filename: str):
    data = []
    for task in tasks:
        data.append(task.to_dict())


    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_tasks(filename: str) -> list:
    if not os.path.exists(filename):
        return []


    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

        tasks = []
        for item in data:
            tasks.append(Task.from_dict(item))
        return  tasks
