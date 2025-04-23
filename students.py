students = [
    {"name": "Harry", "grades": [80, 90, 85]},
    {"name": "Ron", "grades": [60, 70, 65]},
    {"name": "Hermione", "grades": [95, 90, 92]}
]


students.append({"name": "Draco", "grades": [70, 66, 95]})
del students[1]

def calculate_average(grades):
    return sum(grades) / len(grades)


for student in students:
    name = student["name"]
    grades = student["grades"]

    average_grade = round(calculate_average(grades), 2)

    if average_grade >= 75:
        status = "Успешен"
    else:
        status = "Отстающий"

    print(f"Студент: {name}\nСредний балл: {average_grade:.2f}\nСтатус: {status}")
    print("---------------------")


def overall_average(students):
    total_sum = 0
    count = 0
    for student in students:
        total_sum += sum(student['grades'])
        count += len(student['grades'])
    return round(total_sum / count, 2)


print(f"\nОбщий средний балл всех студентов: {overall_average(students)}")
