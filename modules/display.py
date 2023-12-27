def display_tasks(tasks):
    """現在のタスクを表示する関数"""
    print("=== タスク一覧 ===")
    if not tasks:
        print("タスクはありません")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("================")