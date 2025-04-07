def get_age(prompt):
    while True:
        try:
            age = input(prompt)
            age_float = float(age)
            if age_float.is_integer():
                return int(age_float)
            else:
                return age_float
        except ValueError:
            print("Это не число! Пожалуйста, введите число.")


def get_citizenship():
    while True:
        citizenship = input('Вы гражданин этой страны? (да/нет) ').lower()

        if citizenship == 'да':
            return True
        elif citizenship == 'нет':
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")
            continue


def get_convictions():
    while True:
        convictions = input('Вы были судимы? (да/нет) ').lower()
        if convictions == 'да':
            return True
        elif convictions == 'нет':
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'")
            continue


def main():
    age = get_age("Введите ваш возраст: ")
    if not isinstance(age, (int, float)):
        print("Возраст введен неправильно!")
        return

    citizenship = get_citizenship()
    if citizenship is None:
        print("Гражданство введено неправильно!")
        return get_citizenship()

    convictions = get_convictions()
    if convictions is None:
        print("Информация о судимости введена неправильно!")
        return get_convictions()

    if age >= 18 and citizenship == True and convictions == False:
        print("Результат: Вы можете голосовать")
    else:
        print("Результат: Вы не можете голосовать")


main()