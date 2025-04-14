sum_even = sum(i for i in range(2, 101, 2))
print(f"Сумма всех чётных чисел от 1 до 100 равна {sum_even}")

squares_of_oddnumbers = [i**2 for i in range(1, 11, 2)]
print("Cписок квадратов всех нечётных чисел от 1 до 10", squares_of_oddnumbers)

count = 0
while True:
    number = int(input("Введите число: "))
    if number < 0:
        break
    count += 1

print(f"Введено {count} положительных чисел.")