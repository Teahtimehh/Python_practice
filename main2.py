def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


for number in even_numbers(10):
    print(number)


def test_max_number():
    assert max_number(8, 2) == 8, "Ошибка: max_number(8, 2) должна быть равна 8"
    assert max_number(-1, 10) == 10, "Ошибка: max_number(-1, 10) должна быть равна 10"
    assert max_number(100, 50) == 100, "Ошибка: max_number(100, 50) должна быть равна 100"
    assert max_number(7, 7) == 7, "Ошибка: max_number(7, 7) числа одинаковы"
    assert max_number(0, 0) == 0, "Ошибка: max_number(0, 0) числа одинаковы"
    assert max_number(-5, -10) == -5, "Ошибка: max_number(-5, 10) должна быть -5"
    assert max_number(5.5, 6.5) == 6.5, "Ошибка: max_number(5.5, 6.5) должна быть 6.5 "

    print("Все тесты пройдены!")


test_max_number()
