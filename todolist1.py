class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = False
            print(f'Задача "{task}" добавлена.')
        else:
            print(f'Задача "{task}" уже существует.')

    def complete_task(self, task):
        if task in self.tasks:
            if not self.tasks[task]:
                self.tasks[task] = True
                print(f'Задача "{task}" отмечена как выполненная.')
            else:
                print(f'Задача "{task}" уже была выполнена ранее.')
        else:
            print(f'Задача "{task}" не найдена.')

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f'Задача "{task}" удалена.')
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


if __name__ == "__main__":
    todo = ToDoList()

    todo.add_task("Купить продуктов")
    todo.add_task("Сделать уборку дома")
    todo.add_task("Позвонить маме")

    todo.list_tasks()

    todo.complete_task("Купить продуктов")
    todo.complete_task("Несуществующая задача")

    todo.list_tasks()

    todo.remove_task("Купить продуктов")
    todo.remove_task("Несуществующая задача")

    todo.list_tasks()
