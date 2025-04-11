def getpositiveinteger():
    while True:
        try:
            number = int(input("Введите целое положительное число: "))
            if number > 0:
                return number
            else:
                print("Ошибка! Введено неправильное число. Попробуйте снова.")
        except ValueError:
            print("Ошибка! Вы ввели некорректное значение. Попробуйте снова.")


number = getpositiveinteger()

while number >= 0:
    print(number)
    number -= 1
