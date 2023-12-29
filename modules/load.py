import json

def load_tasks(tasks):
    """タスクをファイルから読み込む関数"""
    try:
        with open("tasks.json", "r") as file:
            file_content = file.read()
            if file_content:
                tasks.extend(json.loads(file_content))
            return tasks
    except FileNotFoundError:
        return tasks