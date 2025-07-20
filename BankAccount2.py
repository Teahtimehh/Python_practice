class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = self.__validate_amount(initial_balance)

    def __validate_amount(self, amount):
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        return amount

    def deposit(self, amount):
        amount = self.__validate_amount(amount)
        self.__balance += amount
        return f"Пополнение на {amount:.2f}₽. Баланс: {self.__balance:.2f}₽"

    def withdraw(self, amount):
        amount = self.__validate_amount(amount)
        if amount > self.__balance:
            return f"Ошибка: Недостаточно средств. Баланс: {self.__balance:.2f}₽"
        self.__balance -= amount
        return f"Снятие {amount:.2f}₽. Остаток: {self.__balance:.2f}₽"

    def get_balance(self):
        return f"Текущий баланс: {self.__balance:.2f}₽"


def bank_menu():
    print("\n" + "=" * 40)
    print("Добро пожаловать в банковскую систему!")
    print("=" * 40)

    try:
        initial = float(input("Введите начальный баланс: "))
        account = BankAccount(initial)
        print(f"Счет создан. {account.get_balance()}")
    except ValueError as e:
        print(f"Ошибка: {e}")
        account = BankAccount()
        print("Создан счет с балансом 0₽")

    while True:
        print("\nМеню:")
        print("1. Проверить баланс")
        print("2. Пополнить счет")
        print("3. Снять средства")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            print(account.get_balance())

        elif choice == "2":
            try:
                amount = float(input("Введите сумму для пополнения: "))
                print(account.deposit(amount))
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            try:
                amount = float(input("Введите сумму для снятия: "))
                print(account.withdraw(amount))
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            print("Спасибо за использование нашей системы! До свидания!")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 4")


if __name__ == "__main__":
    bank_menu()
