import json
import os


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str):
        description = description.strip()
        if not description:
            print("Ошибка: описание задачи не может быть пустым.")
            return False

        if any(task["description"].lower() == description.lower() for task in self.tasks):
            print(f'Задача "{description}" уже существует.')
            return False

        self.tasks.append({
            "description": description,
            "completed": False
        })
        print(f'Задача "{description}" добавлена.')
        return True

    def complete_task(self, index: int):
        if not self._is_valid_index(index):
            print("Ошибка: неверный индекс задачи.")
            return False

        if self.tasks[index]["completed"]:
            print(f'Задача "{self.tasks[index]["description"]}" уже выполнена.')
            return False

        self.tasks[index]["completed"] = True
        print(f'Задача "{self.tasks[index]["description"]}" отмечена как выполненная.')
        return True

    def remove_task(self, index: int):
        if not self._is_valid_index(index):
            print("Ошибка: неверный индекс задачи.")
            return False

        description = self.tasks[index]["description"]
        del self.tasks[index]
        print(f'Задача "{description}" удалена.')
        return True

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("Список задач:")
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i + 1}. [{status}] {task['description']}")

    def save_to_json(self, filename: str):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
            print(f"Задачи сохранены в {filename}")
            return True
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
            return False

    def load_from_json(self, filename: str):
        try:
            if not os.path.exists(filename):
                print(f"Файл {filename} не найден")
                return False

            with open(filename, 'r', encoding='utf-8') as f:
                self.tasks = json.load(f)
            print(f"Задачи загружены из {filename}")
            return True
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")
            return False

    def _is_valid_index(self, index: int):
        return 0 <= index < len(self.tasks)


def main():
    manager = TaskManager()

    menu_options = {
        '1': {
            'title': 'Добавить задачу',
            'action': lambda: manager.add_task(input("Введите описание задачи: "))
        },
        '2': {
            'title': 'Завершить задачу',
            'action': lambda: manager.complete_task(
                int(input("Введите номер задачи: ")) - 1
            )
        },
        '3': {
            'title': 'Удалить задачу',
            'action': lambda: manager.remove_task(
                int(input("Введите номер задачи: ")) - 1
            )
        },
        '4': {
            'title': 'Показать список задач',
            'action': manager.list_tasks
        },
        '5': {
            'title': 'Сохранить в JSON',
            'action': lambda: manager.save_to_json(input("Введите имя файла: "))
        },
        '6': {
            'title': 'Загрузить из JSON',
            'action': lambda: manager.load_from_json(input("Введите имя файла: "))
        },
        '7': {
            'title': 'Запустить тесты',
            'action': lambda: run_tests_imported()
        },
        '8': {
            'title': 'Выход',
            'action': exit
        }
    }

    def run_tests_imported():
        try:
            from test_task_manager import run_tests
            run_tests()
        except ImportError:
            print("Ошибка: Модуль тестов не найден!")
        except Exception as e:
            print(f"Ошибка при запуске тестов: {e}")

    while True:
        print("\n" + "=" * 40)
        print("Менеджер задач".center(40))
        print("=" * 40)
        for key, option in menu_options.items():
            print(f"{key}. {option['title']}")

        choice = input("\nВыберите действие: ").strip()

        if choice in menu_options:
            try:
                menu_options[choice]['action']()
            except ValueError:
                print("Ошибка: введено некорректное значение! Требуется число.")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт из меню.")

if __name__ == "__main__":
    main()