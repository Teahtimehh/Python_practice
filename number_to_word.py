def number_to_word(num):
    words = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five'
    }

    if num in words:
        return words[num]
    else:
        return "Неправильно введено число!"


number = int(input("Введите число от 1 до 5: "))
print("Соответствующее слово:",number_to_word(number))
