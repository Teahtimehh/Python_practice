class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = self._validate_amount(initial_balance)

    @staticmethod
    def _validate_amount(amount):
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        return amount

    def deposit(self, amount):
        amount = self._validate_amount(amount)
        self.__balance += amount
        return f"Пополнение на {amount:.2f}₽. Баланс: {self.__balance:.2f}₽"

    def withdraw(self, amount):
        amount = self._validate_amount(amount)
        if amount > self.__balance:
            return f"Ошибка: Недостаточно средств. Баланс: {self.__balance:.2f}₽"
        self.__balance -= amount
        return f"Снятие {amount:.2f}₽. Остаток: {self.__balance:.2f}₽"

    def get_balance(self):
        return f"Текущий баланс: {self.__balance:.2f}₽"


def bank_menu():
    print("\n" + "=" * 40 + "\nДобро пожаловать в банковскую систему!\n" + "=" * 40)

    try:
        initial = float(input("Введите начальный баланс: "))
        account = BankAccount(initial)
        print(f"Счет создан. {account.get_balance()}")
    except ValueError as e:
        print(f"Ошибка: {e}\nСоздан счет с балансом 0₽")
        account = BankAccount()

    menu_actions = {
        '1': {
            'title': 'Проверить баланс',
            'action': lambda: print(account.get_balance())
        },
        '2': {
            'title': 'Пополнить счет',
            'action': lambda: (
                amount := float(input("Введите сумму для пополнения: ")),
                print(account.deposit(amount))
            )
        },
        '3': {
            'title': 'Снять средства',
            'action': lambda: (
                amount := float(input("Введите сумму для снятия: ")),
                print(account.withdraw(amount))
            )
        },
        '4': {
            'title': 'Выход',
            'action': lambda: (print("Спасибо за использование! До свидания!"), exit())
        }
    }

    while True:
        print("\nМеню:\n" + "\n".join(f"{key}. {option['title']}" for key, option in menu_actions.items()))

        choice = input("Выберите действие: ").strip()

        if choice in menu_actions:
            try:
                menu_actions[choice]['action']()
            except ValueError as e:
                print(f"Ошибка: {e}")
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт из меню")


if __name__ == "__main__":
    bank_menu()