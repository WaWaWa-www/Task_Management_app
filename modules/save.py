import json

def save_tasks(tasks):
    """タスクをファイルに保存する関数"""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)