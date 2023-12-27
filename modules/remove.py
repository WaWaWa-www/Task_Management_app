from .display import display_tasks
from .save import save_tasks

def remove_task(tasks):
    """タスクを削除する関数"""
    display_tasks(tasks)
    task_index = int(input("削除したいタスクの番号を入力してください: ")) - 1

    try:
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"タスク '{removed_task}' を削除しました")
        return tasks
    except IndexError:
        print("無効な番号です")