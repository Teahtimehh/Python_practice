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
        print(f"Пополнение на {amount:.2f}₽. Новый баланс: {self.__balance:.2f}₽")

    def withdraw(self, amount):
        amount = self.__validate_amount(amount)
        if amount > self.__balance:
            print(f"Ошибка: Недостаточно средств. Текущий баланс: {self.__balance:.2f}₽")
            return False
        self.__balance -= amount
        print(f"Снятие {amount:.2f}₽. Остаток: {self.__balance:.2f}₽")
        return True

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Текущий баланс: {self.__balance:.2f}₽"


if __name__ == "__main__":
    try:
        account = BankAccount(1000)
        print(account)

        account.deposit(500)

        account.withdraw(200)
        account.withdraw(2000)

        bad_account = BankAccount(-100)
    except ValueError as e:
        print(f"Ошибка: {e}")