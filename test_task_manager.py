import os
import json
from task_manager import TaskManager


def test_add_task():
    print("\n=== Тест: Добавление задач ===")
    manager = TaskManager()

    assert manager.add_task("Задача 1") is True, "Не удалось добавить задачу"
    assert manager.add_task("Задача 2") is True, "Не удалось добавить вторую задачу"

    assert len(manager.tasks) == 2, f"Ожидалось 2 задачи, получено {len(manager.tasks)}"

    assert manager.add_task("") is False, "Пустая задача не должна добавляться"

    assert manager.add_task("Задача 1") is False, "Дубликат задачи не должен добавляться"

    assert manager.tasks[0]["description"] == "Задача 1", "Некорректное описание задачи"
    assert manager.tasks[0]["completed"] is False, "Новая задача должна быть невыполненной"

    print("✅ Все тесты добавления задач пройдены успешно")


def test_complete_task():
    print("\n=== Тест: Завершение задач ===")
    manager = TaskManager()
    manager.add_task("Задача 1")
    manager.add_task("Задача 2")

    assert manager.complete_task(0) is True, "Не удалось завершить задачу"
    assert manager.tasks[0]["completed"] is True, "Задача не отмечена как выполненная"

    assert manager.complete_task(0) is False, "Повторное завершение должно возвращать False"

    assert manager.complete_task(10) is False, "Неверный индекс должен возвращать False"

    assert manager.tasks[1]["completed"] is False, "Вторая задача не должна измениться"

    print("✅ Все тесты завершения задач пройдены успешно")


def test_remove_task():
    print("\n=== Тест: Удаление задач ===")
    manager = TaskManager()
    manager.add_task("Задача 1")
    manager.add_task("Задача 2")
    manager.add_task("Задача 3")

    assert manager.remove_task(1) is True, "Не удалось удалить задачу"
    assert len(manager.tasks) == 2, "Неверное количество задач после удаления"
    assert manager.tasks[0]["description"] == "Задача 1", "Первая задача не должна измениться"
    assert manager.tasks[1]["description"] == "Задача 3", "Третья задача должна сместиться на место второй"

    assert manager.remove_task(5) is False, "Неверный индекс должен возвращать False"

    assert manager.remove_task(2) is False, "Нельзя удалить несуществующую задачу"

    print("✅ Все тесты удаления задач пройдены успешно")


def test_save_and_load():
    print("\n=== Тест: Сохранение и загрузка ===")
    test_file = "test_tasks.json"
    manager = TaskManager()
    manager.add_task("Сохраненная задача 1")
    manager.add_task("Сохраненная задача 2")
    manager.complete_task(0)

    assert manager.save_to_json(test_file) is True, "Ошибка сохранения"
    assert os.path.exists(test_file), "Файл не был создан"

    new_manager = TaskManager()
    assert new_manager.load_from_json(test_file) is True, "Ошибка загрузки"

    assert len(new_manager.tasks) == 2, "Неверное количество загруженных задач"
    assert new_manager.tasks[0]["description"] == "Сохраненная задача 1", "Некорректное описание первой задачи"
    assert new_manager.tasks[0]["completed"] is True, "Статус выполнения первой задачи не сохранен"
    assert new_manager.tasks[1]["description"] == "Сохраненная задача 2", "Некорректное описание второй задачи"
    assert new_manager.tasks[1]["completed"] is False, "Статус выполнения второй задачи не сохранен"

    if os.path.exists(test_file):
        os.remove(test_file)

    print("✅ Все тесты сохранения и загрузки пройдены успешно")


def test_boundary_conditions():
    print("\n=== Тест: Граничные условия ===")
    manager = TaskManager()

    assert manager.remove_task(0) is False, "Удаление из пустого списка должно возвращать False"
    assert manager.complete_task(0) is False, "Завершение в пустом списке должно возвращать False"
    manager.list_tasks()

    manager.add_task("Задача")
    assert manager.remove_task(-1) is False, "Отрицательный индекс должен возвращать False"
    assert manager.complete_task(-1) is False, "Отрицательный индекс должен возвращать False"

    assert manager.remove_task(1) is False, "Индекс = длине списка должен возвращать False"
    assert manager.complete_task(1) is False, "Индекс = длине списка должен возвращать False"

    print("✅ Все тесты граничных условий пройдены успешно")


def run_tests():
    print("\n" + "=" * 50)
    print("ЗАПУСК АВТОМАТИЗИРОВАННЫХ ТЕСТОВ".center(50))
    print("=" * 50)

    tests = [
        test_add_task,
        test_complete_task,
        test_remove_task,
        test_save_and_load,
        test_boundary_conditions
    ]

    failed_tests = []

    for test in tests:
        try:
            test()
            print(f"Тест '{test.__name__}' пройден успешно!\n")
        except AssertionError as e:
            print(f"❌ Тест '{test.__name__}' не пройден: {e}\n")
            failed_tests.append(test.__name__)
        except Exception as e:
            print(f"🔥 Ошибка в тесте '{test.__name__}': {e}\n")
            failed_tests.append(test.__name__)

    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ".center(50))
    print("=" * 50)

    if not failed_tests:
        print("✅ ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
    else:
        print(f"❌ НЕ ПРОЙДЕНО ТЕСТОВ: {len(failed_tests)} из {len(tests)}")
        print("Список непройденных тестов:")
        for name in failed_tests:
            print(f"  - {name}")

    print("=" * 50 + "\n")


if __name__ == "__main__":
    run_tests()