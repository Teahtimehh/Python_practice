class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if not task.strip():
            print("Ошибка: нельзя добавить пустую задачу.")
            return

        task_lower = task.lower()
        existing_task = next((t for t in self.tasks if t.lower() == task_lower), None)

        if existing_task is not None:
            print(f'Задача "{existing_task}" уже существует (учтен регистр).')
        else:
            self.tasks[task] = False
            print(f'Задача "{task}" добавлена.')

    def complete_task(self, task):
        task_lower = task.lower()
        matching_task = next((t for t in self.tasks if t.lower() == task_lower), None)

        if matching_task is not None:
            if not self.tasks[matching_task]:
                self.tasks[matching_task] = True
                print(f'Задача "{matching_task}" отмечена как выполненная.')
            else:
                print(f'Задача "{matching_task}" уже была выполнена ранее.')
        else:
            print(f'Задача "{task}" не найдена.')

    def remove_task(self, task):
        task_lower = task.lower()
        matching_task = next((t for t in self.tasks if t.lower() == task_lower), None)

        if matching_task is not None:
            del self.tasks[matching_task]
            print(f'Задача "{matching_task}" удалена.')
        else:
            print(f'Задача "{task}" не найдена.')

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("Список задач:")
        for task, completed in self.tasks.items():
            status = "✓" if completed else "✗"
            print(f"- {task} {status}")


def main():
    todo = ToDoList()

    menu_options = {
        '1': {'title': 'Добавить задачу', 'action': lambda: todo.add_task(input("Введите задачу: "))},
        '2': {'title': 'Завершить задачу', 'action': lambda: todo.complete_task(input("Введите задачу: "))},
        '3': {'title': 'Удалить задачу', 'action': lambda: todo.remove_task(input("Введите задачу: "))},
        '4': {'title': 'Показать список задач', 'action': todo.list_tasks},
        '5': {'title': 'Выход', 'action': exit}
    }

    while True:
        print("\n--- Меню To-Do List ---")
        for key, option in menu_options.items():
            print(f"{key}. {option['title']}")

        choice = input("Выберите действие: ")

        if choice in menu_options:
            menu_options[choice]['action']()
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт из меню.")


if __name__ == "__main__":
    main()