def getwords(password="lucky"):
    while True:
        words = str(input("Введите пароль: "))
        if words == password:
            return words
        else:
            print("Ошибка! Введён неправильный пароль. Попробуйте снова.")


number = getwords()
print("Вы ввели правильный пароль:", number)
