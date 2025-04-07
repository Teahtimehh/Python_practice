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
    age = get_yes_no('Вам есть 18 лет?')
    citizenship = get_yes_no('Вы гражданин этой страны?')
    convictions = get_yes_no('Вы были судимы?')

    if age == True and citizenship and not convictions:
        print("Результат: Вы можете голосовать")
    else:
        print("Результат: Вы не можете голосовать")


main()
