def number_to_word(num):
    words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }

    if num in words:
        return words[num]
    else:
        return "Неправильно введено число!"


number = int(input("Введите число от 1 до 5: "))
print(number_to_word(number))
