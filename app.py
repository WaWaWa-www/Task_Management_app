import json
from modules.load import load_tasks
from modules.save import save_tasks
from modules.display import display_tasks
from modules.add import add_task
from modules.remove import remove_task

def main():
    # タスクを格納するリスト
    tasks = []
    tasks = load_tasks(tasks)
    while True:
        print("\n1. タスク一覧を表示")
        print("2. タスクを追加")
        print("3. タスクを削除")
        print("4. 終了")
        choice = input("選択肢を入力してください: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            tasks = add_task(tasks)
        elif choice == "3":
            tasks = remove_task(tasks)
        elif choice == "4":
            print("アプリを終了します。")
            save_tasks(tasks)
            break
        else:
            print("無効な選択です。再度選択してください。")

if __name__ == "__main__":
    main()
