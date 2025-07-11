class ToDoList:
    def __init__(self):
        self.tasks = {}

    def _find_task(self, task_name):
        task_name = task_name.strip().lower()
        for existing_task in self.tasks:
            if existing_task.lower().strip() == task_name:
                return existing_task
        return None

    def _get_existing_task(self, task):
        existing_task = self._find_task(task)
        if existing_task is None:
            print(f'Задача "{task.strip()}" не найдена.')
        return existing_task

    def add_task(self, task):
        task = task.strip()
        if not task:
            print("Ошибка: нельзя добавить пустую задачу.")
            return

        if self._find_task(task) is not None:
            print(f'Задача "{task}" уже существует.')
        else:
            self.tasks[task] = False
            print(f'Задача "{task}" добавлена.')

    def complete_task(self, task):
        existing_task = self._get_existing_task(task)
        if existing_task is None:
            return

        if self.tasks[existing_task]:
            print(f'Задача "{existing_task}" уже была выполнена ранее.')
        else:
            self.tasks[existing_task] = True
            print(f'Задача "{existing_task}" отмечена как выполненная.')

    def remove_task(self, task):
        existing_task = self._get_existing_task(task)
        if existing_task is None:
            return

        del self.tasks[existing_task]
        print(f'Задача "{existing_task}" удалена.')

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
        '1': {
            'title': 'Добавить задачу',
            'action': lambda: todo.add_task(input("Введите задачу: "))
        },
        '2': {
            'title': 'Завершить задачу',
            'action': lambda: todo.complete_task(input("Введите задачу: "))
        },
        '3': {
            'title': 'Удалить задачу',
            'action': lambda: todo.remove_task(input("Введите задачу: "))
        },
        '4': {
            'title': 'Показать список задач',
            'action': todo.list_tasks
        },
        '5': {
            'title': 'Выход',
            'action': exit
        }
    }

    while True:
        print("\n--- Меню To-Do List ---")
        for key, option in menu_options.items():
            print(f"{key}. {option['title']}")

        choice = input("Выберите действие: ").strip()

        if choice in menu_options:
            menu_options[choice]['action']()
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт из меню.")


if __name__ == "__main__":
    main()
