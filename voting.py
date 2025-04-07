def get_age(prompt):
    while True:
        try:
            age = input(prompt)
            age_int = int(age)
            return age_int
        except ValueError:
            try:
                age_float = float(age)
                return age_float
            except ValueError:
                print("Это не число! Пожалуйста, введите число.")


def get_yes_no(question):
    while True:
        answer = input(f"{question} (да/нет) ").strip().lower()
        if answer in ('да', 'yes'):
            return True
        elif answer in ('нет', 'no'):
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")


def main():
    age = get_age("Введите ваш возраст: ")
    
    if not isinstance(age, (int, float)):
        print("Возраст введен неправильно!")
        return

    citizenship = get_yes_no('Вы гражданин этой страны?')
    convictions = get_yes_no('Вы были судимы?')

    if age >= 18 and citizenship and not convictions:
        print("Результат: Вы можете голосовать")
    else:
        print("Результат: Вы не можете голосовать")


if __name__ == "__main__":
    main()
