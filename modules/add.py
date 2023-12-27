from .save import save_tasks

def add_task(tasks):
    """新しいタスクを追加する関数"""
    new_task = input("新しいタスクを入力してください: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"タスク '{new_task}' を追加しました")
    return tasks