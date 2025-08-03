import os
from task_manager import TaskManager

def run_tests():
    print("\n" + "=" * 40)
    print("Запуск ручных тестов".center(40))
    print("=" * 40)

    test_manager = TaskManager()
    test_file = "test_tasks.json"

    print("\nТест 1: Добавление задач")
    test_manager.add_task("Тестовая задача 1")
    test_manager.add_task("Тестовая задача 2")
    test_manager.add_task("")
    test_manager.add_task("Тестовая задача 1")
    test_manager.list_tasks()

    print("\nТест 2: Выполнение задач")
    test_manager.complete_task(0)
    test_manager.complete_task(0)
    test_manager.complete_task(10)
    test_manager.list_tasks()

    print("\nТест 3: Удаление задач")
    test_manager.remove_task(1)
    test_manager.remove_task(10)
    test_manager.list_tasks()

    print("\nТест 4: Сохранение и загрузка")
    test_manager.save_to_json(test_file)

    new_manager = TaskManager()
    new_manager.load_from_json(test_file)
    new_manager.list_tasks()

    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\nТестовый файл {test_file} удален")

    print("\nВсе тесты завершены!")

if __name__ == "__main__":
    run_tests()